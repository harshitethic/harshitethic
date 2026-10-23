# Independent evaluation and feedback guide

Updated **23 October 2026**. This is an invitation to *test claims*, not an assertion of adoption, a certification, a security audit, or an application for artificial stars.

## Which project should I review?

| Time | Project | Reproducible test | Good feedback |
| --- | --- | --- | --- |
| 5–10 min | [LeaseLedger](https://github.com/harshitethic/LeaseLedger) | Python 3.11+; in a clean checkout run `python3 -m examples.recovery_walkthrough`, then `python3 -m unittest discover -s tests -v`. No model/API credentials needed. | Can an expired worker acknowledge a reclaimed lease? Can a WAL backup be verified? What does the single-host scope exclude? |
| 15–30 min | [RepoPilot](https://github.com/harshitethic/RepoPilot) | Follow the [first-run guide](https://github.com/harshitethic/RepoPilot/blob/main/docs/first-run.md); import a disposable ZIP and search a known line **without Ollama**. | Does ZIP import fail safely? Are error states understandable? Can another repository's delayed results leak into the UI? |
| 30–60 min | [PatchPilot](https://github.com/harshitethic/PatchPilot) | Follow the [local setup](https://github.com/harshitethic/PatchPilot#-quick-start--macos--apple-silicon) and [Docker isolation workflow](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml); use only a disposable test repository. | Does the agent fail closed without Docker? Does a failed test leave a reviewable diff? Is any host capability unexpectedly exposed? |

**Safety:** Never use production credentials, private customer code, confidential datasets or sensitive repositories for evaluation. PatchPilot is a local developer tool, not an independently audited multi-tenant service. RepoPilot local APIs must not be made public. LeaseLedger is at-least-once on one host, not exactly-once across services.

## What counts as *external* feedback?

A report is independently verifiable when it comes from a person other than the repository maintainer or automated assistant and includes:

1. Public issue or PR URL, or a consented anonymized issue summary.
2. Environment (OS, version, commit/release), minimal reproduction and expected/actual behavior.
3. Maintainer response, regression test or design decision, and a link to the resulting change.
4. Verification outcome (*confirmed*, *not reproducible*, *out of scope*), not just a positive testimonial.

Feedback by bots or the maintainer is **not** an independent user or review. Star counts and forks indicate interest, not successful installation. An external PR is **not** an accepted contribution until merged.

## Reviewer prompts and checkpoints

### LeaseLedger: correctness under contention

- Run the recovery demo and compare [checked output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json). Report any divergence, including Python and SQLite versions.
- Examine [fencing design](https://github.com/harshitethic/LeaseLedger/blob/main/docs/architecture.md) and adversarial [lease-starvation analysis](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/expired-lease-cleanup-progress.md).
- Run the [repeated benchmark](https://github.com/harshitethic/LeaseLedger/blob/main/docs/workload-benchmarks.md) with its stated configuration; report all raw trials, machine/OS, scheduling variability and failures. Do **not** compare different hardware as equivalent or turn no-op throughput into production capacity.

### RepoPilot: isolation and onboarding

- Use two synthetic repositories with distinguishable file names; rapidly switch while a delayed response is outstanding.
- Inspect [ZIP threat model](https://github.com/harshitethic/RepoPilot/blob/main/docs/zip-ingestion-security.md), [HTTP upload admission](https://github.com/harshitethic/RepoPilot/blob/main/docs/request-body-admission.md), and [browser scenario](https://github.com/harshitethic/RepoPilot/blob/main/docs/browser-demo.md).
- Document first-run failures from clean Windows ZIP-only, macOS and Linux setups. Distinguish untested platforms.

### PatchPilot: security and UX

- Check [trust boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md), [model context privacy](https://github.com/harshitethic/PatchPilot/blob/main/docs/model-context-privacy.md), and [HTTP access controls](https://github.com/harshitethic/PatchPilot/blob/main/docs/api-access-control.md).
- Try harmless adversarial instructions in a synthetic fixture (never real secrets). Confirm untrusted repository content cannot bypass required Docker test isolation.
- Test installation with Docker unavailable. A failure must be clear and must **not** fall back to host execution.

## Public evidence register

This register deliberately starts without fabricated reviewers or customer counts. Add entries **only after verification**:

| Date | Project | Independent source | Reproduction | Fix / outcome |
| --- | --- | --- | --- | --- |
| — | — | No independently verified review logged in this register yet | — | — |

## Ten-part portfolio improvement contract

| Area | Objective | Honest evidence of completion |
| --- | --- | --- |
| Adoption | 10 independent developers | Ten verifiable install/use reports; **not yet claimed** |
| PR backlog | Close duplicates, follow up on review | Upstream PR links and maintainer responses, not a raw count |
| Flagships | Maintain three reliable projects | Release builds, test runs and reproducible demos |
| Profile | Make engineering evidence scannable | A short, link-backed profile README |
| Videos | Three real software recordings | Video captures of unmocked actions, explicitly labelling fixtures |
| Benchmarks | Repeated, comparable performance study | Commands, full trial data, machine notes and limitations |
| Reviews | Three independent engineering reviews | External comments/diffs with author identity and responses |
| Releases | Clean install and release contract | Versioned artifacts, CI, license, change logs, known limitations |
| Case studies | Three verified technical explanations | Problem, reproduction, alternatives, implementation, results |
| Discovery | Real users, organic interest | External issue links, honest release notes and relevant discussions |

**How to submit:** Open a focused issue in the relevant project; include the environment, exact command, expected result, observed result, sanitized logs, and consent before quoting your feedback. No paid/staged endorsements, exchange-star schemes or unsolicited mass mentions.
