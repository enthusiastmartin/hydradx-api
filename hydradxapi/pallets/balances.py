from hydradxapi.pallets import Pallet


class Balances(Pallet):
    MODULE_NAME = "Balances"

    def account_free_balance(self, account) -> int:
        return self.query_entry("System", "Account", params=[account]).value["data"][
            "free"
        ]
