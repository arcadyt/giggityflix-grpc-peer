"""
Giggityflix gRPC Peer communication library.

This package provides gRPC interfaces for communication between peers and edge services
in the Giggityflix media streaming platform.
"""

# Version info
__version__ = "0.1.0"

# Import generated modules
import giggityflix_grpc_peer.base_pb2 as base
import giggityflix_grpc_peer.base_pb2_grpc as base_grpc
import giggityflix_grpc_peer.catalog_pb2 as catalog
import giggityflix_grpc_peer.file_operations_pb2 as file_operations
import giggityflix_grpc_peer.media_pb2 as media
import giggityflix_grpc_peer.webrtc_pb2 as webrtc
import giggityflix_grpc_peer.commons_pb2 as commons

# Re-export service classes
PeerEdgeServiceStub = base_grpc.PeerEdgeServiceStub
PeerEdgeServiceServicer = base_grpc.PeerEdgeServiceServicer
add_PeerEdgeServiceServicer_to_server = base_grpc.add_PeerEdgeServiceServicer_to_server

# Re-export message classes
EdgeMessage = base.EdgeMessage
PeerMessage = base.PeerMessage
EdgeWebRTCMessage = base.EdgeWebRTCMessage
PeerWebRTCMessage = base.PeerWebRTCMessage

# Re-export error types
CatalogErrorReason = commons.CatalogErrorReason

# Define what gets imported with "from giggityflix_grpc_peer import *"
__all__ = [
    # Service classes
    'PeerEdgeServiceStub', 'PeerEdgeServiceServicer', 'add_PeerEdgeServiceServicer_to_server',

    # Main message types
    'EdgeMessage', 'PeerMessage', 'EdgeWebRTCMessage', 'PeerWebRTCMessage',

    # Domain modules
    'catalog', 'file_operations', 'media', 'webrtc', 'commons',

    # Base module
    'base',

    # Error types
    'CatalogErrorReason',
]