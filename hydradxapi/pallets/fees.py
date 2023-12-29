from dataclasses import dataclass
from hydradxapi.pallets import Pallet


@dataclass
class Fees:
    asset_fee: float
    protocol_fee: float
    block: int

    def as_dict(self):
        return {
            "asset_fee": str(self.asset_fee),
            "protocol_fee": str(self.protocol_fee),
            "block": str(self.block),
        }


class DynamicFees(Pallet):
    MODULE_NAME = "DynamicFees"

    def asset_fees(self, asset_id) -> Fees:
        entry = self.query_entry(self.MODULE_NAME, "AssetFee", params=[asset_id])
        return Fees(
            entry["asset_fee"].value / 10_000,
            entry["protocol_fee"].value / 10_000,
            int(entry["timestamp"].value),
        )
