from hydradxapi.pallets import Pallet


class Uniques(Pallet):
    MODULE_NAME = "Uniques"

    def asset(self, collection, item) -> dict:
        entry = self.query_entry(self.MODULE_NAME, "Asset", params=[collection, item])
        return entry.value
