# GiggityFlix gRPC Shared Module

Shared gRPC interface definitions for communication between peer and edge services in the GiggityFlix media streaming platform.

## Overview

This package provides:

- Protocol Buffer definitions (`.proto` files) in the `protos/` directory
- Generated Python gRPC code in the `src/generated/` directory
- Helper scripts to regenerate code when proto files change

## Installation

```bash
# Install the package
pip install -e .

# Using Poetry
poetry install
```

## Usage

After installation, you can import the generated gRPC modules:

```python
# Import peer-edge service definitions
from src.generated.peer_edge import peer_edge_pb2, peer_edge_pb2_grpc

# Create a gRPC stub
channel = grpc.insecure_channel('localhost:50051')
stub = peer_edge_pb2_grpc.PeerEdgeServiceStub(channel)

# Create a message
request = peer_edge_pb2.PeerRegistrationRequest(
    peer_name="my-peer",
    catalog_uuids=["uuid1", "uuid2"]
)
```

## Generating gRPC Code

To regenerate the gRPC code after modifying proto files:

```bash
# Using Poetry script
poetry run generate-protos

# Using Python module
python -m scripts.generate_protos
```

## Adding New Proto Files

1. Add your `.proto` file to the `protos/` directory
2. Run the generate-protos script
3. Import the generated modules as shown in the usage example

## Development Workflow

1. Make changes to `.proto` files in the `protos/` directory
2. Run `poetry run generate-protos` to regenerate the Python code
3. The generated code will be in `src/generated/<proto_module>/`
