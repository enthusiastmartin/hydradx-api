from hydradxapi import HydraDX
from hydradxapi.pallets.oracle import OraclePeriod, OracleSource

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"


def test_hydradx_init():
    hydra = HydraDX(HYDRA_MAINNET)

    # HDX
    hydra.connect()
    s = hydra.api.omnipool.asset_state(0)
    print(s)
    hydra.close()

    # GLMR
    hydra.connect()
    s = hydra.api.omnipool.asset_state(16)
    print(s)
    hydra.close()


def test_total_issuance():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    total = hydra.api.tokens.total_issuance(101)
    print(total)
    if not total > 0:
        raise AssertionError("No issuance found for BTC 2-Pool.")
    hydra.close()


def test_get_shares():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    pools = hydra.api.stableswap.pools()
    shares = pools[101].shares
    print(shares)
    if not shares > 0:
        raise AssertionError("No shares found for Pool 101.")
    hydra.close()


def test_last_block_omnipool_oracle_price():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    result = hydra.api.oracle.omnipool_oracle_price(0, OraclePeriod.LAST_BLOCK)
    hydra.close()
    print(result)
    assert result is not None


def test_short_omnipool_oracle_price():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    result = hydra.api.oracle.omnipool_oracle_price(0, OraclePeriod.SHORT)
    hydra.close()
    print(result)
    assert result is not None


def test_staking_position_votes():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    result = hydra.api.staking.position_votes()
    hydra.close()
    print(result)
    assert result is not None
