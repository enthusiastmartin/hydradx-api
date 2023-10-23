from hydradxapi.api import API
from hydradxapi.client import Client

__all__ = ["HydraDX"]


class HydraDX:
    def __init__(self, url):
        self.url = url
        self._client = None
        self._api = None

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def connect(self):
        """

        :return:
        """
        self._client = Client(self.url)
        self._api = API(self._client)

    def close(self):
        self._client.close()
        self._client = None
        self._api = None

    @property
    def api(self):
        if self._api is None:
            raise ValueError("Client not initialized")
        return self._api
