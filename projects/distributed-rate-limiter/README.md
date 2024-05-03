# Distributed Rate Limiter

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores token bucket, atomic admission, tenant keys, benchmarks. It is designed as a focused engineering lab for Go roles.

## Current implementation
Mutex-protected token bucket with injected clock. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
Go, Redis, Lua

## Architecture
```mermaid
flowchart LR
  n0["Request"] --> n1
  n1["tenant bucket"] --> n2
  n2["atomic refill and consume"] --> n3
  n3["allow or reject"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires Go 1.23 or later.

```sh
go test ./...
```

## Next milestones
- [ ] Redis Lua implementation
- [ ] multi-process atomicity
- [ ] HTTP middleware
- [ ] benchmarks

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
