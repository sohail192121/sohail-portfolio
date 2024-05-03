# Domain-Driven Booking Service

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores booking invariants, overlap prevention, transactions, tenant isolation. It is designed as a focused engineering lab for Go roles.

## Current implementation
Tenant-scoped half-open intervals and atomic overlap checks in memory. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
Go, PostgreSQL

## Architecture
```mermaid
flowchart LR
  n0["Booking command"] --> n1
  n1["tenant resource"] --> n2
  n2["overlap check"] --> n3
  n3["transaction"] --> n4
  n4["confirmation"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires Go 1.23 or later.

```sh
go test ./...
```

## Next milestones
- [ ] PostgreSQL exclusion constraints
- [ ] HTTP adapter
- [ ] idempotency
- [ ] database integration tests

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
