#!/usr/bin/env python

from . import raw


class WrappedStruct(object):
    def __init__(self, struct_type, struct=None):
        self._struct_type = struct_type
        if struct is None:
            struct = self._struct_type()
        self.wrap(struct)

    def wrap(self, struct):
        for (n, t) in self._struct_type._fields_:
            setattr(self, n, getattr(struct, n))

    def unwrap(self):
        struct = self._struct_type()
        for (n, t) in self._struct_type._fields_:
            setattr(struct, n, getattr(self, n))
        return struct


class Format7Settings(WrappedStruct):
    def __init__(self, struct=None):
        WrappedStruct.__init__(self, raw.fc2Format7ImageSettings, struct)
        # TODO wrap mode? probably not

    def get_pixel_format(self):
        for k in raw.fc2PixelFormat:
            if raw.fc2PixelFormat[k] == self.pixelFormat:
                return k
        raise KeyError("Invalid pixel_format: %s" % self.pixelFormat)

    def set_pixel_format(self, pixel_format):
        if isinstance(pixel_format, (str, unicode)):
            if pixel_format not in raw.fc2PixelFormat:
                raise KeyError("Invalid pixel_format: %s" % pixel_format)
            pixel_format = raw.fc2PixelFormat[pixel_format]
        self.pixelFormat = pixel_format

