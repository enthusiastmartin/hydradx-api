from dataclasses import dataclass
from typing import Optional, TYPE_CHECKING

from hydradxapi.pallets import Pallet
from hydradxapi.pallets.balances import Balances
from hydradxapi.pallets.tokens import Tokens

if TYPE_CHECKING:
    from hydradxapi.client import Client


@dataclass
class AssetState:
    reserve: int
    hub_reserve: int
    shares: int
    protocol_shares: int
    cap: int
    tradability: int
    asset_id: Optional[int]

    @staticmethod
    def from_entry(asset_id: int, entry: dict) -> "AssetState":
        return AssetState(
            entry["reserve"],
            entry["hub_reserve"],
            entry["shares"],
            entry["protocol_shares"],
            entry["cap"],
            entry["tradable"],
            asset_id,
        )

    def __str__(self):
        return f"Asset: {self.asset_id}\n\tReserve: {self.reserve}\n\tLRNA: {self.hub_reserve}\n\tShares: {self.shares}\n\tProtocol: {self.protocol_shares}"


@dataclass
class Position:
    asset_id: int
    amount: int
    shares: int
    price: int

    @staticmethod
    def from_entry(entry: dict) -> "Position":
        return Position(
            entry["asset_id"], entry["amount"], entry["shares"], entry["price"]
        )


class Omnipool(Pallet):
    ACCOUNT = "7L53bUTBbfuj14UpdCNPwmgzzHSsrsTWBHX5pys32mVWM3C1"

    MODULE_NAME = "Omnipool"

    ASSET_STATE_STORAGE = "Assets"

    def __init__(self, client: "Client"):
        super().__init__(client)
        self._balances = Balances(self._client)
        self._tokens = Tokens(self._client)

    def asset_state(self, asset_id) -> AssetState:
        entry = self.query_entry(
            self.MODULE_NAME, self.ASSET_STATE_STORAGE, params=[asset_id]
        )
        if int(asset_id) == 0:
            reserve = self._balances.account_free_balance(self.ACCOUNT)
        else:
            reserve = self._tokens.account_free_balance(self.ACCOUNT, asset_id)
        entry = entry.value.copy()
        entry["reserve"] = reserve
        return AssetState.from_entry(asset_id, entry)

    def lrna_reserve(self):
        return self._tokens.account_free_balance(self.ACCOUNT, 1)

    def position(self, position_id) -> Position:
        entry = self.query_entry(self.MODULE_NAME, "Positions", params=[position_id])
        return Position.from_entry(entry)
