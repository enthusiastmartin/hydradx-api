from hydradxapi.pallets.fees import DynamicFees
from hydradxapi.pallets.omnipool import Omnipool
from hydradxapi.pallets.oracle import Oracle
from hydradxapi.pallets.registry import AssetRegistry
from hydradxapi.pallets.stableswap import StableSwap
from hydradxapi.pallets.staking import Staking
from hydradxapi.pallets.tokens import Tokens


class API:
    """
    HydraDX chain API
    """

    def __init__(self, client):
        self._client = client

    @property
    def omnipool(self):
        return Omnipool(self._client)

    @property
    def fees(self):
        return DynamicFees(self._client)

    @property
    def registry(self):
        return AssetRegistry(self._client)

    @property
    def stableswap(self):
        return StableSwap(self._client)

    @property
    def tokens(self):
        return Tokens(self._client)

    @property
    def oracle(self):
        return Oracle(self._client)

    @property
    def staking(self):
        return Staking(self._client)
