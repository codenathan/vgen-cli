class PackageCommands(object):

    def __init__(self):
        self.repo = None
        self.prerequisites = None

    def get_code(self):
        raise NotImplementedError('You must specify on how we must retrieve the code')

    def after_download(self):
        raise NotImplementedError('You must specify the command to stop the web server')

    def check_prerequisites(self):
        raise NotImplementedError('You need to know whats required')

    def package_is_setup(self):
        raise NotImplementedError('You must specify a command to see if the package has been setup')

