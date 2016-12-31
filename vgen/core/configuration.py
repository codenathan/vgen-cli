import vgen.config as config   # import default config file
import conf_validator as validator
from expection import ImproperlyConfigured, FieldDoesNotExist


class Configuration(object):
    """ Configuration Service to handle all config process """

    @staticmethod
    def config_exists(attr):
        """ Checks if the attribute exists within the config.py file"""
        try:
            return getattr(config, attr)
        except AttributeError:
            raise ImproperlyConfigured("'%s' is not configured please configure config.py ." % attr)

    def get(self, attr):
        return self.config_exists(attr)

    @staticmethod
    def is_valid(attr):
        """ Checks if the config attribute is valid """
        current_attr_value = getattr(config, attr)  # get current value

        if hasattr(validator, attr):

            default_attr_values = getattr(validator, attr)  # get default values

            if isinstance(default_attr_values, tuple):

                if ((attr in validator.REQUIRED and current_attr_value not in default_attr_values) or
                        (attr in validator.NOT_REQUIRED and current_attr_value is not None and current_attr_value not in default_attr_values)):
                    """ Validate all lists"""
                    raise ImproperlyConfigured('%s : %s must be one of %r' %
                                               (attr, current_attr_value, default_attr_values))
            return True

        elif attr in validator.PATH:

            if (attr in validator.REQUIRED) or (attr in validator.NOT_REQUIRED and current_attr_value is not None):
                """ validate path files """
                import os
                if not os.path.exists(current_attr_value):
                    raise ImproperlyConfigured('no such directory: %r' % current_attr_value)

            return True
        elif attr in validator.VARIABLE:
            if attr in validator.REQUIRED and current_attr_value is None:
                raise ImproperlyConfigured('You need to specify a value for: %s' % attr)
            return True
        elif attr in validator.BOOLEAN:
            if current_attr_value is not isinstance(current_attr_value, bool):
                raise ImproperlyConfigured('You must specify a boolean value for %' % attr)
            return True
        else:
            raise FieldDoesNotExist('%r is not a valid in config' % attr)


