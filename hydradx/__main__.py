import click

from hydradx import HydraDX

HYDRA_MAINNET = "wss://hydradx-rpc.dwellir.com"


@click.group()
def app():
    pass


@click.group()
def omnipool():
    pass


@omnipool.command(name="asset")
def asset():
    hydra = HydraDX(HYDRA_MAINNET)
    with hydra:
        print(hydra.api.omnipool.position(2719))


app.add_command(omnipool)

app()
