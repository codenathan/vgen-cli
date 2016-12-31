from .base import Base
from vgen.templates import mapping as template_mapping
from vgen.core.helpers import *
from vgen.scripts import packages
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
            self.template = getattr(template_mapping, self.web_server)[self.web_server_version](self.__dict__)
            self.package = None
            self.check_if_package()

    def run(self):

        make_directories(self.doc_path, self.public_path)
        template_string = self.template.render_template()

        self.filename = self.create_config_file(template_string)
        print 'Created Vhost file for  %s : %r' % (self.host, self.filename)

        self.run_as_root()  # we now need permission to update permissions
        self.update_host_files()
        self.update_folder_permissions()

        self.server.restart_server()

        print 'VGen Finished'

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

    def update_host_files(self):
        ip = '127.0.0.1'
        if self.dev_env is not None:
            config_ip = self.config.get('IP_ADDRESS')
            if config_ip is not '*':
                ip = config_ip
        self.host_files.update(ip, self.host)

    def update_folder_permissions(self):

        if self.dev_env is not None and self.operating_system is not 'Windows':
            user = self.user
        elif self.operating_system is not 'Windows':
            user = self.root
        else:
            return False

        change_directory_owner_recursively(self.doc_path, user)

    def check_if_package(self):
        package = self.options['--pkg']

        if package is not None:
            if package in self.defaults.PACKAGES:
                self.package = package
                self.setup_package()
            else:
                raise AttributeError('The package %r is not available' % package)

    def setup_package(self):
        package = getattr(packages, self.package.title())()
        package.install_package(self.config.get('DOCUMENT_ROOT'), self.slug)
