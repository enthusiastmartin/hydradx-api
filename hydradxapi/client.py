from substrateinterface import SubstrateInterface
from substrateinterface.exceptions import SubstrateRequestException


class Client:
    def __init__(self, url):
        try:
            api = SubstrateInterface(
                url=url,
                type_registry_preset="polkadot",
            )
        except ConnectionRefusedError as e:
            raise SubstrateRequestException(f"⚠️ Failed to connect to {url}") from e
        except Exception as e:
            raise RuntimeError(str(e)) from e
        self.api = api

    def close(self):
        self.api.close()
