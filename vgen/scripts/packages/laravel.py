from vgen.core.command.package_commands import PackageCommands


class Laravel(PackageCommands):

    def __init__(self):
        super(Laravel, self).__init__()
        self.prerequisites = ('composer', 'php', 'laravel')
        self.check_prerequisites()

    def install_package(self, directory,name):
        self.change_directory(directory)
        self.run_command("laravel new "+name)
