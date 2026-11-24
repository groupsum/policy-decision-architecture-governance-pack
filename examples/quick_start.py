"""Inspect the installed pack identity."""

from policy_decision_architecture_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:policy-decision-architecture"
print(metadata["origin"]["id"])
