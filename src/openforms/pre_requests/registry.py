from openforms.plugins.registry import BaseRegistry

from .base import PreRequestHookBase


class Registry(BaseRegistry[PreRequestHookBase]):
    """
    A registry for pre-request hooks.
    """

    module = "pre_requests"


# Sentinel to provide the default registry. You can easily instantiate another
# :class:`Registry` object to use as dependency injection in tests.
register = Registry()
