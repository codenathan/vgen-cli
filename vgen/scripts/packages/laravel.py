from vgen.core.package_commands import PackageCommands
from vgen.core.helpers_package import *


class Laravel(PackageCommands):

    def __init__(self):
        super(Laravel, self).__init__()
        self.prerequisites = ('composeer', 'php')
        self.check_prerequisites()

    def check_prerequisites(self):
        for packages in self.prerequisites:
            print packages
            """
            if check_package(packages) is False:
                print 'Oh no %r :' % packages
            else:
                print 'Checked %s ' % packages
            """


