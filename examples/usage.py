"""Find a specification and its downstream path in the installed manifest."""

from policy_decision_architecture_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:authorization-request-and-response-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-authorization-request-and-response-contract.yaml"
