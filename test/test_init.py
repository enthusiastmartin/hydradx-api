from hydradxapi import HydraDX


def test_hydradx_init():
    hydra = HydraDX("url")
    assert hydra.url == "url"

    with hydra:

        h = hydra.api.omnipool
        print(h)
