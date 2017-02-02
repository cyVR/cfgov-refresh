from flags.utils import flags_enabled as utils_flag_enabled

from jinja2 import contextfunction


@contextfunction
def flag_enabled(context, key):
    request = None
    if context:
        request = context.get('request')
    return utils_flag_enabled(request, key)


@contextfunction
def flags_enabled(context, *keys):
    return all(flag_enabled(context, key) for key in keys)


@contextfunction
def flag_disabled(context, key):
    return not flag_enabled(context, key)
