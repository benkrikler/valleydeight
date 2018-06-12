from .base import BaseValidator


__all__ = ["Object"]


class Object(BaseValidator):
    def __init__(self, class_type, expand_dicts=True, expand_lists=True, args=None, **kwargs):
        super(BaseValidator, self).__init__(**kwargs)
        self.class_type = class_type
        self.expand_dicts = expand_dicts
        self.expand_lists = expand_lists
        self.args = args

    def __call__(self, instance):
        if self.args:
            instance = self.args(instance)

        if self.expand_dicts and isinstance(instance, dict):
            return self.class_type(**instance)
        if self.expand_lists and isinstance(instance, (tuple, list)):
            return self.class_type(*instance)
        return self.class_type(instance)
