# Prototype boundaries

The queue is a single-threaded prototype and is not thread safe. Failed tasks retry immediately and can delay lower-priority tasks. Celery and Redis are not integrated.
