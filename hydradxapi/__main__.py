import click

from hydradxapi import HydraDX

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"


@click.group()
def app():
    pass


@click.group()
def omnipool():
    pass


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


app.add_command(omnipool)

app()
