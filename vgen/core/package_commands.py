from .terminal_commands import TerminalCommands
from vgen.core.helpers_package import *
from vgen.core.expection import *
from vgen.config import CHECK_PREREQUISITES


class PackageCommands(TerminalCommands):

    def __init__(self):
        self.repo = None
        self.prerequisites = {}

    def install_package(self):
        raise NotImplementedError('You must specify on how we must retrieve the code')

    def after_download(self):
        raise NotImplementedError('You must specify the command to stop the web server')

    def check_prerequisites(self):
        if not CHECK_PREREQUISITES:
            print 'Skipping checking Checking Prerequisites'
            return True

        print 'Checking Prerequisites...'
        if not self.prerequisites:
            return True
        else:
            is_false = False
            results = check_packages(self.prerequisites)

            for attr, value in results.iteritems():
                if value is False :
                    print 'Package %s not installed ' % attr
                    is_false = True

            if is_false is True:
                raise ImproperlyConfigured('You do not have the required package prerequisites installed : \n %r ' % results)

    def package_is_setup(self):
        raise NotImplementedError('You must specify a command to see if the package has been setup')

