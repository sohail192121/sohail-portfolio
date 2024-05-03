# Local drill

Run `python core.py` for a synthetic SQLite backup/restore drill. It creates and closes its own temporary databases and compares ordered-row checksums after a simulated data-loss operation. It does not connect to external databases or clusters. Printed timings apply only to this local experiment and are not multi-zone recovery metrics.

Before a future Kubernetes drill: define a separate sandbox cluster, explicit target selectors, abort conditions, maximum blast radius, backup integrity checks, recovery owner and recovery verification. No Chaos Mesh or Velero deployment has been performed.
