from .base import BaseValidator


__all__ = ["List"]


class List(BaseValidator):
    def __init__(self, element_type, **kwargs):
        super(List, self).__init__(**kwargs)
        self.element_type = element_type

    def __call__(self, instance):
        if not isinstance(instance, (list, tuple)):
            self._raise()
        return [self.element_type(ele) for ele in instance]
