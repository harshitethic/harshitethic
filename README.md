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
All **32 tests pass** across Python 3.11–3.13 in CI. Version 0.1.2
adds seeded fault-injection tests and fixes a verified queue-starvation bug
where 100+ exhausted leases concealed runnable jobs. Version 0.1.1
introduced online WAL-safe backups and integrity verification.

[Read the architecture](https://github.com/harshitethic/LeaseLedger/blob/main/docs/architecture.md)
· [Why fencing tokens matter](https://github.com/harshitethic/LeaseLedger/blob/main/docs/notes/why-fencing-tokens.md)
· [See verified CI](https://github.com/harshitethic/LeaseLedger/actions/workflows/ci.yml)
· [v0.1.2 release](https://github.com/harshitethic/LeaseLedger/releases/tag/v0.1.2)
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
<p><strong>Engineering focus:</strong> fail-closed Docker test isolation, fenced local workspaces, protected diagnostic logs, adversarial regression tests, and <a href="https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml">live isolation CI</a>.</p>
<p><a href="https://github.com/harshitethic/PatchPilot#readme">Source and architecture →</a></p>
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
<h3><a href="https://github.com/harshitethic/PsychologyOS">PsychologyOS</a></h3>
<p><strong>Full-stack learning platform · TypeScript · Next.js</strong></p>
<p>Study materials, practice quizzes, mock exams, progress tracking, accounts, moderation, and an optional local-AI tutor.</p>
<p><strong>Engineering focus:</strong> end-to-end product architecture, health checks, and <a href="https://github.com/harshitethic/PsychologyOS/actions/workflows/ci.yml">automated project validation</a>.</p>
<p><a href="https://psychologyos.space/">Live website →</a> · <a href="https://github.com/harshitethic/PsychologyOS">Source and tests →</a></p>
</td>
<td width="50%" valign="top">
<h3><a href="https://github.com/harshitethic/RepoPilot">RepoPilot</a></h3>
<p><strong>Local codebase exploration · Python · FastAPI · React · Ollama</strong></p>
<p>Clones or imports repositories, indexes source, exposes file trees and code search, and supplies relevant context to a local language model for questions about the code.</p>
<p><strong>Engineering focus:</strong> safe streaming imports, error handling, CodeQL security scanning, and <a href="https://github.com/harshitethic/RepoPilot/actions/workflows/ci.yml">frontend/backend CI</a>.</p>
<p><a href="https://github.com/harshitethic/RepoPilot">Source →</a> · <a href="https://github.com/harshitethic/RepoPilot/blob/main/docs/http-smoke-test.md">Reproducible HTTP walkthrough →</a></p>
</td>
</tr>
</table>

## How I work — engineering evidence

Alongside source code, I maintain [engineering case studies](portfolio/engineering-case-studies.md) showing the problems, design decisions, tests and trade-offs behind my work: **lease fencing, agent isolation, ZIP/Git import boundaries, full-stack CI recovery, and native Linux/macOS portability**. Each case links to verifiable PRs and CI results.

## Open-source contributions

As of **13 October 2026**, I have **20 merged pull requests across 9 repositories owned by other developers/organizations**. These include bug fixes, tests, developer tooling, and documentation. Browse the [merged PR history](https://github.com/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic+-user%3Aharshitethic).

| Project | Accepted work |
| --- | --- |
| [Hebbian-Robotics/hflow](https://github.com/Hebbian-Robotics/hflow/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | 9 merged PRs involving data validation, artifact handling, tests, and examples |
| [Internet Archive / Open Library](https://github.com/internetarchive/openlibrary/pull/13854) | Corrected out-of-date developer documentation |
| [ChurchCRM](https://github.com/ChurchCRM/CRM/pull/10431) | Fixed floating controls overlapping modal dialogs |
| [StaveIndustries / woo-pay](https://github.com/StaveIndustries/woo-pay/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | Improved WooCommerce error reporting and payment-failure persistence |
| [pranjalparmar/fastdocparse](https://github.com/pranjalparmar/fastdocparse/pulls?q=is%3Apr+is%3Amerged+author%3Aharshitethic) | Simplified CLI errors and grounding logic |

*PR acceptance and code review are more informative than a raw count of opened PRs. Current status and diffs are available via the links above.*

**Recent maintainer review follow-through:** On [ChurchCRM PR #10484](https://github.com/ChurchCRM/CRM/pull/10484), I corrected the translation-extraction configuration in response to maintainer feedback, verified that the requested string appeared in the generated catalog without committing it, and passed lint plus independent security checks. **The PR is still open**, so it is not included in the merged-contribution count.

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

[ClonePeek](https://github.com/harshitethic/clonepeek) is a dependency-free,
offline preflight scanner for execution-capable repository config
(editor auto-tasks, npm lifecycle scripts, devcontainer commands and MCP
servers). In [v0.2.1](https://github.com/harshitethic/clonepeek/releases/tag/v0.2.1),
I reproduced and fixed a Git filesystem-monitor execution risk in passive scans.
The [v0.2.2 release](https://github.com/harshitethic/clonepeek/releases/tag/v0.2.2)
fixes a previously missed Windows PowerShell execution pattern and includes a
[46-case synthetic evaluation](https://github.com/harshitethic/clonepeek/blob/main/docs/EVALUATION.md)
with **all 34 tests passing** on Linux, macOS and Windows CI.
The evaluation deliberately records false positives and false negatives;
its scores do **not** estimate real-world malware detection.

## Collaboration

I enjoy tackling concrete bugs, building useful developer tools, and working through edge cases with maintainers. For engineering opportunities, architecture discussions, or collaborations:

**[harshitethic.com](https://harshitethic.com)** · **[LinkedIn](https://www.linkedin.com/in/harshitethic/)** · **[contact@harshitethic.com](mailto:contact@harshitethic.com)**

<sub>Evidence first: source code, reproducible examples, tests, PR discussions, and the trade-offs behind implementation.</sub>
