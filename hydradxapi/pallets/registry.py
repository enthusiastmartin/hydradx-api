from dataclasses import dataclass

from hydradxapi.pallets import Pallet


@dataclass
class Asset:
    asset_id: int
    decimals: int
    symbol: str


class AssetRegistry(Pallet):
    MODULE_NAME = "AssetRegistry"

    def asset_metadata(self, asset_id) -> Asset:
        entry = self.query_entry(
            self.MODULE_NAME, "AssetMetadataMap", params=[asset_id]
        )
        return Asset(
            int(asset_id),
            entry["decimals"].value,
            entry["symbol"].value,
        )
