from vgen.core import Configuration
from vgen.core import defaults
from vgen.core.expection import *
from vgen.services import hostfileupdate

import importlib


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.config = Configuration()
        self.defaults = defaults
        self.server = None
        self.host_files = hostfileupdate
        self.set_server()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def set_server(self):

        dev_env = self.config.get('DEV_ENVIRONMENT')
        web_server = self.config.get('WEB_SERVER')
        operating_system = self.config.get('OPERATING_SYSTEM')

        try:

            if dev_env is not None:
                server = 'vgen.scripts.development.' + dev_env + '.' + operating_system
            else:
                server = 'vgen.scripts.os.' + operating_system

            module = importlib.import_module(server)

            self.server = getattr(module, web_server.title())()

        except:
            raise ImproperlyConfigured('Web Server could not be determined check configuration')


