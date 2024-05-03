# Async API with Celery Workers

**Sohail Sharif · Personal engineering project · Core prototype**

## Problem
This project explores task priorities, bounded retries, dead letters, load tests. It is designed as a focused engineering lab for Python roles.

## Current implementation
Stable priority scheduling, bounded retries and dead-letter capture. See source and executable tests for the exact behavior.

This repository is an initial implementation, not a deployed production system. The full target architecture below is a roadmap. No throughput, uptime, savings or recovery claims have been measured for a production environment.

## Target stack
Python, FastAPI, Celery, Redis

## Architecture
```mermaid
flowchart LR
  n0["API"] --> n1
  n1["priority queue"] --> n2
  n2["worker"] --> n3
  n3["result or bounded retry"] --> n4
  n4["dead letter"]
```

The diagram describes the target architecture; adapters listed below are not implemented yet.

## Run and verify
Run from this directory. Requires Python 3.11 or later; standard library only.

```sh
python -m unittest discover -s tests -v
```

## Next milestones
- [ ] FastAPI routes
- [ ] Celery Redis adapter
- [ ] distributed result store
- [ ] k6 load measurements

## Trade-offs
- The domain core is isolated from infrastructure so its invariants can be tested quickly.
- In-memory state makes the prototype reproducible but does not survive restarts or coordinate multiple machines.
- Production authentication, secret management, persistence, metrics and deployment verification remain required.

## Evidence
Tests are executable specifications. Cloud and load-test results are deliberately unclaimed. Record real commands, versions, hardware, dataset, date and results in `docs/VALIDATION.md` before quoting numbers on a resume.

## Interview discussion
Explain the failure boundary, tenant boundary, consistency model, retry behavior, operational signals and why the chosen persistence adapter fits the workload.
