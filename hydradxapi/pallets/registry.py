from dataclasses import dataclass
from typing import Optional

from hydradxapi.pallets import Pallet


@dataclass
class Asset:
    asset_id: int
    decimals: Optional[int]
    symbol: Optional[str]


class AssetRegistry(Pallet):
    MODULE_NAME = "AssetRegistry"

    def asset_metadata(self, asset_id) -> Asset:
        entry = self.query_entry(
            self.MODULE_NAME, "AssetMetadataMap", params=[asset_id]
        )
        entry = entry.value
        return Asset(
            int(asset_id),
            entry["decimals"] if entry else None,
            entry["symbol"] if entry else None,
        )

    def stablepool_assets(self) -> list[Asset]:
        entries = self.query_entries(
            self.MODULE_NAME, "Assets"
        )

        result = []
        for entry in entries:
            if entry[1]["asset_type"] == "StableSwap":
                asset_id = int(entry[0].value)
                asset = self.asset_metadata(asset_id)
                result.append(asset)

        return result

