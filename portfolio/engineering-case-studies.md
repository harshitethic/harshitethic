# Engineering case studies

A selection of technical work with **links to source, regression tests and CI**. These notes cover the concrete engineering decisions behind the projects, including their current limitations. They are intended to be checked against the public repositories rather than taken on faith.

Updated: 13 October 2026.

## 1. PatchPilot — reducing the attack surface of an AI coding agent

**Repository:** [PatchPilot](https://github.com/harshitethic/PatchPilot)
**Change review:** [Repository trust boundary hardening](https://github.com/harshitethic/PatchPilot/pull/13)
**Verification:** [Backend CI](https://github.com/harshitethic/PatchPilot/actions/workflows/backend-ci.yml)

**Problem:** An agent that clones a repository, sends source to an LLM and executes tests must treat repository URLs, symlinks, model-produced edits and workspace IDs as untrusted. Simple string filtering alone is not sufficient.

**Design decisions:**

- Normalize GitHub HTTPS clone URLs. Reject local file URLs, alternate hosts, credential-bearing URLs, and unexpected path segments.
- Resolve context paths within the repository root and reject symlink escapes.
- Stage and validate model edits before applying them; reject duplicate edits that would otherwise overwrite a prior change.
- Run generated test commands through a restricted parser instead of a shell.
- Preserve a human-readable Git diff as the main review artifact.

**Evidence:** The hardening change adds seven adversarial regression tests. The full backend suite passed 32 tests locally; GitHub Actions validated it on Python 3.11 and 3.12.

**Explicit limitation:** A repository's own test scripts can execute arbitrary code despite command-name restrictions. PatchPilot is a local development tool; true untrusted workloads require containers or microVMs, bounded resources and network isolation. See [security boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md).

## 2. RepoPilot — importing and understanding untrusted code

**Repository:** [RepoPilot](https://github.com/harshitethic/RepoPilot)
**Change review:** [ZIP/Git import hardening and frontend fix](https://github.com/harshitethic/RepoPilot/pull/6)
**Verification:** [Frontend and backend CI](https://github.com/harshitethic/RepoPilot/actions/workflows/ci.yml)

**Problem:** A codebase explorer must ingest archives and Git repositories while minimizing filesystem traversal, unintended file reads, collision-prone temporary files and leakage of internal server errors.

**Engineering work:**

- Add path boundary checks and refuse symlinked indexed files.
- Use a randomly created temporary file for ZIP uploads rather than a predictable user-derived path.
- Reject blank searches, tighten canonical repository URL checks and correct line-count reporting.
- Add seven network-free regression tests, including ZIP-slip and symlink cases.
- Repair an existing React JSX error that prevented Vite from building.

**Evidence:** The seven new tests passed on macOS and Kali; both GitHub Actions jobs passed on the merged PR.

**Limitations:** Resource quotas, sandboxing and authentication are required before offering untrusted ZIP analysis publicly. Repositories can also contain malicious text targeting the AI prompt; indexed text is not trusted instructions.

## 3. PsychologyOS — rescuing a failing full-stack CI pipeline

**Repository:** [PsychologyOS](https://github.com/harshitethic/PsychologyOS)
**Change reviews:** [TypeScript and CI repair](https://github.com/harshitethic/PsychologyOS/pull/4) · [Patched PostCSS dependency](https://github.com/harshitethic/PsychologyOS/pull/5)
**Verification:** [GitHub Actions CI](https://github.com/harshitethic/PsychologyOS/actions/workflows/ci.yml)

**Problem:** The full-stack education project was failing TypeScript checks in the admin password route, profile year validation and curriculum seed types. The health smoke-test runner also used a module-incompatible top-level await.

**Approach:**

- Repair the admin account lookup to use the configured username instead of a boolean session check.
- Validate nullable profile year input and make curriculum data structures accurately typed.
- Remove duplicate curriculum mapping keys.
- Wrap the health test in a valid asynchronous entry point.
- Apply compatible lockfile updates and a narrow PostCSS override instead of forcing a framework/database major upgrade.

**Evidence:** GitHub Actions now passes on main for type checking, project health verification and the doctor checks. The npm audit findings were reduced from seven to three; the remaining reports involve Prisma and its dependency chain.

**Limitations:** The three remaining security advisories require a Prisma compatibility and deployment test plan. Do not assume a passing TypeScript check proves every production database operation works.

## 4. FxSound — diagnosing a platform-specific compilation failure

**Repository:** [FxSound Linux/macOS](https://github.com/harshitethic/fxsound-linux-macos)
**Code review:** [Linux include case fix](https://github.com/harshitethic/fxsound-linux-macos/pull/2)
**CI:** [Linux workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/linux-port.yml) · [macOS workflow](https://github.com/harshitethic/fxsound-linux-macos/actions/workflows/macos-port.yml)

**Problem:** The DSP port built on a case-insensitive development filesystem but failed on an Ubuntu Linux runner because upstream code included differently capitalized Windows compatibility headers.

**Approach:** Reproduce the failure using Linux CMake; trace the missing header include; change include capitalization while preserving native Windows-compatible behavior; rerun the complete DSP core build and preset tests.

**Evidence:** The patched core compiled on Kali. The DSP smoke test completed its eight signal-processing modes and the factory-preset audio and round-trip checks passed locally. Independent CI for this PR is the final authority for cross-platform behavior.

**Limitations:** A passing DSP unit test does not prove full live PipeWire device routing, GUI interaction or audio latency on every distribution. Native audio ports remain alpha software.

---

## Verification philosophy

The most useful engineering signal is not a crowded green contribution calendar. It is a **traceable chain of evidence**: reproducible defect, constrained implementation, regression test, passing CI, documented trade-offs, and accepted code review.

This portfolio avoids invented impact or benchmark numbers. Production usage metrics should be included only when supported by logs or an approved public case study.
