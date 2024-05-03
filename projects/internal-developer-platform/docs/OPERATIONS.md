# Operations

Run `python core.py sample-api platform --output artifacts` to generate a service template. Output uses an intentionally invalid image placeholder, requiring a reviewed immutable image digest before deployment. The namespace enforces restricted pod security and starts with deny-all networking; add reviewed ingress/egress policies before enabling application traffic. Supply a non-root runtime user in the image. Review probes, resource sizing and network policies for the actual application.

The ArgoCD application under templates is a reference and is not applied by the generator. Repository creation, pipeline creation, environment provisioning and monitoring integration are pending. There is no production credential use in this prototype.
