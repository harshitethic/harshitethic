<div align="center">
  <img src="https://raw.githubusercontent.com/harshitethic/harshitethic/main/assets/header.svg" width="100%" alt="Harshit Sharma — software engineering portfolio" />

  <h1>Harshit Sharma</h1>
  <strong>Backend systems · AI developer tools · Cross-platform software</strong>

  <p><a href="https://harshitethic.com">Website</a> · <a href="https://www.linkedin.com/in/harshitethic/">LinkedIn</a> · <a href="mailto:contact@harshitethic.com">Email</a> · <a href="https://github.com/harshitethic?tab=repositories">All repositories</a></p>
</div>

I build and test developer tools, backend services and native integrations. My main interests are **correctness under failure**, **safe execution boundaries**, and **reproducible engineering evidence**.

## Start here — three projects worth reviewing

| Project | Engineering problem | Reproduce / inspect |
| --- | --- | --- |
| **[LeaseLedger](https://github.com/harshitethic/LeaseLedger)** · Python, SQLite | Single-host durable jobs with fenced leases, worker crash recovery, idempotency, dead-letter handling and WAL-safe backup. **Not** distributed consensus or exactly-once side effects. | [One-command offline demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md) · [Architecture](https://github.com/harshitethic/LeaseLedger/blob/main/docs/architecture.md) · [Benchmarks and limitations](https://github.com/harshitethic/LeaseLedger/blob/main/docs/workload-benchmarks.md) · [CI](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml) |
| **[PatchPilot](https://github.com/harshitethic/PatchPilot)** · Python, Docker | Local AI-assisted repository edits and reviewable diffs. Model-selected tests run in fail-closed Docker isolation. **Not** audited multi-tenant or unrestricted autonomous execution. | [Preview release](https://github.com/harshitethic/PatchPilot/releases/tag/v0.4.0) · [Execution boundaries](https://github.com/harshitethic/PatchPilot/blob/main/docs/security-boundaries.md) · [Live Docker isolation CI](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml) |
| **[RepoPilot](https://github.com/harshitethic/RepoPilot)** · FastAPI, React, Ollama | Local codebase import, indexing, search and optional LLM context. Limits ZIP/Git work and prevents stale cross-repository UI responses. | [First run, no model needed](https://github.com/harshitethic/RepoPilot/blob/main/docs/first-run.md) · [Real browser verification](https://github.com/harshitethic/RepoPilot/blob/main/docs/browser-demo.md) · [CI and CodeQL](https://github.com/harshitethic/RepoPilot/actions) |

**Engineering evidence:** [Failure analyses, design decisions, regression tests and independent CI](portfolio/engineering-case-studies.md). These are reviewable examples, not claims of external production usage.

## Upstream work — accepted fixes, not PR volume

Examples of changes **merged by external maintainers**:

- [Concord #1144](https://github.com/useconcord/concord/pull/1144): prevent premature object-URL revocation from interrupting downloads; add regression tests.
- [ChurchCRM #10759](https://github.com/ChurchCRM/CRM/pull/10759): fix FrankenPHP missing-route behavior with tests.
- [agent-trace #264](https://github.com/Siddhant-K-code/agent-trace/pull/264): add a read-only activation preflight.

[See live merged external PR history](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic+-user%3Aharshitethic) · [Open PRs awaiting review](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3Aharshitethic+-user%3Aharshitethic). I count **accepted contributions**, not opened PRs, as upstream credibility.

## Additional work

- **[CHAI](https://github.com/harshitethic/CHAI):** experimental Linux desktop agent workspace; [read its workflow contract and limitations](https://github.com/harshitethic/CHAI/blob/main/docs/WORKFLOW.md). Alpha, not equivalent to Codex/Work.
- **[FxSound for Linux/macOS](https://github.com/harshitethic/fxsound-linux-macos):** native audio portability experiments using C++, PipeWire and CoreAudio; alpha.
- **[chatgpt-bot-telegram](https://github.com/harshitethic/chatgpt-bot-telegram):** earlier independently starred/forked bot, maintained with tested abuse guardrails. Stars are interest, not evidence of current production deployments.

## How to evaluate or contribute

A skeptical reviewer should be able to repeat a setup, find the exact tests behind claims, and report where reality differs from the README. Each flagship accepts reproducible bug reports and focused fixes. See the [independent evaluation and feedback guide](portfolio/independent-evaluation.md) for scoped review requests, success criteria and a no-fabrication evidence log.

## Security-focused developer tooling

**[ClonePeek](https://harshitethic.github.io/clonepeek/)** provides a
standard-library-only, offline scanner to inventory execution-capable
repository configuration and a
[reusable GitHub Action](https://github.com/harshitethic/clonepeek/blob/main/docs/GITHUB-ACTION.md)
for PR checks. It reports *trigger → command → file/line → review action*
without running untrusted repository scripts. The scanner also examines
bounded first-hop local shell-script references and hardened Git diff
inspection, with explicit gaps for dynamic or transitive execution.

The [v0.5.1 release](https://github.com/harshitethic/clonepeek/releases/tag/v0.5.1)
is published as a [free GitHub Marketplace Action](https://github.com/marketplace/actions/clonepeek-passive-repository-execution-audit).
The current main branch has **81 Python tests** and passing CI across
Windows, Linux and macOS, including reusable-action integration tests.
Watch a [34-second replay of real CLI output](https://harshitethic.github.io/clonepeek/#video-demo)
from the versioned synthetic fixture; this isn't a live user scan.
Its
[51-case synthetic evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md)
is deliberately labeled as *non-representative*; findings are heuristic
review prompts, **not malware verdicts or proof of repository safety**.

The [verified separate-repository consumer workflow](https://github.com/harshitethic/RepoPilot/actions/runs/38728091966) also exercised the released GitHub Action against two immutable public config snapshots: seven Cursor hooks and two VS Code folder-open tasks. [See the engineering case study](portfolio/engineering-case-studies.md) and [reproduction details](https://github.com/harshitethic/clonepeek/blob/main/docs/CROSS-REPO-SMOKE.md). This does not imply independent external adoption.

## Contact

For source reviews, collaborations or engineering roles: **[website](https://harshitethic.com)** · **[LinkedIn](https://www.linkedin.com/in/harshitethic/)** · **[email](mailto:contact@harshitethic.com)**.

<sub>Public evidence over vanity metrics. Limitations and failed experiments belong next to the working examples.</sub>
