

class Template(object):

    def __init__(self):
        self.template = ''

    def get_template(self,*args):
        raise NotImplementedError('You must implement a template string for every template')
