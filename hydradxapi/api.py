from hydradxapi.pallets.fees import DynamicFees
from hydradxapi.pallets.omnipool import Omnipool
from hydradxapi.pallets.registry import AssetRegistry
from hydradxapi.pallets.stableswap import StableSwap
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
