# Real demonstrations and verification

A quick way to inspect runnable behavior. These are existing repository artifacts, not generated product mockups.

| Tool | Demonstration | What it proves | What it does not prove |
| --- | --- | --- | --- |
| [LeaseLedger](https://github.com/harshitethic/LeaseLedger) | [Offline recovery walkthrough](https://github.com/harshitethic/LeaseLedger/blob/main/docs/reproducible-demo.md) and [expected machine-readable output](https://github.com/harshitethic/LeaseLedger/blob/main/docs/recovery-demo-output.json) | Real SQLite fencing and crash-recovery example; assertions run in CI | Multi-host consensus or exactly-once external effects |
| [PatchPilot](https://github.com/harshitethic/PatchPilot) | [Browser verification](https://github.com/harshitethic/PatchPilot/blob/main/docs/browser-verification.md), [sandbox CI](https://github.com/harshitethic/PatchPilot/actions/workflows/docker-isolation.yml) | Local browser scenarios and isolated Docker execution checks | Independent production security assessment |
| [RepoPilot](https://github.com/harshitethic/RepoPilot) | [Captured browser walkthrough](https://github.com/harshitethic/RepoPilot/blob/main/docs/RepoPilot-live-verified-walkthrough.gif) and [test method](https://github.com/harshitethic/RepoPilot/blob/main/docs/browser-demo.md) | Actual local app operations with controlled ZIP projects | Real model inference in the delayed-answer fixture |
| [ClonePeek](https://github.com/harshitethic/clonepeek) | [CLI replay](https://harshitethic.github.io/clonepeek/#video-demo), [demo fixture](https://github.com/harshitethic/clonepeek/blob/main/assets/demo-output.txt) and [GitHub Action CI](https://github.com/harshitethic/clonepeek/actions/workflows/composite-action.yml) | Known script/hook detection without executing sample code | Comprehensive detection or a guarantee that a repository is safe |

## Still needed

- [ ] Record an independent, unedited PatchPilot end-to-end run, with model version and local runtime recorded
- [ ] Have an outside developer follow the installation instructions without maintainer help
- [ ] Collect consented user feedback and note issues fixed as a result
- [ ] Revalidate links and CI after future releases

Please report any broken commands with exact environment details and redacted logs. This document separates *tested fixtures* from independent production evidence.
