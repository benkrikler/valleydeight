from .exceptions import ValidatorException


__all__ = ["Pass"]


class BaseValidator(object):
    def __init__(self, node=""):
        self.__name = node

    @property
    def node(self):
        return self.__name

    @property
    def options(self):
        return tuple()

    def __call__(self, instance):
        raise NotImplementedError

    def _raise(self, instance=None, msg=None):
        raise ValidatorException(msg)

    def opt(self, option, value):
        if option not in self.options:
            raise KeyError("{} not an option for {} validators".format(option, type(self)))
        setattr(self, option, value)
        return self

    def opts(self, **kwargs):
        for k, v in kwargs.items():
            self.opt(k, v)
        return self


class Pass(BaseValidator):
    def __call__(self, instance):
        return instance
