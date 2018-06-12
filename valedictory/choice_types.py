from .base import BaseValidator
from .exceptions import ValidatorException


__all__ = ["Choice"]


class Choice(BaseValidator):
    def __init__(self, *choices, **kwargs):
        super(Choice, self).__init__(**kwargs)
        self.validator_choices = tuple(c for c in choices if isinstance(c, BaseValidator))
        self.static_choices = tuple(c for c in choices if c not in self.validator_choices)

    def __call__(self, instance):
        if instance in self.static_choices:
            return instance

        for choice in self.validator_choices:
            try:
                return choice(instance)
            except ValidatorException:
                continue
        self._raise(msg="No valid choice")
