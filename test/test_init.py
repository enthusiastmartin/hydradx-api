from hydradxapi import HydraDX

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"

def test_hydradx_init():
    hydra = HydraDX(HYDRA_MAINNET)
    hydra.connect()
    s = hydra.api.omnipool.asset_state(0)
    print(s)
    hydra.close()

    hydra.connect()

    s = hydra.api.omnipool.asset_state(2)
    print(s)
    hydra.close()

