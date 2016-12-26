from vgen.core import *


class Base(object):
    """A base command."""

    def __init__(self, options, *args, **kwargs):
        self.options = options
        self.args = args
        self.kwargs = kwargs
        self.config = Configuration()

    def run(self):
        raise NotImplementedError('You must implement the run() method yourself!')





