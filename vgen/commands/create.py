from .base import Base
from vgen.templates import mapping
from vgen.core.helpers import *
from os import path


class Create(Base):
    def __init__(self, options, *args, **kwargs):
            super(Create, self).__init__(options, *args, **kwargs)

            self.check_hostname()
            self.filename = None

            self.host = self.options['HOST']
            self.slug = slugify(self.host)
            self.web_server = self.config.get('WEB_SERVER')
            self.operating_system = self.config.get('OPERATING_SYSTEM')
            self.dev_env = self.config.get('DEV_ENVIRONMENT')
            self.web_server_version = self.config.get('WEB_SERVER_VERSION')
            self.doc_path = path.join(self.config.get('DOCUMENT_ROOT'), self.slug)
            self.public_path = path.join(self.doc_path, 'public')
            self.template = getattr(mapping, self.web_server)[self.web_server_version](self.__dict__)

    def run(self):
        make_directories(self.doc_path, self.public_path)
        template_string = self.template.render_template()

        self.filename = self.create_config_file(template_string)

        print 'Created Vhost file for  %s : %r' % (self.host, self.filename)

    def create_config_file(self, data):
        path_enabled = self.config.get('PATH_ENABLED')
        extension = self.defaults.CONF_EXT[self.web_server]

        filename = path.join(path_enabled, self.slug + extension)

        f = open(filename, "w+")
        f.write(data)
        f.close()

        return filename

    def check_hostname(self):
        hostname = self.options['HOST']
        if not check_if_hostname_is_valid(hostname):
            raise AttributeError('The hostname provided %r is not valid' % hostname)





