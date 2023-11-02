from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING, List

from hydradxapi.pallets import Pallet
from hydradxapi.pallets.balances import Balances
from hydradxapi.pallets.fees import Fees, DynamicFees
from hydradxapi.pallets.registry import AssetRegistry, Asset
from hydradxapi.pallets.tokens import Tokens

if TYPE_CHECKING:
    from hydradxapi.client import Client


@dataclass
class Pool:
    pool_id: int
    assets: List[Asset]
    initial_amplification: int
    final_amplification: int
    initial_block: int
    final_block: int
    fee: float


class StableSwap(Pallet):
    MODULE_NAME = "Stableswap"

    def __init__(self, client: "Client"):
        super().__init__(client)
        self._balances = Balances(self._client)
        self._tokens = Tokens(self._client)
        self._registry = AssetRegistry(self._client)
        self._fees = DynamicFees(self._client)

    def pools(self) -> dict[int, Pool]:
        entries = self.query_entries(self.MODULE_NAME, "Pools")
        result = {}
        for entry in entries:
            pool_id = entry[0].value
            assets = entry[1]["assets"].value
            i_amp = entry[1]["initial_amplification"].value
            f_amp = entry[1]["final_amplification"].value
            i_block = entry[1]["initial_block"].value
            f_block = entry[1]["final_block"].value
            fee = int(entry[1]["fee"].value) / 10000

            s_assets = [self._registry.asset_metadata(int(asset)) for asset in assets]
            result[int(pool_id)] = Pool(
                pool_id,
                s_assets,
                int(i_amp),
                int(f_amp),
                int(i_block),
                int(f_block),
                fee,
            )

        return result
