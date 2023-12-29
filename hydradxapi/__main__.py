import click

from hydradxapi import HydraDX

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"


@click.group()
def app():
    pass


@click.group()
def omnipool():
    pass


@click.group()
def registry():
    pass


@click.group()
def stableswap():
    pass


@omnipool.command(name="state")
def state():
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.omnipool.state())


@omnipool.command(name="asset")
@click.argument("asset_id")
def asset(asset_id):
    if int(asset_id) == 1:
        print("LRNA asset does not have a state")
        return
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.omnipool.asset_state(asset_id))


@omnipool.command(name="position")
@click.argument("position_id")
def position(position_id):
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.omnipool.position(position_id))


@omnipool.command(name="fees")
@click.argument("asset_id")
def position(asset_id):
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.fees.asset_fees(asset_id))


@registry.command(name="metadata")
@click.argument("asset_id")
def metadata(asset_id):
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.registry.asset_metadata(asset_id))


@registry.command(name="all")
def all_assets():
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.registry.assets())


@registry.command(name="stablepool_assets")
def stableswap_assets():
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.registry.stablepool_assets())


@stableswap.command(name="pools")
def pools():
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.stableswap.pools())


app.add_command(omnipool)
app.add_command(registry)
app.add_command(stableswap)

app()
