# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: rpc.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'rpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\trpc.proto\x12\x07kvstore\"\'\n\tKVRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"+\n\nKVResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"q\n\x14\x41ppendEntriesRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\x05\x12#\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x12.kvstore.KVRequest\x12\x14\n\x0cleaderCommit\x18\x04 \x01(\x05\"6\n\x15\x41ppendEntriesResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\"0\n\x0bVoteRequest\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\"1\n\x0cVoteResponse\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x13\n\x0bvoteGranted\x18\x02 \x01(\x08\x32\xb0\x02\n\x0fKeyValueService\x12.\n\x03Put\x12\x12.kvstore.KVRequest\x1a\x13.kvstore.KVResponse\x12.\n\x03Get\x12\x12.kvstore.KVRequest\x1a\x13.kvstore.KVResponse\x12\x31\n\x06\x44\x65lete\x12\x12.kvstore.KVRequest\x1a\x13.kvstore.KVResponse\x12N\n\rAppendEntries\x12\x1d.kvstore.AppendEntriesRequest\x1a\x1e.kvstore.AppendEntriesResponse\x12:\n\x0bRequestVote\x12\x14.kvstore.VoteRequest\x1a\x15.kvstore.VoteResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_KVREQUEST']._serialized_start=22
  _globals['_KVREQUEST']._serialized_end=61
  _globals['_KVRESPONSE']._serialized_start=63
  _globals['_KVRESPONSE']._serialized_end=106
  _globals['_APPENDENTRIESREQUEST']._serialized_start=108
  _globals['_APPENDENTRIESREQUEST']._serialized_end=221
  _globals['_APPENDENTRIESRESPONSE']._serialized_start=223
  _globals['_APPENDENTRIESRESPONSE']._serialized_end=277
  _globals['_VOTEREQUEST']._serialized_start=279
  _globals['_VOTEREQUEST']._serialized_end=327
  _globals['_VOTERESPONSE']._serialized_start=329
  _globals['_VOTERESPONSE']._serialized_end=378
  _globals['_KEYVALUESERVICE']._serialized_start=381
  _globals['_KEYVALUESERVICE']._serialized_end=685
# @@protoc_insertion_point(module_scope)
