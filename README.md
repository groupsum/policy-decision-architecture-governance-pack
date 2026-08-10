# policy-decision-architecture-governance-pack

Governance for PDP, PEP, PIP, PAP, authorization request and response contracts, permissions, enforcement gateways, entitlement inputs, failure, caching, availability, and audit evidence.

## Package identity

- Pack ID: `pack:policy-decision-architecture`
- PyPI distribution: `policy-decision-architecture-governance-pack`
- Python import: `policy_decision_architecture_governance_pack`
- Reservation owner: `extension-pack:policy-decision-architecture-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add policy-decision-architecture-governance-pack
uv run ssot pack sync . policy_decision_architecture_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://www.oasis-open.org/standard/xacmlv3-0/
