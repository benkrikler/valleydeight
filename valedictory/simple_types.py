from .base import BaseValidator
import six


__all__ = ["Str", "Int", "Bool", "Float"]



class SimpleType(BaseValidator):
    def __init__(self, **kwargs):
        super(SimpleType, self).__init__(**kwargs)

    def __call__(self, instance):
        if not isinstance(instance, self.class_type):
            self._raise()
        return instance


class Str(SimpleType):
    class_type = six.string_types


class Int(SimpleType):
    class_type = int


class Bool(SimpleType):
    class_type = bool


class Float(SimpleType):
    class_type = float
