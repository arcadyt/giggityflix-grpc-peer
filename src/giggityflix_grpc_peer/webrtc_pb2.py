# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: webrtc.proto
# Protobuf Python Version: 6.30.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    0,
    '',
    'webrtc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import commons_pb2 as commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cwebrtc.proto\x12\x15giggityflix_grpc_peer\x1a\rcommons.proto\"\xa4\x01\n\x14StreamSessionRequest\x12\x12\n\ncatalog_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x1d\n\x10max_bitrate_kbps\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x0fpreferred_codec\x18\x04 \x01(\tH\x01\x88\x01\x01\x42\x13\n\x11_max_bitrate_kbpsB\x12\n\x10_preferred_codec\"\x99\x01\n\x15StreamSessionResponse\x12\x12\n\ncatalog_id\x18\x01 \x01(\t\x12\x12\n\nsession_id\x18\x02 \x01(\t\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12=\n\x05\x65rror\x18\x04 \x01(\x0e\x32).giggityflix_grpc_peer.CatalogErrorReasonH\x00\x88\x01\x01\x42\x08\n\x06_error\"+\n\x08SDPOffer\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0b\n\x03sdp\x18\x02 \x01(\t\",\n\tSDPAnswer\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0b\n\x03sdp\x18\x02 \x01(\t\"`\n\x0cICECandidate\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x11\n\tcandidate\x18\x02 \x01(\t\x12\x0f\n\x07sdp_mid\x18\x03 \x01(\t\x12\x18\n\x10sdp_m_line_index\x18\x04 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'webrtc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STREAMSESSIONREQUEST']._serialized_start=55
  _globals['_STREAMSESSIONREQUEST']._serialized_end=219
  _globals['_STREAMSESSIONRESPONSE']._serialized_start=222
  _globals['_STREAMSESSIONRESPONSE']._serialized_end=375
  _globals['_SDPOFFER']._serialized_start=377
  _globals['_SDPOFFER']._serialized_end=420
  _globals['_SDPANSWER']._serialized_start=422
  _globals['_SDPANSWER']._serialized_end=466
  _globals['_ICECANDIDATE']._serialized_start=468
  _globals['_ICECANDIDATE']._serialized_end=564
# @@protoc_insertion_point(module_scope)
