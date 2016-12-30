class Template(object):
    def __init__(self, *args):
        self.template = ''
        self.setup = args[0]

    def get_template(self):
        raise NotImplementedError('You must implement a template string for every template')

    def render_template(self):
        return self.get_template().strip()
