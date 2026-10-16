# Engineering case studies

A selection of technical work with **links to source, regression tests and CI**. These notes cover the concrete engineering decisions behind the projects, including their current limitations. They are intended to be checked against the public repositories rather than taken on faith.

Updated: 16 October 2026 (IST).

## 1. LeaseLedger — explicit correctness contracts for durable work

**Repository:** [LeaseLedger](https://github.com/harshitethic/LeaseLedger)
**Evidence:** [Live executable demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md) · [Machine-checked output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json) · [CI matrix](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml) · [Release v0.1.3](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.3) · [100-expired-leases bug reproduction](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/expired-lease-cleanup-progress.md) · [Fencing-token failure analysis](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/why-fencing-tokens.md) · [WAL-safe recovery runbook](https://github.com/harshitethic/LeaseLedger/blob/main/docs/backup-and-recovery.md)

**Problem:** Naive job processing loses work when a worker crashes and allows a
paused worker to acknowledge a job after its lease has been reassigned.

**Design:** SQLite WAL for durability, `BEGIN IMMEDIATE` for atomic multi-process
claims, monotonic fencing tokens, deadline-validated acknowledgements, worker
heartbeats, idempotent submissions, bounded retries and dead-letter records.
Every transition writes a durable audit event in the same transaction.

**Verification:** Forty automated tests passed on Python 3.11, 3.12 and
3.13, including four real processes competing for 48 jobs, an abrupt worker
process termination followed by fenced recovery, and concurrent online backups.
A separate deterministic reference model covers 640 seeded operations, while
a regression creates 121 expired high-priority leases and proves a ready job
behind them is still claimed in one call. The bug is fixed in v0.1.2.
SQLite snapshots are verified for page and foreign-key integrity and refuse
overwriting existing files. A working single-command walkthrough reproduces
the observable queue lifecycle, and its actual stdout JSON is versioned and
compared in CI on three Python versions. Ruff, packaging and benchmark-smoke CI also pass.

**Writer-contention follow-through:** [PR #5](https://github.com/harshitethic/LeaseLedger/pull/5) reproduced an expiry bypass: ACK, heartbeat and failure sampled time before waiting for the SQLite writer lock. A lease that expired during that wait could still mutate the queue. Time is now sampled after acquisition, with refreshed claim selection and producer delays. Six regressions use a real SQLite blocker and an injected clock; all six fail on the previous implementation. The complete 40-test suite and four-process benchmark smoke passed on Kali/Python 3.12 and macOS/Python 3.14, followed by Python 3.11–3.13 CI and CodeQL. [Failure analysis and timing contract](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/lease-expiry-after-lock.md) distinguish validation time from response delivery and external effects.

**Delivery follow-through:** [PR #6](https://github.com/harshitethic/LeaseLedger/pull/6) makes releases depend on the complete Python test/packaging matrix, benchmark smoke, lint and reusable CodeQL gate. Eight publication-boundary tests bring the suite to **48 tests** and cover immutable releases, conflicting/annotated tags, stale main commits, version/changelog mismatches and API errors. Only the final main-push job has release write permission. The [actual successful main workflow](https://github.com/harshitethic/LeaseLedger/actions/runs/38745249190) published [v0.1.3](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.3) at verified commit `783ad67`; this is live publication evidence, not only a mocked API test. [Release recovery and limitations](https://github.com/harshitethic/LeaseLedger/blob/main/docs/releases.md) explicitly forbid moving conflicting tags and distinguish GitHub source releases from PyPI distribution or service deployment.

**Performance evidence:** [PR #7](https://github.com/harshitethic/LeaseLedger/pull/7) adds repeated finite-backlog experiments with operation p50/p95/p99s, retries, actual handler timing, process cleanup and exact job/event accounting. Six benchmark regressions bring the suite to **54 tests**, passing on Kali/macOS and in Python 3.11–3.13 CI alongside packaging, lint, benchmark smoke and CodeQL. The [recorded 60 trials](https://github.com/harshitethic/LeaseLedger/blob/main/docs/workload-benchmarks.md) completed 18,000 jobs and 1,800 retries on Kali and macOS; every trial is retained with source fingerprints. Added instrumentation exposed that requested 5 ms sleeps actually had 173–191 ms per-trial handler medians on the Mac versus about 5.1 ms on Kali. The cause remains unisolated, so the writeup explicitly rejects cross-device capacity comparisons. No-op scaling was non-monotonic, worker shares could be uneven, and p99s/maxima remain inspectable. This is synthetic workload evidence, not a production SLO or benchmark against another broker.

**Trade-off:** This is a **single-host, at-least-once** queue. It is not
distributed consensus, exactly-once external processing or a verified
production-scale benchmark. Handler code is trusted local Python.

---

## 2. PatchPilot — reducing the attack surface of an AI coding agent

**Repository:** [PatchPilot](https://github.com/harshitethic/PatchPilot)
**Change reviews:** [Repository trust boundaries](https://github.com/harshitethic/PatchPilot/pull/13) · [Safe workspace lifecycle](https://github.com/harshitethic/PatchPilot/pull/19) · [Docker test isolation](https://github.com/harshitethic/PatchPilot/pull/24) · [Host Git-only execution and private logs](https://github.com/harshitethic/PatchPilot/pull/25) · [Prevent hostile Git hooks and internal control-file edits](https://github.com/harshitethic/PatchPilot/pull/26) · [Verified loopback and bearer HTTP protection](https://github.com/harshitethic/PatchPilot/pull/27) · [Verified sensitive-commit refusal](https://github.com/harshitethic/PatchPilot/pull/28) · [Protect AI source context and provider errors](https://github.com/harshitethic/PatchPilot/pull/29)
**Verification:** [Backend CI](https://github.com/harshitethic/PatchPilot/actions/workflows/backend-ci.yml) · [CodeQL Python scanning](https://github.com/harshitethic/PatchPilot/actions/workflows/codeql.yml)

**Problem:** An agent that clones a repository, sends source to an LLM and executes tests must treat repository URLs, symlinks, model-produced edits and workspace IDs as untrusted. Simple string filtering alone is not sufficient.

**Design decisions:**

- Normalize GitHub HTTPS clone URLs. Reject local file URLs, alternate hosts, credential-bearing URLs, and unexpected path segments.
- Resolve context paths within the repository root and reject symlink escapes.
- Stage model edits in memory, including sequential edits to the same file, and apply only after every operation is validated.
- Add workspace inventory, private-file protection, deletion guards and default dry-run cleanup.
- Restrict browser origins, bound GitHub issue URL inputs to the official API host, and strip sensitive environment values from test subprocesses.
- Preserve a reviewable Git diff and version-controlled evidence of what was tested.

**Evidence:** The backend suite now passes **112 tests**, including 15 HTTP access-control regressions, seven secret-commit prevention tests and six sensitive AI-context/provider-error regressions (remote requests, DNS-rebinding-style Host headers, malicious browser origins, bearer authentication, weak-token fail-closed behavior and protected workspace routes). Python 3.11/3.12 GitHub CI, live Docker isolation and CodeQL scanning all passed for [PR #27](https://github.com/harshitethic/PatchPilot/pull/27), [PR #28](https://github.com/harshitethic/PatchPilot/pull/28), and [PR #29](https://github.com/harshitethic/PatchPilot/pull/29). PR #28 reproduces accidental local Git commits containing unignored `.env` files or recognizable credentials, then refuses them before Git history changes while keeping files and staging for review. PR #29 independently reproduces credential-bearing `.env` and source context reaching a model prompt, excludes those sensitive paths and known signatures, bounds file reads, and prevents raw provider errors from being echoed to API users. The 14 October 2026 post-merge scan reported **zero open CodeQL alerts**; no findings were manually dismissed to produce that result.

**Provider reliability follow-through:** [PR #30](https://github.com/harshitethic/PatchPilot/pull/30) reproduced oversized buffered responses, malformed JSON and unhandled transport failures before implementing a shared bounded transport: 1 MiB outbound UTF-8 JSON, 2 MiB raw response bodies and a 240-second total network deadline. Rejecting compression before decompression prevents an expanded chunk from bypassing the intended bound. The change adds 16 regressions, including real TCP slow-drip/disconnect testing and ASGI → real Git → loopback provider → edit/diff/commit integration. A failed coder response preserves tracked source, and a run without a test command cannot claim its tests passed. [Python 3.11/3.12 CI](https://github.com/harshitethic/PatchPilot/actions/runs/38732100462), [live Docker isolation](https://github.com/harshitethic/PatchPilot/actions/runs/38732100454), and [CodeQL](https://github.com/harshitethic/PatchPilot/actions/runs/38732100589) all passed before merge. [Reproduction commands and limits](https://github.com/harshitethic/PatchPilot/blob/main/docs/model-provider-limits.md) distinguish per-call transfer caps from missing concurrency, cloning-disk and billing quotas.

**Repair privacy follow-through:** [PR #31](https://github.com/harshitethic/PatchPilot/pull/31) reproduced credentials returning through raw Git diffs and failed-test logs even when the source-context filter excluded them. Repair prompts now omit raw diffs and check recognizable diagnostic secrets before tail truncation. Four adversarial scenarios fail on the prior code; all five new tests, including a safe repair, pass with the fix. The full 112-test suite, Docker isolation and CodeQL passed before merge and on merged main. The local patch remains unredacted and arbitrary diagnostic secrets can evade the heuristic.

**Browser correctness:** [PR #32](https://github.com/harshitethic/PatchPilot/pull/32) reproduced an earlier successful run's plan, passing-test label and diff remaining visible during a later request or after its failure. Result fields now clear at request start and on errors, including partial rendering failures. Five real Chromium scenarios verify success, literal HTML-like text, pending state, HTTP errors, disconnects and malformed responses. Browser CI, the existing 112-test backend suite, Docker isolation and Python CodeQL passed on the PR and merged main. [Reproduction and recorded evidence](https://github.com/harshitethic/PatchPilot/blob/main/docs/browser-verification.md) explicitly identify the controlled HTTP fixture: this is frontend verification, not a real-model or Docker demo.

**Explicit limitation:** Repository test commands use a fail-closed, resource-limited Docker runner and the real Linux isolation integration test passes. This is **not independently audited multi-tenant isolation**: Git cloning and backend plumbing still execute on the host, the API now offers one strong shared bearer token and loopback-only default, **not** production multi-user identity or per-workspace permissions; the staged-content guard and model-context filter are **heuristics, not full DLP**, and cannot detect arbitrary or encoded secrets, user-provided tasks or credentials already in history; a clean CodeQL scan is not proof of comprehensive security. See [security issue #23](https://github.com/harshitethic/PatchPilot/issues/23), [HTTP access-control tests and model](https://github.com/harshitethic/PatchPilot/blob/main/docs/api-access-control.md) and [security boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md) and [commit safety trade-offs](https://github.com/harshitethic/PatchPilot/blob/main/docs/commit-safety.md) and [model-context privacy limitations](https://github.com/harshitethic/PatchPilot/blob/main/docs/model-context-privacy.md).

## 3. RepoPilot — importing and understanding untrusted code

**Repository:** [RepoPilot](https://github.com/harshitethic/RepoPilot)
**Change reviews:** [ZIP/Git import boundaries](https://github.com/harshitethic/RepoPilot/pull/6) · [Bounded streaming uploads](https://github.com/harshitethic/RepoPilot/pull/15) · [Safe import lifecycle](https://github.com/harshitethic/RepoPilot/pull/17) · [Sanitized API failures](https://github.com/harshitethic/RepoPilot/pull/18) · [Hardened HTTPS Git imports and collision-safe IDs](https://github.com/harshitethic/RepoPilot/pull/21) · [Local-only API boundary](https://github.com/harshitethic/RepoPilot/pull/23) · [Validated ZIP extraction and collision recovery](https://github.com/harshitethic/RepoPilot/pull/22) · [Session-isolated browser workflow and model health](https://github.com/harshitethic/RepoPilot/pull/25) · [Concurrent import limits](https://github.com/harshitethic/RepoPilot/pull/26)
**Verification:** [Frontend and backend CI](https://github.com/harshitethic/RepoPilot/actions/workflows/ci.yml) · [Python and JavaScript CodeQL](https://github.com/harshitethic/RepoPilot/actions/workflows/codeql.yml) · [HTTP-level demonstration](https://github.com/harshitethic/RepoPilot/blob/main/docs/http-smoke-test.md) · [Real-browser ZIP and delayed-answer isolation evidence](https://github.com/harshitethic/RepoPilot/blob/main/docs/browser-demo.md)

**Problem:** A codebase explorer must ingest archives and Git repositories while minimizing filesystem traversal, unintended file reads, collision-prone temporary files and leakage of internal server errors.

**Engineering work:**

- Add path boundary checks and refuse symlinked indexed files.
- Stream ZIP uploads in bounded chunks into unique private temporary files rather than loading entire archives into memory; enforce archive size limits and clean up failures.
- Validate the entire ZIP directory before touching disk; reject symbolic links, Windows path traversal, duplicate/case-colliding paths and file/directory aliases. Enforce actual streamed-byte quotas, use exclusive file creation and roll back only the current reserved workspace.
- Add repository inventory and an import-count limit, refuse symlinked import directories, and preview stale cleanup before any deletion.
- Reject blank searches, tighten canonical repository URL checks and correct line-count reporting.
- Require credential-free HTTPS GitHub imports, suppress host Git config and credential helpers, and reserve temporary import IDs atomically so a clone failure cannot delete a preexisting workspace.
- Return sanitized HTTP errors while logging internal exceptions server-side.
- Reject non-loopback API clients by default using the actual ASGI peer rather than spoofable forwarding headers. Keep local development working and document same-host reverse proxy risks.
- Repair a JSX error that previously prevented the frontend production build.
- Preserve a structured, truthful Ollama online/offline status instead of treating every nonempty status dictionary as healthy; discard raw model-probe diagnostics.
- Reset all repository-scoped search, question, answer and architecture state when switching imports. Invalidate late async responses so Repo A's results cannot appear in Repo B's UI.
- Exercise two distinct ZIP imports, real FastAPI indexing/search and a deliberately delayed answer through a headless Chromium browser, with a deterministic final LLM stub and a published post-switch screenshot.
- Enforce a default 2 GiB budget for persisted imported repository files, with cross-process import admission and rollback of only the newly reserved workspace when a completed Git clone exceeds capacity.

**Evidence:** The backend suite grew from seven initial import-boundary tests to **60 tests**, including four real ASGI/HTTP smoke tests covering ZIP upload, source indexing and search, repository lifecycle and degraded AI availability, plus five adversarial Git import regressions and ten ZIP path/collision/failure-injection regressions. [PR #19](https://github.com/harshitethic/RepoPilot/pull/19) ensures an optional Ollama outage reports degraded availability without exposing an exception. The expanded backend Python 3.11/3.12/3.13 matrix, frontend production build, and Python/JavaScript CodeQL workflows passed on [PR #22](https://github.com/harshitethic/RepoPilot/pull/22), with [ZIP-specific limitations](https://github.com/harshitethic/RepoPilot/blob/main/docs/zip-ingestion-security.md); a separate real HTTPS GitHub clone on Kali also succeeded, and its reserved temporary directory was cleaned up. See the [import threat model](https://github.com/harshitethic/RepoPilot/blob/main/docs/github-import-security.md).

PR [#25](https://github.com/harshitethic/RepoPilot/pull/25) independently passed Python 3.11–3.13 CI, frontend tests/build, a Playwright real-backend A/B ZIP browser scenario, and Python/JavaScript CodeQL. The [browser walkthrough](https://github.com/harshitethic/RepoPilot/blob/main/docs/browser-demo.md) explains what was real, what was stubbed, and how the late-response regression is reproduced. The model response was controlled, so this is not evidence of model quality or production-grade multitenant isolation.

PR [#26](https://github.com/harshitethic/RepoPilot/pull/26) passed 60 backend tests (including eight new resource-limit regressions), concurrency tests across separate OS processes, the frontend and browser CI, and both CodeQL languages. The [storage-budget analysis](https://github.com/harshitethic/RepoPilot/blob/main/docs/import-storage-budget.md) explicitly distinguishes persistent storage from peak disk usage: the Git clone can temporarily consume more than its budget before it is rolled back. These tests do not prove full resource isolation.

**Limitations:** The unauthenticated API is now loopback-only by default, but this is **not authentication**, sandboxing or safe public/multi-user hosting. Same-host reverse proxies and tunnels can bridge remote clients into loopback. Resource quotas, user authorization and independent security review remain necessary before Internet deployment. Repositories can also contain malicious text targeting the AI prompt; indexed text is not trusted instructions.

## 4. PsychologyOS — preserving learning history through maintenance

**Repository:** [PsychologyOS](https://github.com/harshitethic/PsychologyOS)
**Change reviews:** [Admin credential provisioning](https://github.com/harshitethic/PsychologyOS/pull/12) · [Prisma dependency remediation](https://github.com/harshitethic/PsychologyOS/pull/13) · [Non-destructive curriculum seeding](https://github.com/harshitethic/PsychologyOS/pull/14) · [Revocable admin sessions and HTTP tests](https://github.com/harshitethic/PsychologyOS/pull/15) · [Atomic learning attempts](https://github.com/harshitethic/PsychologyOS/pull/16)

**Problem:** A routine curriculum reseed deleted and recreated questions and flashcards. SQLite foreign-key cascades erased student attempts and flashcard progress. Rebuilt mock-paper membership also changed the meaning of an existing paper. Separately, the Prisma CLI's merge dependency had a recursive-object stack-exhaustion advisory.

**Design:** Match existing questions/cards by complete content and preserve their IDs, including legacy random IDs. Changed content creates a new resource so a past answer is not silently reinterpreted. Topic resource additions commit atomically; mock-paper membership is initialized only when empty and thereafter retained. A failed later topic can be retried without undoing already committed topics.

**Verification:** The actual full seed runs three times against disposable SQLite with synthetic student history. Four scenarios verify repeated-seed preservation, changed/omitted/duplicate content, trigger-injected rollback after a card write, and failed mock-paper initialization/retry. SQLite integrity and foreign-key checks pass. CI also runs six admin provisioning tests, three Prisma dependency regressions, the health check, TypeScript checks and the optimized production build. CI and CodeQL passed on both PR #14 and merged main [`fcb324a`](https://github.com/harshitethic/PsychologyOS/commit/fcb324a3e5aacb46855c9196077d6f60ff4ee299).

**Authentication and transaction follow-through:** Production-handler HTTP tests reproduced malformed admin-cookie signatures returning 500 and cookies remaining valid after password rotation/account deletion. [PR #15](https://github.com/harshitethic/PsychologyOS/pull/15) validates MAC encoding, binds signatures to current account ID/credentials, and atomically arbitrates competing rotations. [PR #16](https://github.com/harshitethic/PsychologyOS/pull/16) rejects malformed answers and commits attempts, mastery, revisions and XP in one transaction. Trigger-injected late failures roll everything back; eight concurrent answers preserve the exact XP total. Independent CI initially exposed SQLite writer contention missed locally. Sharing one production client and one SQLite connection per process resolved it without relaxing deadlines; Node 20 with two CPUs and subsequent CI passed. There are 13 HTTP scenarios (14 Node reports including their parent suite), using real Next.js handlers and disposable seeded SQLite. CI and CodeQL passed on both PR heads and merged main.

**Dependency decision:** The three high-severity audit entries were one transitive dependency chain. A scoped override patches its merge library without forcing a Prisma major/database migration. The cyclic-object regression fails on the old version and passes on the patched version; real Prisma config loading is tested. `npm audit` reports **zero vulnerabilities** at verification on 15 October 2026. Findings were not dismissed to achieve that result. See [compatibility evidence and limits](https://github.com/harshitethic/PsychologyOS/blob/main/docs/prisma-dependency-security.md).

**Trade-offs:** This is an additive loader, not a full content-versioning system. Old and revised questions can both appear in practice; retirement needs a reviewed migration. Transactions cover one topic or paper, not the complete curriculum, and concurrent seeders are not supported. Previously deleted history requires a backup. The Prisma major migration remains separate work. HTTP verification covers production handlers in an isolated local server, not deployment availability. Logout clears the local cookie; there is no per-session revocation store. Retries after a lost successful response lack idempotency, and a single SQLite connection is not distributed admission control. See the [HTTP authentication contract](https://github.com/harshitethic/PsychologyOS/blob/main/docs/http-authentication.md) and [learning transaction limits](https://github.com/harshitethic/PsychologyOS/blob/main/docs/learning-transactions.md). See the [reproduction and recovery boundaries](https://github.com/harshitethic/PsychologyOS/blob/main/docs/curriculum-seeding.md).

## 5. FxSound — diagnosing a platform-specific compilation failure

**Repository:** [FxSound Linux/macOS](https://github.com/harshitethic/fxsound-linux-macos)
**Code review:** [Linux include case fix](https://github.com/harshitethic/fxsound-linux-macos/pull/2)
**CI:** [Linux workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/linux-port.yml) · [macOS workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/macos-port.yml)

**Problem:** The DSP port built on a case-insensitive development filesystem but failed on an Ubuntu Linux runner because upstream code included differently capitalized Windows compatibility headers.

**Approach:** Reproduce the failure using Linux CMake; trace the missing header include; change include capitalization while preserving native Windows-compatible behavior; rerun the complete DSP core build and preset tests.

**Evidence:** The patched core compiled on Kali. The DSP smoke test completed its eight signal-processing modes and the factory-preset audio and round-trip checks passed locally. The updated pull request passed independent Linux (DSP and PipeWire) and macOS build/test workflows before merge. Both main-branch workflows also run on matching source changes.

**Limitations:** A passing DSP unit test does not prove full live PipeWire device routing, GUI interaction or audio latency on every distribution. Native audio ports remain alpha software.

---

## 6. ClonePeek — turning passive-scan isolation into a reusable GitHub Action

**Repository:** [ClonePeek](https://github.com/harshitethic/clonepeek)
**Implementation reviews:** [Git execution isolation #5](https://github.com/harshitethic/clonepeek/pull/5) · [Local shell-reference review #9](https://github.com/harshitethic/clonepeek/pull/9) · [Tracked script-diff correction #10](https://github.com/harshitethic/clonepeek/pull/10) · [Reusable Action #12](https://github.com/harshitethic/clonepeek/pull/12) · [Separate consumer verification #15](https://github.com/harshitethic/clonepeek/pull/15)
**Original engineering write-up:** [The `git diff` that wasn't read-only](https://harshitethic.github.io/clonepeek/articles/git-fsmonitor-passive-scanning.html) — a reproducible account of the subprocess hazard and its security boundaries.

**Evidence:** [v0.5.0 release](https://github.com/harshitethic/clonepeek/releases/tag/v0.5.0) · [Git isolation reproduction](https://github.com/harshitethic/clonepeek/blob/main/docs/GIT-CONFIG-ISOLATION.md) · [Action integration guide](https://github.com/harshitethic/clonepeek/blob/main/docs/GITHUB-ACTION.md) · [Cross-repository smoke proof](https://github.com/harshitethic/clonepeek/blob/main/docs/CROSS-REPO-SMOKE.md)

**Problem:** Inspecting an unfamiliar repository for commands that might run during an npm install, VS Code folder-open event, development-container startup or coding-agent lifecycle should not execute the repository's code. The original `--changed-since` scanner could accidentally invoke a repository-defined Git `core.fsmonitor` helper, violating the tool's passive-scan contract. It could also overlook a risky command inside a local script referenced by an unchanged `package.json`.

**Design and debugging:** Reproduced the Git helper issue in a disposable repository with a marker file; hardened the inherited Git environment, explicitly disabled filesystem monitors and hook paths, external diff, text conversion and unexpected remote helpers, and restricted ref inputs. Added **one-hop read-only** inspection of literal local `.sh` references, with symlink/path-escape checks, 32-reference budget, 128 KiB read and 2,000-line limits. Fixed changed-file mode to notice tracked referenced scripts even when their parent config is unchanged. The tool does not run package managers, shell scripts or agent hooks.

**Delivering the tool:** Shipped a separate, versioned GitHub composite Action with **report-only defaults**, opt-in severity thresholds, reviewed baselines, SARIF/JSON/text outputs, and count-only job summaries. It imports the scanner from the Action checkout rather than code from the consumer repository, and does not need a runtime Python dependency install from the target.

**Verification:** **64 tests** pass; the released main branch passed a six-job Python 3.10/3.13 matrix across Windows, macOS and Ubuntu plus a three-job composite-Action integration matrix. A further actual consumer workflow in **[RepoPilot PR #24](https://github.com/harshitethic/RepoPilot/pull/24)** invoked the immutable ClonePeek release from a *different repository*, using sparse checkouts of two **pinned, real public configuration files**. It verified Git blob identities and detected seven medium Cursor command hooks plus two high YappChat folder-open tasks, with source paths and output counts asserted. The consumer PR's backend/frontend CI (4/4) and CodeQL (2/2) also passed. Neither upstream project's code was executed.

**Limitations and external adoption:** These results are **selected, maintainer-run smoke tests**, not validation by an independent outside developer, field detection accuracy, or evidence of user adoption. The [51-case synthetic evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md) deliberately includes false positives and false negatives and must not be interpreted as real-world malware-detection precision or recall. Dynamic/nested shell execution and many other surfaces remain outside scope; Git is hardened but not fully sandboxed. No scan proves that a repository is safe. [External validation issue #14](https://github.com/harshitethic/clonepeek/issues/14) remains open for genuine feedback.

---

## Verification philosophy

The most useful engineering signal is not a crowded green contribution calendar. It is a **traceable chain of evidence**: reproducible defect, constrained implementation, regression test, passing CI, documented trade-offs, and accepted code review.

This portfolio avoids invented impact or benchmark numbers. Production usage metrics should be included only when supported by logs or an approved public case study.
