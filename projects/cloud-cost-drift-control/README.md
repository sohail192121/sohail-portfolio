# Cloud Cost and Drift Control

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores drift detection, tag policy, idle resources, cost reports. It is designed as a focused engineering lab for DevOps roles.

## Current implementation
Offline inventory policy and drift report, with no cloud mutations. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
Python, Terraform, AWS Cost Explorer, Infracost

## Architecture
```mermaid
flowchart LR
  n0["Billing and inventory"] --> n1
  n1["normalize"] --> n2
  n2["policy checks"] --> n3
  n3["report"] --> n4
  n4["reviewed remediation"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires Python 3.11 or later; standard library only.

```sh
python -m unittest discover -s tests -v
```

## Next milestones
- [ ] Read-only AWS collector
- [ ] Terraform plan adapter
- [ ] Infracost estimates
- [ ] scheduled reports

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
