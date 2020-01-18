#!/usr/bin/env python

import re
from keyword import kwlist
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper
from csgo import common_enums

kwlist = set(kwlist + ['None'])

_proto_modules = ['gcsystemmsgs_pb2',
                  'gcsdk_gcmessages_pb2',
                  'cstrike15_gcmessages_pb2',
                  'econ_gcmessages_pb2',
                  ]

_proto_module = __import__("csgo.protobufs", globals(), locals(), _proto_modules, 0)

classes = {}

for name in _proto_modules:

    proto = getattr(_proto_module, name)
    gvars = globals()

    for class_name, value in proto.__dict__.items():
        if not isinstance(value, EnumTypeWrapper) or hasattr(common_enums, class_name):
            continue

        attrs_starting_with_number = False
        attrs = {}

        for ikey, ivalue in value.items():
            ikey = re.sub(r'^(k_)?(%s_)?' % class_name, '', ikey)
            attrs[ikey] = ivalue

            if ikey[0:1].isdigit() or ikey in kwlist:
                attrs_starting_with_number = True

        classes[class_name] = attrs, attrs_starting_with_number

# Generate print out

print("from enum import IntEnum")

for class_name, (attrs, attrs_starting_with_number) in sorted(classes.items(), key=lambda x: x[0].lower()):
        if attrs_starting_with_number:
            print("\n%s = IntEnum(%r, {" % (class_name, class_name))
            for ikey, ivalue in attrs.items():
                print("    %r: %r," % (ikey, ivalue))
            print("    })")
        else:
            print("\nclass {class_name}(IntEnum):".format(class_name=class_name))
            for ikey, ivalue in sorted(attrs.items(), key=lambda y: y[1]):
                print("    {} = {}".format(ikey, ivalue))

print("\n__all__ = [")

for class_name in sorted(classes, key=lambda x: x.lower()):
    print("    %r," % class_name)

print("    ]")
