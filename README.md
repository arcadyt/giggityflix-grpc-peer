# GiggityFlix gRPC Shared Module

Shared gRPC interface definitions for communication between peer and edge services in the GiggityFlix media streaming
platform.

## Overview

This package provides:

- Protocol Buffer definitions (`.proto` files) in the `protos/` directory
- Generated Python gRPC code in the `src/giggityflix_grpc_peer/` directory
- Helper scripts to regenerate code when proto files change

## Installation

### Standard Installation

```bash
# Install directly from git repository
pip install git+https://github.com/giggityflix/grpc-peer.git

# Or install locally after cloning
git clone https://github.com/giggityflix/grpc-peer.git
cd grpc-peer
pip install .
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/giggityflix/grpc-peer.git
cd grpc-peer

# Install in development mode
pip install -e .
```

## Usage

### Importing the package

The package provides easy access to the gRPC classes and message types:

```python
# Import the stub for client-side usage
from giggityflix_grpc_peer.peer_edge import PeerEdgeServiceStub

# Import message types
from giggityflix_grpc_peer.peer_edge import (
    EdgeMessage, PeerMessage,
    PeerRegistrationRequest, PeerRegistrationResponse
)

# Import server-side classes
from giggityflix_grpc_peer.peer_edge import (
    PeerEdgeServiceServicer,
    add_PeerEdgeServiceServicer_to_server
)
```

### Client Example

```python
import grpc
from giggityflix_grpc_peer.peer_edge import PeerEdgeServiceStub, PeerRegistrationRequest

# Create a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
stub = PeerEdgeServiceStub(channel)

# Create a stream for bidirectional communication
requests_iterator = iter([
    PeerMessage(
        request_id="req1",
        registration_request=PeerRegistrationRequest(
            peer_name="my-peer",
            catalog_ids=["uuid1", "uuid2"]
        )
    )
])

# Start the bidirectional stream
responses_iterator = stub.message(requests_iterator)

# Process responses
for response in responses_iterator:
    print(f"Received response: {response}")
```

### Server Example

```python
import asyncio
import grpc
from giggityflix_grpc_peer.peer_edge import (
    PeerEdgeServiceServicer,
    add_PeerEdgeServiceServicer_to_server,
    EdgeMessage, PeerRegistrationResponse
)


class MyPeerEdgeService(PeerEdgeServiceServicer):
    async def message(self, request_iterator, context):
        """Handle bidirectional streaming RPC."""
        async for request in request_iterator:
            if request.HasField('registration_request'):
                # Handle registration request
                reg_request = request.registration_request

                # Create response
                response = EdgeMessage(
                    request_id=request.request_id,
                    registration_response=PeerRegistrationResponse(
                        peer_name=reg_request.peer_name,
                        edge_name="my-edge",
                        success=True
                    )
                )

                yield response


async def serve():
    server = grpc.aio.server()
    add_PeerEdgeServiceServicer_to_server(MyPeerEdgeService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
```

## Generating gRPC Code

If you modify the `.proto` files or add new ones, you need to regenerate the gRPC code:

```bash
# Using the installed package
python -m giggityflix_grpc_peer.compile_protos

# Or from the source directory
python -m src.giggityflix_grpc_peer.compile_protos
```

## Project Structure

- `protos/`: Protocol Buffer definition files
- `src/giggityflix_grpc_peer/`: Package source code
    - `__init__.py`: Package initialization
    - `peer_edge.py`: Module for easy imports
    - `peer_edge_pb2.py`: Generated message classes
    - `peer_edge_pb2_grpc.py`: Generated service classes
    - `compile_protos.py`: Script to generate code from `.proto` files
