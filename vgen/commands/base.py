from vgen.core import Configuration
from vgen.core import defaults
from vgen.core.expection import *
from vgen.core.helpers import *
from vgen.services import hostfileupdate
from os import getlogin
from getpass import getuser
from platform import system
import subprocess


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
        # self.is_running_as_root()
        self.user = None
        self.root = None
        self.set_users()
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

    def set_users(self):
        self.user = getlogin()
        self.root = getuser()

    @staticmethod
    def run_as_root():
        if system() is not 'Windows' and not check_if_running_as_administrator():

            print 'We need to run as root to update permissions '
            try:
                subprocess.call(['sudo su'], shell=True)
            except KeyboardInterrupt:
                print '\nCould not continue as root permission is required'
                exit()