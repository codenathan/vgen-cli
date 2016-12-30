from .base import Base
from vgen.templates import mapping
from vgen.core import helpers
from os import path


class Create(Base):
    def __init__(self, options, *args, **kwargs):
            super(Create, self).__init__(options, *args, **kwargs)

            self.host = self.options['HOST']
            self.slug = helpers.slugify(self.host)
            self.web_server = self.config.get('WEB_SERVER')
            self.operating_system = self.config.get('OPERATING_SYSTEM')
            self.dev_env = self.config.get('DEV_ENVIRONMENT')
            self.web_server_version = self.config.get('WEB_SERVER_VERSION')
            self.doc_path = path.join(self.config.get('DOCUMENT_ROOT'), self.slug)
            self.public_path = path.join(self.doc_path, 'public')

            self.template = getattr(mapping, self.web_server)[self.web_server_version](self.__dict__)

    def run(self):

        helpers.mkdir(self.doc_path, self.public_path)

        template_string = self.template.get_template()

        print template_string
