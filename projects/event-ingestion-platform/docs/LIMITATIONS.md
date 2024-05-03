# Prototype boundaries

The bounded queue and log are volatile; replay offsets are global log positions filtered by tenant. Draining currently retains all events without a retention policy.
