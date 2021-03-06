from .terminal_commands import TerminalCommands


class ServerCommands(TerminalCommands):

    def start_server(self):
        raise NotImplementedError('You must specify the command to start the web server')

    def stop_server(self):
        raise NotImplementedError('You must specify the command to stop the web server')

    def restart_server(self):
        raise NotImplementedError('You must specify the command to restart the web server')