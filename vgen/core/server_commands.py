import os


class ServerCommands(object):

    def __init__(self):
        self.server_path = None

    def run_command(self,command):
        os.system(command)

    def change_directory(self,path):
        os.chdir(path)

    def get_server_path(self):
        raise NotImplementedError('You must specify on how to get the server path')

    def check_server(self):
        raise NotImplementedError('You must specify the command on how check if server has started')

    def start_server(self):
        raise NotImplementedError('You must specify the command to start the web server')

    def stop_server(self):
        raise NotImplementedError('You must specify the command to stop the web server')

    def restart_server(self):
        raise NotImplementedError('You must specify the command to restart the web server')

    def set_server_path(self):
        raise NotImplementedError('You must specify ways on how to set the server path')
