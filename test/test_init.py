from functools import lru_cache

from hydradxapi import HydraDX
from hydradxapi.pallets.oracle import OraclePeriod, OracleSource

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"
LOCAL = "ws://127.0.0.1:8000"

RPC = LOCAL


def test_hydradx_init():
    hydra = HydraDX(RPC)

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
    hydra = HydraDX(RPC)
    hydra.connect()
    total = hydra.api.tokens.total_issuance(101)
    print(total)
    if not total > 0:
        raise AssertionError("No issuance found for BTC 2-Pool.")
    hydra.close()


def test_get_shares():
    hydra = HydraDX(RPC)
    hydra.connect()
    pools = hydra.api.stableswap.pools()
    shares = pools[101].shares
    print(shares)
    if not shares > 0:
        raise AssertionError("No shares found for Pool 101.")
    hydra.close()


def test_last_block_omnipool_oracle_price():
    hydra = HydraDX(RPC)
    hydra.connect()
    result = hydra.api.oracle.omnipool_oracle_price(0, OraclePeriod.LAST_BLOCK)
    hydra.close()
    print(result)
    assert result is not None


def test_short_omnipool_oracle_price():
    hydra = HydraDX(RPC)
    hydra.connect()
    result = hydra.api.oracle.omnipool_oracle_price(0, OraclePeriod.SHORT)
    hydra.close()
    print(result)
    assert result is not None


def test_staking_position_votes():
    hydra = HydraDX(RPC)
    hydra.connect()
    result = hydra.api.staking.position_votes()
    hydra.close()
    print(result)
    assert result is not None


def test_staking_processed_votes():
    hydra = HydraDX(RPC)
    hydra.connect()
    result = hydra.api.staking.processed_votes()
    hydra.close()
    print(len(result))
    assert result is not None


def test_call_value():
    hydra = HydraDX(RPC)
    hydra.connect()

    votes = hydra.api.staking.position_votes()

    rv_batch = []

    for vote in votes[:2]:
        position_id = vote.position_id
        nft = hydra.api.uniques.asset(2222, position_id)
        for v in vote.votes:
            ref_index = v.referendum_id

            @lru_cache
            def is_referendum_finished(index) -> bool:
                referendum = hydra.api.democracy.referendum_info(index)
                return "Finished" in referendum.keys()

            if is_referendum_finished(ref_index):
                # print(f"{nft['owner']} : {v.referendum_id}")
                call = hydra._client.api.compose_call(
                    call_module="Democracy",
                    call_function="remove_other_vote",
                    call_params={"target": nft["owner"], "index": v.referendum_id},
                )
                rv_batch.append(call)

    call = hydra._client.api.compose_call(
        call_module="Utility", call_function="batch", call_params={"calls": rv_batch}
    )

    print(f"{call.encode()}")

    hydra.close()
