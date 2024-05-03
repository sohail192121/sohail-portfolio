# Prototype boundaries

Cancellation waits for active handlers, which must honor context. Retries have no backoff. The job source and dead letters are in memory, with no crash recovery.
