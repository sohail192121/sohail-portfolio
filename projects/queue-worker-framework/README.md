# Queue Worker Framework

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores concurrency control, retries, shutdown, dead letters. It is designed as a focused engineering lab for Go roles.

## Current implementation
Bounded worker concurrency, cancellation and retries. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
Go, PostgreSQL

## Architecture
```mermaid
flowchart LR
  n0["Queue"] --> n1
  n1["bounded workers"] --> n2
  n2["handler"] --> n3
  n3["retry"] --> n4
  n4["dead letter"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires Go 1.23 or later.

```sh
go test ./...
```

## Next milestones
- [ ] Durable queue adapter
- [ ] lease recovery
- [ ] jitter
- [ ] operational metrics

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
