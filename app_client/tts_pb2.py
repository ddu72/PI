# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ttts.proto\x12\x03tts\" \n\x10SynthesisRequest\x12\x0c\n\x04text\x18\x01 \x01(\t\"=\n\x11SynthesisResponse\x12\x13\n\x0b\x61udio_chunk\x18\x01 \x01(\x0c\x12\x13\n\x0b\x63hunk_index\x18\x02 \x01(\x05\x32S\n\nTTSService\x12\x45\n\x10SynthesizeStream\x12\x15.tts.SynthesisRequest\x1a\x16.tts.SynthesisResponse(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tts_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SYNTHESISREQUEST']._serialized_start=18
  _globals['_SYNTHESISREQUEST']._serialized_end=50
  _globals['_SYNTHESISRESPONSE']._serialized_start=52
  _globals['_SYNTHESISRESPONSE']._serialized_end=113
  _globals['_TTSSERVICE']._serialized_start=115
  _globals['_TTSSERVICE']._serialized_end=198
# @@protoc_insertion_point(module_scope)