from hydradxapi import HydraDX

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
