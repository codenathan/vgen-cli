import os

class TerminalCommands(object):
    @staticmethod
    def run_command(command):
        os.system(command)

    @staticmethod
    def change_directory(path):
        os.chdir(path)

    def move_up_one_directory(self,current_dir):
        parent_dir = os.path.abspath(current_dir)
        self.change_directory(parent_dir)


