class FrameworkCommands(object):

    def get_code(self):
        raise NotImplementedError('You must specify on how we must retrieve the code')

    def after_download(self):
        raise NotImplementedError('You must specify the command to stop the web server')

