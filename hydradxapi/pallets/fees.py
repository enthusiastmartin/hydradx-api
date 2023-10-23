from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from hydradxapi.pallets import Pallet
from hydradxapi.pallets.balances import Balances
from hydradxapi.pallets.tokens import Tokens

if TYPE_CHECKING:
    from hydradxapi.client import Client


@dataclass
class Fees:
    asset_fee: float
    protocol_fee: float
    block: int


class DynamicFees(Pallet):
    MODULE_NAME = "DynamicFees"

    def asset_fees(self, asset_id) -> Fees:
        entry = self.query_entry(self.MODULE_NAME, "AssetFee", params=[asset_id])
        print(entry)
        return Fees(
            entry["asset_fee"].value / 10_000,
            entry["protocol_fee"].value / 10_000,
            int(entry["timestamp"].value),
        )
