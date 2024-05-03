# Identity and Access Service

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores refresh rotation, RBAC, audit trail, revocation. It is designed as a focused engineering lab for .NET roles.

## Current implementation
Hashed opaque refresh tokens, one-time rotation and role checks. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
C#, ASP.NET Core, PostgreSQL

## Architecture
```mermaid
flowchart LR
  n0["Sign-in"] --> n1
  n1["token issue"] --> n2
  n2["role check"] --> n3
  n3["refresh rotation"] --> n4
  n4["revocation"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires .NET SDK 9.

```sh
dotnet run
```

## Next milestones
- [ ] ASP.NET JWT issuer
- [ ] password hashing
- [ ] token-family replay revocation
- [ ] durable audit store

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
