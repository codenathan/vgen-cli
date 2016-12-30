from vgen.core import Configuration


class Template(object):
    def __init__(self, *args):
        self.template = ''
        self.setup = args[0]
        self.config = Configuration()
        self.ip = self.config.get('IP_ADDRESS')
        self.port = self.config.get('PORT')
        self.log_path = ''
        self.setup_log_path()

    def get_template(self):
        raise NotImplementedError('You must implement a template string for every template')

    def render_template(self):
        # TODO implement ways of automatically indenting template strings
        return self.get_template().strip()

    def setup_log_path(self):
        if self.config.get('LOGS_PATH') is not None:
            log_path = self.config.get('LOGS_PATH')
        else:
            log_path = '${{APACHE_LOG_DIR}}'

        self.log_path = log_path
