from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException


class Client:
    def __init__(self, url):
        self._url = url

    def connect(self):
        try:
            api = SubstrateInterface(
                url=self._url, type_registry_preset="polkadot", auto_reconnect=True
            )
            hash = api.get_chain_head()
            api.init_runtime(hash)
        except ConnectionRefusedError as e:
            raise SubstrateRequestException(
                f"⚠️ Failed to connect to {self._url}"
            ) from e
        except Exception as e:
            raise RuntimeError(str(e)) from e
        self.api = api

    def close(self):
        self.api.close()
