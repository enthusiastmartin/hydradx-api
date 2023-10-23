from hydradxapi.pallets import Pallet


class Tokens(Pallet):
    MODULE_NAME = "Tokens"

    def account_free_balance(self, account, asset_id) -> int:
        return self.query_entry(
            self.MODULE_NAME, "Accounts", params=[account, asset_id]
        )["free"].value
