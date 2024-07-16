from enum import Enum
from typing import Optional

from hydradxapi.pallets import Pallet


class OracleSource(Enum):
    OMNIPOOL = "omnipool"
    STABLESWAP = "stablesw"


class OraclePeriod(Enum):
    LAST_BLOCK = "LastBlock"
    SHORT = "Short"
    TEN_MINUTES = "TenMinutes"
    HOUR = "Hour"
    DAY = "Day"
    WEEK = "Week"


class Price:
    n: int
    d: int

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __str__(self):
        return f"Price({self.n},{self.n})"

    def to_float(self):
        return self.n / self.d


class Oracle(Pallet):
    MODULE_NAME = "EmaOracle"
    LRNA = 1

    def oracle_price(
        self, source: OracleSource, asset_a: int, asset_b: int, period: OraclePeriod
    ) -> Optional[Price]:
        r = self.query_entry(
            self.MODULE_NAME,
            "Oracles",
            params=[source.value.encode("utf-8"), (asset_a, asset_b), period.value],
        )
        if r is None:
            return None

        n = r.value[0]["price"]["n"]
        d = r.value[0]["price"]["d"]
        return Price(n, d)

    def omnipool_oracle_price(
        self, asset: int, period: OraclePeriod
    ) -> Optional[Price]:
        return self.oracle_price(OracleSource.OMNIPOOL, self.LRNA, asset, period)
