from .exceptions import ValidatorException

class BaseValidator(object):
    def __init__(self, node=""):
        self.__name = node

    @property
    def node(self):
        return self.__name

    def __call__(self, instance):
        raise NotImplemented

    def _raise(self, instance=None, msg=None):
        raise ValidatorException(msg)
