# HydraDX interface

## Description
Simple API for interacting with HydraDX chain.
Mostly support for easily querying storage.
Other features might be added in the future.

## Installation
```bash
pip install hydradx-api
```

## Usage
```python
RPC="ws://127.0.0.1:9944"

from hydradx import HydraDX
hydradx_api = HydraDX(RPC) 
hydradx_api.connect()
state = hydradx_api.api.omnipool.asset_state(0)
...
hydradx_api.close()

```

or taking advantage of context manager:

```python
RPC="ws://127.0.0.1:9944"

from hydradx import HydraDX
with HydraDX(RPC) as hydradx_api:
    state = hydradx_api.api.omnipool.asset_state(0)
    ...

```

## Omnipool support
API currently supports the following:

- `asset_state(asset_id)` - retrieves state of an asset
- `position(position_id)` - retrieves details of a position
- `lrna_reserve()` - returns lrna reserve in the omnipool

...more to be added.