# HydraDX interface for python

## Description
Simple API for interacting with HydraDX chain in python.
Mostly support for easy storage querying.
Other features might be added in the future.

## Installation
```bash
pip install hydradx-api
```

## Usage
```python
RPC="ws://127.0.0.1:9944"

from hydradx import HydraDX
chain = HydraDX(RPC) 
chain.connect()
state = chain.api.omnipool.asset_state(0)
...
chain.close()

```

or taking advantage of context manager:

```python
RPC="ws://127.0.0.1:9944"

from hydradx import HydraDX
with HydraDX(RPC) as chain:
    state = chain.api.omnipool.asset_state(0)
    ...

```

## Omnipool support
API currently supports the following:

- `asset_state(asset_id)` - retrieves state of an asset
- `position(position_id)` - retrieves details of a position
- `lrna_reserve()` - returns lrna reserve in the omnipool

...more to be added.