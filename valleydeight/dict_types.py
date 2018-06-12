from .base import BaseValidator, Pass


__all__ = ["Dict"]


class _Namespace(dict):
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
        self.only_known_keys = True
        self.default_val_type = Pass()
        self.need_all_keys = False

    @property
    def options(self):
        return ("key_value_types", "only_known_keys", "default_val_type", "need_all_keys")

    def __call__(self, instance):
        if not isinstance(instance, dict):
            self._raise()

        out_dict = _Namespace()
        for key, val in instance.items():
            out_dict[key] = self._check_value(key, val)

        if self.need_all_keys:
            self._check_all_keys(out_dict)

        return out_dict

    def _check_value(self, key, val):
        value_type = self.key_value_types.get(key, None)
        if value_type:
            return value_type(val)

        if self.only_known_keys:
            self._raise(msg="Unknown key")

        return self.default_val_type(val)

    def _check_all_keys(self, out_dict):
        missing_keys = [k for k in self.key_value_types if k not in out_dict]
        if missing_keys:
            self._raise(msg="Missing keys")
