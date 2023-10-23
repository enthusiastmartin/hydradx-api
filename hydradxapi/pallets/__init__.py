from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from hydradxapi.client import Client


class Pallet:
    def __init__(self, client: "Client"):
        self._client = client

    def query_entries(self, module, func):
        return self._client.api.query_map(module, func)

    def query_entry(self, module, func, params):
        return self._client.api.query(module, func, params)
