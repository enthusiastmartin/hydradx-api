from dataclasses import dataclass
from typing import TYPE_CHECKING, List

from hydradxapi.pallets import Pallet
from hydradxapi.pallets.balances import Balances
from hydradxapi.pallets.fees import Fees, DynamicFees
from hydradxapi.pallets.registry import AssetRegistry, Asset
from hydradxapi.pallets.tokens import Tokens

if TYPE_CHECKING:
    from hydradxapi.client import Client


POOL_ACCOUNTS = {100: "5CrF36Ep1qfkBe6T5f1oMK7wvvUCcyCJPpGaGTohsJXStNKA"}


@dataclass
class Pool:
    pool_id: int
    assets: List[Asset]
    initial_amplification: int
    final_amplification: int
    initial_block: int
    final_block: int
    fee: float
    reserves: dict[int, str]
    account: str

    def as_dict(self):
        return {
            "pool_id": self.pool_id,
            "assets": [asset.as_dict() for asset in self.assets],
            "initial_amplification": self.initial_amplification,
            "final_amplification": self.final_amplification,
            "initial_block": self.initial_block,
            "final_block": self.final_block,
            "fee": self.fee,
            "reserves": self.reserves,
            "account": self.account,
        }


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

            try:
                pool_account = POOL_ACCOUNTS[int(pool_id)]
                reserves = {}
                for asset in assets:
                    balance = self._tokens.account_free_balance(
                        pool_account, int(asset)
                    )
                    reserves[int(asset)] = str(balance)
            except:
                reserves = {}
                pool_account = ""

            result[int(pool_id)] = Pool(
                pool_id,
                s_assets,
                int(i_amp),
                int(f_amp),
                int(i_block),
                int(f_block),
                fee,
                reserves,
                pool_account,
            )

        return result
