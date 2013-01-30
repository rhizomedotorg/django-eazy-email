from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Context
from django.utils.importlib import import_module


def get_email_processors():
    processors = []
    collect = []
    collect.extend(settings.EAZY_EMAIL_CONTEXT_PROCESSORS)
    for path in collect:
        i = path.rfind('.')
        module, attr = path[:i], path[i+1:]
        try:
            mod = import_module(module)
        except ImportError, e:
            raise ImproperlyConfigured('Error importing eazy-email processor module %s: "%s"' % (module, e))
        try:
            func = getattr(mod, attr)
        except AttributeError:
            raise ImproperlyConfigured('Module "%s" does not define a "%s" callable eazy-email processor' % (module, attr))
        processors.append(func)
    return tuple(processors)

class EmailContext(Context):
    """
    This subclass of template.Context automatically populates itself using
    the processors defined in EAZY_EMAIL_CONTEXT_PROCESSORS.
    """
    def __init__(self, dict_=None):
        Context.__init__(self, dict_, current_app=None,
                use_l10n=None, use_tz=None)
        for processor in get_email_processors():
            self.update(processor())