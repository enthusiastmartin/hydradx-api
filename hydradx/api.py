from hydradx.pallets.omnipool import Omnipool


class API:
    def __init__(self, client):
        self._client = client

    @property
    def omnipool(self):
        return Omnipool(self._client)
