from .base import BaseValidator


__all__ = ["Dict"]


class _NamedDict(dict):

    def __getattribute__(self, name):
        try:
            return self[name]
        except KeyError:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (type(self).__name__, name))

    def __setattr__(self, name, value):
        self[name] = value


class Dict(BaseValidator):
    def __init__(self, **kwargs):
        node = kwargs.pop("node", "")
        super(Dict, self).__init__(node=node)
        self.key_value_types = kwargs

    def __call__(self, instance):
        if not isinstance(instance, dict):
            self._raise()
        out_dict = _NamedDict()
        for key, val in instance.items():
            value_type = self.key_value_types.get(key, None)
            if not value_type:
                self._raise(msg="Unknown key")
            out_dict[key] = value_type(val)
        return out_dict
