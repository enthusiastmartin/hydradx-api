from hydradxapi.pallets import Pallet


class Democracy(Pallet):
    MODULE_NAME = "Democracy"

    def referendum_info(self, index) -> dict:
        entry = self.query_entry(self.MODULE_NAME, "ReferendumInfoOf", params=[index])
        return entry.value
