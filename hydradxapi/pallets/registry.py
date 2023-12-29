from dataclasses import dataclass
from typing import Optional

from hydradxapi.pallets import Pallet


@dataclass
class Asset:
    asset_id: int
    decimals: Optional[int]
    symbol: Optional[str]

    def as_dict(self):
        return {
            "asset_id": self.asset_id,
            "decimals": self.decimals,
            "symbol": self.symbol,
        }


class AssetRegistry(Pallet):
    MODULE_NAME = "AssetRegistry"

    def assets(self) -> dict[int, Asset]:
        entries = self.query_entries(self.MODULE_NAME, "AssetMetadataMap")
        result = {}
        for entry in entries:
            asset_id = int(entry[0].value)
            entry = entry[1].value.copy()
            asset = Asset(
                asset_id,
                entry["decimals"],
                entry["symbol"],
            )
            result[asset_id] = asset
        return result

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
        entries = self.query_entries(self.MODULE_NAME, "Assets")

        result = []
        for entry in entries:
            if entry[1]["asset_type"] == "StableSwap":
                asset_id = int(entry[0].value)
                asset = self.asset_metadata(asset_id)
                result.append(asset)

        return result
