"""
vgen

Usage:
  vgen create HOST [--pkg=<package>]
  vgen archive HOST
  vgen -h | --help
  vgen --version

Arguments:
  HOST  fully qualified domain name

Options:
  -h --help                        Show this screen.
  --version                        Show version.
  --pkg=<package>                  Optional - framework/application to install i.e wordpress/laravel/codeigniter

Examples:
  vgen create stage.vgen.com
  vgen create dev.vgen.com --p=laravel --u=myusername -d
  vgen archive www.vgen.com


Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/codenathan/vgen-cli

"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as version


def main():
    """Main CLI entry point."""

    import commands
    options = docopt(__doc__, version=version)  # options returns all usage/options in array

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.

    for method_or_attr, is_active in options.iteritems():
        if hasattr(commands, method_or_attr) and is_active:  # checks if commands/__init__.py has methods / attributes
            module = getattr(commands, method_or_attr)  # gets the file for the found method
            commands = getmembers(module, isclass)  # returns all the class files associated to the file
            command = [command[1] for command in commands if command[0] != 'Base'][0]  # command[1] has class file path
            command = command(options)  # init class & pass through the options to the class
            command.run()  # call the run method on the command file
