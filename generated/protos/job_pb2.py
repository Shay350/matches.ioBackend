# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: protos/job.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'protos/job.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10protos/job.proto\x12\x03job\x1a\x1fgoogle/protobuf/timestamp.proto\"\x8a\x02\n\x03Job\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x63ompany_name\x18\x04 \x01(\t\x12\x0e\n\x06salary\x18\x05 \x01(\x02\x12\"\n\x08industry\x18\x06 \x01(\x0e\x32\x10.job.JobIndustry\x12#\n\nexperience\x18\x07 \x01(\x0e\x32\x0f.job.Experience\x12\x30\n\x0cposting_date\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0c\x65xternal_url\x18\t \x01(\t\x12\x0e\n\x06skills\x18\n \x03(\t\x12\n\n\x02id\x18\x0b \x01(\t*\xf6\x02\n\x0bJobIndustry\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08SOFTWARE\x10\x01\x12\x0c\n\x08HARDWARE\x10\x02\x12\x0c\n\x08\x45MBEDDED\x10\x03\x12\x14\n\x10MACHINE_LEARNING\x10\x04\x12\x12\n\x0ePRODUCT_DESIGN\x10\x05\x12\x16\n\x12PRODUCT_MANAGEMENT\x10\x06\x12\x07\n\x03LAW\x10\x07\x12\x0c\n\x08MEDICINE\x10\x08\x12\x0b\n\x07\x42IOLOGY\x10\t\x12\r\n\tCHEMISTRY\x10\n\x12\x0b\n\x07\x46INANCE\x10\x0b\x12\x0e\n\nACCOUNTING\x10\x0c\x12\r\n\tMARKETING\x10\r\x12\r\n\tECONOMICS\x10\x0e\x12\x0c\n\x08\x42USINESS\x10\x0f\x12\x13\n\x0fHUMAN_RESOURCES\x10\x10\x12\x0b\n\x07\x41\x43TUARY\x10\x11\x12\x0e\n\nJOURNALISM\x10\x12\x12\x0f\n\x0bPHOTOGRAPHY\x10\x13\x12\x0e\n\nCONSULTING\x10\x14\x12\x11\n\rMANUFACTURING\x10\x15\x12\x0c\n\x08RESEARCH\x10\x16*]\n\nExperience\x12\x0e\n\nINTERNSHIP\x10\x00\x12\x0c\n\x08NEW_GRAD\x10\x01\x12\n\n\x06JUNIOR\x10\x02\x12\n\n\x06SENIOR\x10\x03\x12\x0c\n\x08\x44IRECTOR\x10\x04\x12\x0b\n\x07\x43_SUITE\x10\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOBINDUSTRY']._serialized_start=328
  _globals['_JOBINDUSTRY']._serialized_end=702
  _globals['_EXPERIENCE']._serialized_start=704
  _globals['_EXPERIENCE']._serialized_end=797
  _globals['_JOB']._serialized_start=59
  _globals['_JOB']._serialized_end=325
# @@protoc_insertion_point(module_scope)
