<div align="center">
  <img src="https://raw.githubusercontent.com/harshitethic/harshitethic/main/assets/header.svg" width="100%" alt="Harshit Sharma — software engineering portfolio" />

  <h1>Harshit Sharma</h1>
  <strong>Software engineer · AI developer tools · Backend systems · Cross-platform software</strong>

  <p>
    <a href="https://harshitethic.com">Website</a> ·
    <a href="https://www.linkedin.com/in/harshitethic/">LinkedIn</a> ·
    <a href="mailto:contact@harshitethic.com">Email</a> ·
    <a href="https://github.com/harshitethic?tab=repositories">Repositories</a>
  </p>
</div>

I build software across **AI tooling, APIs, full-stack applications, and native systems**. My work spans shipping interfaces and backend services, integrating local language models, debugging production environments, and contributing fixes to other teams' open-source projects.

**What I optimize for:** reproducible setup, observable behavior, clear failure handling, tests that catch regressions, and code that another engineer can review and maintain.

## Engineering spotlight: reliable background work

**[LeaseLedger](https://github.com/harshitethic/LeaseLedger)** is an original,
single-host **durable job queue** built with Python and SQLite WAL. It tackles
real backend consistency problems: fencing stale workers, recovering crashed
leases, idempotent producer requests, transactional audit events, bounded retries
and dead-letter jobs. Four independent processes compete for work in its
integration tests, and a killed worker's lease can be reclaimed safely.
All **54 tests pass** across Python 3.11–3.13 in CI (40 queue, eight publication and six benchmark tests). A
[one-command offline demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md)
also proves stale-ACK rejection and backup recovery using a real SQLite database.
Version [0.1.3](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.3) was published by a workflow gated on tests, packaging, benchmark smoke, lint and CodeQL.
The [writer-contention fix](https://github.com/harshitethic/LeaseLedger/pull/5) rejects leases that expire while waiting for SQLite, with six regressions and verified Kali/macOS runs.
A [60-trial workload study](https://github.com/harshitethic/LeaseLedger/blob/main/docs/workload-benchmarks.md) records 18,000 completed jobs, 1,800 retries, operation p95/p99s, worker contention and actual handler delays across Kali and macOS. It preserves all trials and documents a large scheduling discrepancy instead of claiming production capacity.
Version 0.1.2 adds seeded fault-injection tests and fixes a verified queue-starvation bug
where 100+ exhausted leases concealed runnable jobs. Version 0.1.1
introduced online WAL-safe backups and integrity verification.

[Run the verified offline demo](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md)
· [View its machine-checked JSON output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json)
· [Read the architecture](https://github.com/harshitethic/LeaseLedger/blob/main/docs/architecture.md)
· [Why fencing tokens matter](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/why-fencing-tokens.md)
· [See verified CI](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml)
· [v0.1.3 release](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.3)
· [Reproduced claim starvation and fix](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/expired-lease-cleanup-progress.md)
· [Online backup and recovery](https://github.com/harshitethic/LeaseLedger/blob/main/docs/backup-and-recovery.md)

*Scope is explicit: at-least-once processing on a single host, not exactly-once
external effects or a multi-region distributed queue.*

## Selected engineering work

<table>
<tr>
<td width="50%" valign="top">
<h3><a href="https://github.com/harshitethic/PatchPilot">PatchPilot</a></h3>
<p><strong>Local-first AI developer agent · Python · Git</strong></p>
<p>Takes a repository task through code inspection, change planning, edits in a separate local workspace, test execution, and reviewable Git diffs.</p>
<p><strong>Engineering focus:</strong> fail-closed Docker test isolation, loopback-only API with optional bearer authentication, protected workspace operations, staged-secret commit refusal, filtered model context, bounded model-provider transfers, 112 backend tests, five real Chromium scenarios for result/error state, and <a href="https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml">live isolation CI</a>.</p>
<p><a href="https://github.com/harshitethic/PatchPilot#readme">Source and architecture →</a> · <a href="https://github.com/harshitethic/PatchPilot/blob/main/docs/api-access-control.md">HTTP security model →</a> · <a href="https://github.com/harshitethic/PatchPilot/blob/main/docs/commit-safety.md">Commit safety and limits →</a> · <a href="https://github.com/harshitethic/PatchPilot/blob/main/docs/model-context-privacy.md">AI context privacy →</a> · <a href="https://github.com/harshitethic/PatchPilot/blob/main/docs/model-provider-limits.md">Provider limits and integration tests →</a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/harshitethic/fxsound-linux-macos">FxSound: Linux and macOS</a></h3>
<p><strong>Native audio integration · C++ · PipeWire · CoreAudio</strong></p>
<p>Unofficial community ports retaining the upstream DfxDsp processing engine while adapting audio transport to Linux and macOS.</p>
<p><strong>Engineering focus:</strong> platform boundaries, native builds, audio processing, installer workflows, and <a href="https://github.com/harshitethic/fxsound-linux-macos/actions">platform CI</a>.</p>
<p><strong>Status:</strong> alpha software; see the README for platform-specific limitations.</p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<h3><a href="https://harshitethic.github.io/clonepeek/">ClonePeek — live demo ↗</a></h3>
<p><strong>Offline repository security review · Python · GitHub Actions</strong></p>
<p>Inventories known first-run execution hooks in unfamiliar repositories—npm lifecycle scripts, VS Code tasks, devcontainers, Cursor and Claude Code hooks, and local MCP launch commands—without executing repository code.</p>
<p><strong>Engineering focus:</strong> bounded, passive reads, symlink protections, SARIF reporting, reviewed baselines, 64 automated tests, and an <a href="https://github.com/harshitethic/clonepeek/actions/workflows/composite-action.yml">actual reusable-action CI matrix</a> on Linux, macOS, and Windows.</p>
<p><a href="https://github.com/harshitethic/clonepeek/releases/tag/v0.5.0">v0.5.0 release →</a> · <a href="https://github.com/harshitethic/clonepeek/blob/main/docs/GITHUB-ACTION.md">GitHub Action quick start →</a> · <a href="https://github.com/harshitethic/clonepeek/blob/main/docs/THREAT_MODEL.md">Threat model →</a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/harshitethic/RepoPilot">RepoPilot</a></h3>
<p><strong>Local codebase exploration · Python · FastAPI · React · Ollama</strong></p>
<p>Clones or imports repositories, indexes source, exposes file trees and code search, and supplies relevant context to a local language model for questions about the code.</p>
<p><strong>Engineering focus:</strong> validated and bounded ZIP extraction, atomic import reservations, credential-free HTTPS Git cloning, a local-only API security boundary, <strong>45+ backend tests</strong>, Python 3.11–3.13 and <a href="https://github.com/harshitethic/RepoPilot/actions/workflows/ci.yml">frontend/backend CI</a>.</p>
<p><a href="https://github.com/harshitethic/RepoPilot">Source →</a> · <a href="https://github.com/harshitethic/RepoPilot/blob/main/docs/http-smoke-test.md">Reproducible HTTP walkthrough →</a> · <a href="https://github.com/harshitethic/RepoPilot/blob/main/docs/github-import-security.md">Import security model →</a> · <a href="https://github.com/harshitethic/RepoPilot/blob/main/docs/local-api-boundary.md">Local-only API threat model →</a> · <a href="https://github.com/harshitethic/RepoPilot/blob/main/docs/zip-ingestion-security.md">ZIP threat model →</a></p>
</td>
</tr>
</table>

## How I work — engineering evidence

Alongside source code, I maintain [engineering case studies](portfolio/engineering-case-studies.md) showing the problems, design decisions, tests and trade-offs behind my work: **lease fencing, agent isolation, ZIP/Git import boundaries, SQLite data preservation, full-stack CI recovery, and native Linux/macOS portability**. Each case links to verifiable PRs and CI results.

**Recent reliability work:** [PsychologyOS PR #15](https://github.com/harshitethic/PsychologyOS/pull/15) binds admin cookies to current account credentials and revokes them on password rotation/deletion. [PR #16](https://github.com/harshitethic/PsychologyOS/pull/16) makes quiz/exam writes atomic and verifies rollback plus concurrent XP accounting through 13 real HTTP scenarios. Both passed CI and CodeQL. In [PR #14](https://github.com/harshitethic/PsychologyOS/pull/14), I reproduced a curriculum reseed erasing student history, preserved legacy resource IDs, and added real SQLite rollback/retry tests. CI now verifies the production build. [PR #13](https://github.com/harshitethic/PsychologyOS/pull/13) also resolved the remaining dependency audit findings with a scoped, regression-tested patch. [Read the design and limitations](https://github.com/harshitethic/PsychologyOS/blob/main/docs/curriculum-seeding.md).

## Open-source contributions

As of **15 October 2026**, I have **25 merged pull requests across 9 repositories owned by other developers/organizations**. These include bug fixes, tests, developer tooling, and documentation. Browse the [merged PR history](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic+-user%3Aharshitethic).

| Project | Accepted work |
| --- | --- |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | 9 merged PRs involving data validation, artifact handling, tests, and examples |
| [Internet Archive / Open Library](https://github.com/internetarchive/openlibrary/pull/13854) | Corrected out-of-date developer documentation |
| [ChurchCRM](https://github.com/ChurchCRM/CRM/pull/10431) | Fixed floating controls overlapping modal dialogs |
| [StaveIndustries / woo-pay](https://github.com/StaveIndustries/woo-pay/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | Improved WooCommerce error reporting and payment-failure persistence |
| [pranjalparmar/fastdocparse](https://github.com/pranjalparmar/fastdocparse/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | Simplified CLI errors and grounding logic |

*PR acceptance and code review are more informative than a raw count of opened PRs. Current status and diffs are available via the links above.*

**Recent maintainer review follow-through:** On [ChurchCRM PR #10484](https://github.com/ChurchCRM/CRM/pull/10484), I corrected the translation-extraction configuration in response to maintainer feedback, verified that the requested string appeared in the generated catalog without committing it, and passed lint plus independent security checks. **The PR was merged on 14 October 2026** and is included in the verified merged-contribution count.

**Ongoing review:** [Poetry PR #11135](https://github.com/python-poetry/poetry/pull/11135) now preserves PATH executable aliases when source directories share their names, following a reviewer's reproduction. The follow-up passed 97 local environment tests (four platform skips) and real disposable CLI checks. [Upstream CI passed](https://github.com/python-poetry/poetry/actions/runs/38736327430); it remains **open for maintainer review**, and is not counted as accepted work.

**Maintaining community contributions:** [WhatsApp bot PR #40](https://github.com/harshitethic/whatsapp-chatgpt/pull/40) incorporated a correction from [lucaslokchan's earlier PR #19](https://github.com/harshitethic/whatsapp-chatgpt/pull/19), preserved verified co-author credit, and added privacy tests that prevent raw chat messages and provider exceptions from reaching logs. Both Node 20 and Node 22 CI checks passed. Historical unmerged credential-exposing PRs were closed with rotation notices; closing them does not erase the old public diffs.

## Earlier projects with community adoption

My earlier Telegram/WhatsApp AI bot repositories have attracted developers and forks. They are **legacy projects built around older APIs**, not examples of my current production architecture.

| Repository | GitHub stars · forks (13 Oct 2026) |
| --- | ---: |
| [chatgpt-bot-telegram](https://github.com/harshitethic/chatgpt-bot-telegram) | 141 · 148 |
| [ChatGPT-Telegram-Bot](https://github.com/harshitethic/ChatGPT-Telegram-Bot) | 72 · 371 |
| [whatsapp-chatgpt](https://github.com/harshitethic/whatsapp-chatgpt) | 68 · 168 |

## Engineering toolbox

| Area | Technology |
| --- | --- |
| **Backend & AI** | Python, FastAPI, Node.js, APIs, local LLMs, Ollama, agent workflows |
| **Frontend** | TypeScript, React, Next.js, JavaScript |
| **Systems** | C++, Linux, macOS, SQLite WAL, fencing tokens, crash recovery, native audio |
| **Delivery** | Git, GitHub Actions, Docker, integration tests, VPS deployment, observability |

## Current focus

I publish **reproducible engineering work**, clear failure analyses, and
maintenance-focused open source rather than maximizing commit counts.
See the [public portfolio quality roadmap](portfolio/quality-roadmap-2026.md)
and recent work on [fenced leases](https://github.com/harshitethic/LeaseLedger)
and [isolated AI-agent test execution](https://github.com/harshitethic/PatchPilot/pull/24).

## Security-focused developer tooling

**[ClonePeek](https://harshitethic.github.io/clonepeek/)** provides a
standard-library-only, offline scanner to inventory execution-capable
repository configuration and a
[reusable GitHub Action](https://github.com/harshitethic/clonepeek/blob/main/docs/GITHUB-ACTION.md)
for PR checks. It reports *trigger → command → file/line → review action*
without running untrusted repository scripts. The scanner also examines
bounded first-hop local shell-script references and hardened Git diff
inspection, with explicit gaps for dynamic or transitive execution.

The [v0.5.0 release](https://github.com/harshitethic/clonepeek/releases/tag/v0.5.0)
has **64 Python tests** and passing CI across Windows, Linux and macOS,
including actual reusable-action integration tests. Its
[51-case synthetic evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md)
is deliberately labeled as *non-representative*; findings are heuristic
review prompts, **not malware verdicts or proof of repository safety**.

The [verified separate-repository consumer workflow](https://github.com/harshitethic/RepoPilot/actions/runs/38728091966) also exercised the released GitHub Action against two immutable public config snapshots: seven Cursor hooks and two VS Code folder-open tasks. [See the engineering case study](portfolio/engineering-case-studies.md) and [reproduction details](https://github.com/harshitethic/clonepeek/blob/main/docs/CROSS-REPO-SMOKE.md). This does not imply independent external adoption.

## Collaboration

I enjoy tackling concrete bugs, building useful developer tools, and working through edge cases with maintainers. For engineering opportunities, architecture discussions, or collaborations:

**[harshitethic.com](https://harshitethic.com)** · **[LinkedIn](https://www.linkedin.com/in/harshitethic/)** · **[contact@harshitethic.com](mailto:contact@harshitethic.com)**

<sub>Evidence first: source code, reproducible examples, tests, PR discussions, and the trade-offs behind implementation.</sub>
