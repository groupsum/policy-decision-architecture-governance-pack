<div align="center">

# policy-decision-architecture-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/policy-decision-architecture-governance-pack.svg)](https://pypi.org/project/policy-decision-architecture-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/policy-decision-architecture-governance-pack.svg)](https://pypi.org/project/policy-decision-architecture-governance-pack/)
[![License](https://img.shields.io/pypi/l/policy-decision-architecture-governance-pack.svg)](https://pypi.org/project/policy-decision-architecture-governance-pack/)
[![CI](https://github.com/groupsum/policy-decision-architecture-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/groupsum/policy-decision-architecture-governance-pack/actions/workflows/ci.yml)
[![Publish](https://github.com/groupsum/policy-decision-architecture-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/policy-decision-architecture-governance-pack/actions/workflows/publish.yml)

</div>

Governance for PDP, PEP, PIP, PAP, authorization request and response contracts, permissions, enforcement gateways, entitlement inputs, failure, caching, availability, and audit evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `policy-decision-architecture-governance-pack` is an installable SSOT governance pack for Policy Decision Architecture. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for policy decision architecture, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`policy-decision-architecture-governance-pack`](https://pypi.org/project/policy-decision-architecture-governance-pack/)
- GitHub package repository: [`groupsum/policy-decision-architecture-governance-pack`](https://github.com/groupsum/policy-decision-architecture-governance-pack)
- Import package: `policy_decision_architecture_governance_pack`
- 4 portable downstream ADR templates for governed decisions.
- 7 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:policy-decision-architecture`
- PyPI package: `policy-decision-architecture-governance-pack`
- Import package: `policy_decision_architecture_governance_pack`
- GitHub repository: [groupsum/policy-decision-architecture-governance-pack](https://github.com/groupsum/policy-decision-architecture-governance-pack)
- Reservation owner: `extension-pack:policy-decision-architecture-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

Policy Decision Architecture

## Authority Sources

- [OASIS XACML 3.0](https://www.oasis-open.org/standard/xacmlv3-0/)

## Included ADRs

- [`adr:policy-decisions-use-explicit-pdp-pep-pip-pap-boundaries`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/adr/ADR-1000-policy-decisions-use-explicit-pdp-pep-pip-pap-boundaries.yaml) - Policy Decisions Use Explicit PDP PEP PIP PAP Boundaries
- [`adr:policy-inputs-use-principal-action-resource-and-context`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/adr/ADR-1001-policy-inputs-use-principal-action-resource-and-context.yaml) - Policy Inputs Use Principal Action Resource And Context
- [`adr:xacml-is-a-reference-architecture-not-a-required-language`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/adr/ADR-1002-xacml-is-a-reference-architecture-not-a-required-language.yaml) - XACML Is A Reference Architecture Not A Required Language
- [`adr:policy-gateways-are-enforcement-points`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/adr/ADR-1003-policy-gateways-are-enforcement-points.yaml) - Policy Gateways Are Enforcement Points

## Included SPECs

- [`spc:authorization-request-and-response-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2000-authorization-request-and-response-contract.yaml) - Authorization Request And Response Contract
- [`spc:pdp-pep-pip-pap-architecture-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2001-pdp-pep-pip-pap-architecture-contract.yaml) - PDP PEP PIP PAP Architecture Contract
- [`spc:permission-action-and-resource-taxonomy-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2002-permission-action-and-resource-taxonomy-contract.yaml) - Permission Action And Resource Taxonomy Contract
- [`spc:policy-gateway-enforcement-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2003-policy-gateway-enforcement-contract.yaml) - Policy Gateway Enforcement Contract
- [`spc:entitlement-to-policy-input-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2004-entitlement-to-policy-input-contract.yaml) - Entitlement To Policy Input Contract
- [`spc:authorization-failure-cache-and-availability-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2005-authorization-failure-cache-and-availability-contract.yaml) - Authorization Failure Cache And Availability Contract
- [`spc:authorization-decision-audit-contract`](https://github.com/groupsum/policy-decision-architecture-governance-pack/blob/master/src/policy_decision_architecture_governance_pack/templates/specs/SPEC-2006-authorization-decision-audit-contract.yaml) - Authorization Decision Audit Contract

## Install With uv

```bash
uv add policy-decision-architecture-governance-pack
uv add ssot-registry policy-decision-architecture-governance-pack
```

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect policy_decision_architecture_governance_pack
uvx --from ssot-registry ssot pack preflight . policy_decision_architecture_governance_pack --all
uvx --from ssot-registry ssot pack sync . policy_decision_architecture_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from policy_decision_architecture_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-authorization-request-and-response-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/policy-decision-architecture-governance-pack](https://github.com/groupsum/policy-decision-architecture-governance-pack)
- PyPI package: [policy-decision-architecture-governance-pack](https://pypi.org/project/policy-decision-architecture-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the policy decision architecture governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
