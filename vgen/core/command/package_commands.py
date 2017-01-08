from vgen.core.helpers.helpers_package import *
from vgen.config import CHECK_PREREQUISITES
from vgen.core.expection import *
from .terminal_commands import TerminalCommands


class PackageCommands(TerminalCommands):

    def __init__(self):
        self.repo = None
        self.prerequisites = {}
        """
            :param public_folder
           True if default is public
           False for document root
           string if other folder
        """
        self.public_folder = True

    def install_package(self, directory, name):
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
                if value is False:
                    print 'Package %s not installed ' % attr
                    is_false = True

            if is_false is True:
                raise ImproperlyConfigured('You do not have the required package prerequisites installed : '
                                           '\n %r ' % results)

    def set_public_folder(self):
        raise NotImplementedError('You must specify what the public folder for this package is')

    def return_public_folder(self):
        return self.public_folder



