from .base import Base
from vgen.templates import mapping
from vgen.core import helpers
import os


class Create(Base):

    def run(self):
        web_server = self.config.get('WEB_SERVER')
        operating_system = self.config.get('OPERATING_SYSTEM')
        dev_env = self.config.get('DEV_ENVIRONMENT')
        web_server_version = self.config.get('WEB_SERVER_VERSION')
        host = self.options['HOST']
        slug = helpers.slugify(host)

        doc_path = self.config.get('DOCUMENT_ROOT') + os.pathsep + slug
        public_path = doc_path + os.pathsep+'public'

        helpers.mkdir(doc_path)
        helpers.mkdir(public_path)

        template_file = getattr(mapping, web_server)[web_server_version]()

        template_string = template_file.get_template(host, slug, doc_path, public_path)

        print template_string
