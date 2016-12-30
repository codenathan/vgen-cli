from vgen.core import Configuration
from vgen.core import defaults

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
        self.set_server()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')

    def set_server(self):
        dev_env = self.config.get('DEV_ENVIRONMENT')
        web_server = self.config.get('WEB_SERVER')
        operating_system = self.config.get('OPERATING_SYSTEM')

        if dev_env is not None:
            self.server = importlib.import_module('vgen.scripts.development.'+dev_env+'.'+operating_system)
            self.server = getattr(self.server, operating_system.title())
        else:
            self.server = importlib.import_module('vgen.scripts.os.' + operating_system)
            self.server = getattr(self.server, web_server.title())