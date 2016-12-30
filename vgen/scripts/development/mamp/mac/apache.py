from vgen.core import ServerCommands


class Apache(ServerCommands):

    def restart_server(self):
        # TODO need to work on this its quiet buggy
        pass
        # self.run_command("open /Applications/MAMP/MAMP.app/")
        # self.stop_server()
        # self.start_server()

    def start_server(self):
        self.change_directory("/Applications/MAMP/bin")
        self.run_command("./startApache.sh")

    def stop_server(self):
        self.change_directory("/Applications/MAMP/bin")
        self.run_command("./stopApache.sh")
