# Engineering case studies

A selection of technical work with **links to source, regression tests and CI**. These notes cover the concrete engineering decisions behind the projects, including their current limitations. They are intended to be checked against the public repositories rather than taken on faith.

Updated: 14 October 2026.

## 1. LeaseLedger — explicit correctness contracts for durable work

**Repository:** [LeaseLedger](https://github.com/harshitethic/LeaseLedger)
**Evidence:** [Live executable demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md) · [Machine-checked output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json) · [CI matrix](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml) · [Release v0.1.2](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.2) · [100-expired-leases bug reproduction](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/expired-lease-cleanup-progress.md) · [Fencing-token failure analysis](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/why-fencing-tokens.md) · [WAL-safe recovery runbook](https://github.com/harshitethic/LeaseLedger/blob/main/docs/backup-and-recovery.md)

**Problem:** Naive job processing loses work when a worker crashes and allows a
paused worker to acknowledge a job after its lease has been reassigned.

**Design:** SQLite WAL for durability, `BEGIN IMMEDIATE` for atomic multi-process
claims, monotonic fencing tokens, deadline-validated acknowledgements, worker
heartbeats, idempotent submissions, bounded retries and dead-letter records.
Every transition writes a durable audit event in the same transaction.

**Verification:** Thirty-four automated tests passed on Python 3.11, 3.12 and
3.13, including four real processes competing for 48 jobs, an abrupt worker
process termination followed by fenced recovery, and concurrent online backups.
A separate deterministic reference model covers 640 seeded operations, while
a regression creates 121 expired high-priority leases and proves a ready job
behind them is still claimed in one call. The bug is fixed in v0.1.2.
SQLite snapshots are verified for page and foreign-key integrity and refuse
overwriting existing files. A working single-command walkthrough reproduces
the observable queue lifecycle, and its actual stdout JSON is versioned and
compared in CI on three Python versions. Ruff, packaging and benchmark-smoke CI also pass.

**Trade-off:** This is a **single-host, at-least-once** queue. It is not
distributed consensus, exactly-once external processing or a verified
production-scale benchmark. Handler code is trusted local Python.

---

## 2. PatchPilot — reducing the attack surface of an AI coding agent

**Repository:** [PatchPilot](https://github.com/harshitethic/PatchPilot)
**Change reviews:** [Repository trust boundaries](https://github.com/harshitethic/PatchPilot/pull/13) · [Safe workspace lifecycle](https://github.com/harshitethic/PatchPilot/pull/19) · [Docker test isolation](https://github.com/harshitethic/PatchPilot/pull/24) · [Host Git-only execution and private logs](https://github.com/harshitethic/PatchPilot/pull/25) · [Prevent hostile Git hooks and internal control-file edits](https://github.com/harshitethic/PatchPilot/pull/26)
**Verification:** [Backend CI](https://github.com/harshitethic/PatchPilot/actions/workflows/backend-ci.yml) · [CodeQL Python scanning](https://github.com/harshitethic/PatchPilot/actions/workflows/codeql.yml)

**Problem:** An agent that clones a repository, sends source to an LLM and executes tests must treat repository URLs, symlinks, model-produced edits and workspace IDs as untrusted. Simple string filtering alone is not sufficient.

**Design decisions:**

- Normalize GitHub HTTPS clone URLs. Reject local file URLs, alternate hosts, credential-bearing URLs, and unexpected path segments.
- Resolve context paths within the repository root and reject symlink escapes.
- Stage model edits in memory, including sequential edits to the same file, and apply only after every operation is validated.
- Add workspace inventory, private-file protection, deletion guards and default dry-run cleanup.
- Restrict browser origins, bound GitHub issue URL inputs to the official API host, and strip sensitive environment values from test subprocesses.
- Preserve a reviewable Git diff and version-controlled evidence of what was tested.

**Evidence:** The extended backend suite passed **63 tests**, including an adversarial Git-hook integration test, in the Python 3.11/3.12 GitHub Actions matrix. The live Docker isolation workflow and CodeQL analysis also pass. The 14 October 2026 post-merge scan reported **zero open CodeQL alerts**; no findings were manually dismissed to produce that result.

**Explicit limitation:** Repository test commands use a fail-closed, resource-limited Docker runner and the real Linux isolation integration test passes. This is **not independently audited multi-tenant isolation**: Git cloning and backend plumbing still execute on the host, the API lacks public-service authentication, and a clean CodeQL scan is not proof of comprehensive security. See [security issue #23](https://github.com/harshitethic/PatchPilot/issues/23) and [security boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md).

## 3. RepoPilot — importing and understanding untrusted code

**Repository:** [RepoPilot](https://github.com/harshitethic/RepoPilot)
**Change reviews:** [ZIP/Git import boundaries](https://github.com/harshitethic/RepoPilot/pull/6) · [Bounded streaming uploads](https://github.com/harshitethic/RepoPilot/pull/15) · [Safe import lifecycle](https://github.com/harshitethic/RepoPilot/pull/17) · [Sanitized API failures](https://github.com/harshitethic/RepoPilot/pull/18) · [Hardened HTTPS Git imports and collision-safe IDs](https://github.com/harshitethic/RepoPilot/pull/21)
**Verification:** [Frontend and backend CI](https://github.com/harshitethic/RepoPilot/actions/workflows/ci.yml) · [Python and JavaScript CodeQL](https://github.com/harshitethic/RepoPilot/actions/workflows/codeql.yml) · [HTTP-level demonstration](https://github.com/harshitethic/RepoPilot/blob/main/docs/http-smoke-test.md)

**Problem:** A codebase explorer must ingest archives and Git repositories while minimizing filesystem traversal, unintended file reads, collision-prone temporary files and leakage of internal server errors.

**Engineering work:**

- Add path boundary checks and refuse symlinked indexed files.
- Stream ZIP uploads in bounded chunks into unique private temporary files rather than loading entire archives into memory; enforce archive size limits and clean up failures.
- Add repository inventory and an import-count limit, refuse symlinked import directories, and preview stale cleanup before any deletion.
- Reject blank searches, tighten canonical repository URL checks and correct line-count reporting.
- Require credential-free HTTPS GitHub imports, suppress host Git config and credential helpers, and reserve temporary import IDs atomically so a clone failure cannot delete a preexisting workspace.
- Return sanitized HTTP errors while logging internal exceptions server-side.
- Repair a JSX error that previously prevented the frontend production build.

**Evidence:** The backend suite grew from seven initial import-boundary tests to **35 tests**, including four real ASGI/HTTP smoke tests covering ZIP upload, source indexing and search, repository lifecycle and degraded AI availability, plus five adversarial Git import regressions. [PR #19](https://github.com/harshitethic/RepoPilot/pull/19) ensures an optional Ollama outage reports degraded availability without exposing an exception. The backend/frontend CI and Python/JavaScript CodeQL workflows passed on [PR #21](https://github.com/harshitethic/RepoPilot/pull/21); a separate real HTTPS GitHub clone on Kali also succeeded, and its reserved temporary directory was cleaned up. See the [import threat model](https://github.com/harshitethic/RepoPilot/blob/main/docs/github-import-security.md).

**Limitations:** Resource quotas, sandboxing and authentication are required before offering untrusted ZIP analysis publicly. Repositories can also contain malicious text targeting the AI prompt; indexed text is not trusted instructions.

## 4. PsychologyOS — rescuing a failing full-stack CI pipeline

**Repository:** [PsychologyOS](https://github.com/harshitethic/PsychologyOS)
**Change reviews:** [TypeScript/CI repair](https://github.com/harshitethic/PsychologyOS/pull/4) · [Patched PostCSS dependency](https://github.com/harshitethic/PsychologyOS/pull/5) · [Safer admin credential provisioning](https://github.com/harshitethic/PsychologyOS/pull/12)
**Verification:** [GitHub Actions CI](https://github.com/harshitethic/PsychologyOS/actions/workflows/ci.yml) · [TypeScript CodeQL](https://github.com/harshitethic/PsychologyOS/actions/workflows/codeql.yml)

**Problem:** The full-stack education project was failing TypeScript checks in the admin password route, profile year validation and curriculum seed types. The health smoke-test runner also used a module-incompatible top-level await.

**Approach:**

- Repair the admin account lookup to use the configured username instead of a boolean session check.
- Validate nullable profile year input and make curriculum data structures accurately typed.
- Remove duplicate curriculum mapping keys.
- Wrap the health test in a valid asynchronous entry point.
- Apply compatible lockfile updates and a narrow PostCSS override instead of forcing a framework/database major upgrade.
- Remove shared admin default passwords and predictable session signing secrets, use private atomic credential-file provisioning, and avoid printing credential material.

**Evidence:** GitHub Actions passes TypeScript checks, health tests and admin setup tests; the extra six credential regressions validate hashed storage, permissions and refusal of symlinks. The optimized Next.js production build was verified separately. The first three CodeQL findings from insecure local setup scripts have been resolved on `main`. npm audit advisories dropped from seven to three, remaining in Prisma's dependency chain.

**Limitations:** The three remaining security advisories require a Prisma compatibility and deployment test plan. Do not assume a passing TypeScript check proves every production database operation works.

## 5. FxSound — diagnosing a platform-specific compilation failure

**Repository:** [FxSound Linux/macOS](https://github.com/harshitethic/fxsound-linux-macos)
**Code review:** [Linux include case fix](https://github.com/harshitethic/fxsound-linux-macos/pull/2)
**CI:** [Linux workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/linux-port.yml) · [macOS workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/macos-port.yml)

**Problem:** The DSP port built on a case-insensitive development filesystem but failed on an Ubuntu Linux runner because upstream code included differently capitalized Windows compatibility headers.

**Approach:** Reproduce the failure using Linux CMake; trace the missing header include; change include capitalization while preserving native Windows-compatible behavior; rerun the complete DSP core build and preset tests.

**Evidence:** The patched core compiled on Kali. The DSP smoke test completed its eight signal-processing modes and the factory-preset audio and round-trip checks passed locally. The updated pull request passed independent Linux (DSP and PipeWire) and macOS build/test workflows before merge. Both main-branch workflows also run on matching source changes.

**Limitations:** A passing DSP unit test does not prove full live PipeWire device routing, GUI interaction or audio latency on every distribution. Native audio ports remain alpha software.

---

## 6. ClonePeek — reproducible passive-scan trust-boundary repair

**Repository:** [ClonePeek](https://github.com/harshitethic/clonepeek)
**Code review:** [Git filesystem-monitor execution hardening](https://github.com/harshitethic/clonepeek/pull/5)
**Evidence:** [Cross-platform CI](https://github.com/harshitethic/clonepeek/actions/workflows/ci.yml) · [v0.2.2 release](https://github.com/harshitethic/clonepeek/releases/tag/v0.2.2) · [Git helper execution reproduction](https://github.com/harshitethic/clonepeek/blob/main/docs/GIT-CONFIG-ISOLATION.md) · [Labeled synthetic evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md)

**Problem:** An offline scanner that classifies execution-capable repository
configuration should not execute repository-defined code itself. In the
original changed-file implementation, Git's local core.fsmonitor config
could dispatch an executable helper during a name-only diff.

**Reproduction and mitigation:** A disposable repo configured with an
executable filesystem monitor produced an unexpected EXECUTED marker on
two original scanner invocations. The fixed path filters inherited Git
environment overrides, ignores global/system config, explicitly disables
filesystem monitors, hooks, external diffs and text conversion, and keeps
strict argument/ref validation.

**Verification:** The 34-test suite includes the Git helper execution
regression and a Windows PowerShell expression-style fetch-and-execute
regression that failed before the fix. All 12 PR CI checks passed across
two runs of six OS/Python combinations (Ubuntu, Windows, macOS; Python
3.10 and 3.13). A versioned 46-case hand-authored fixture corpus
records high-risk TP=15, FP=3, FN=2, TN=26 and per-rule surface-detection
counts, reproducible with no live malicious scripts.

**Limitations:** ClonePeek invokes an installed Git binary, which is not
fully sandboxed. The corpus is purposely curated around the rules and
contains misleading benign folder-open alerts and missed indirect scripts.
The reported scores describe **only these fixtures**; they are not a
representative real-world malware-detection estimate.

---

## Verification philosophy

The most useful engineering signal is not a crowded green contribution calendar. It is a **traceable chain of evidence**: reproducible defect, constrained implementation, regression test, passing CI, documented trade-offs, and accepted code review.

This portfolio avoids invented impact or benchmark numbers. Production usage metrics should be included only when supported by logs or an approved public case study.
