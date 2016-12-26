from vgen.templates.template import *


class TwoPointFour(Template):

    def get_template(self, host, slug, doc_path, public_dir):
        self.template = """
                    <VirtualHost *:80>
                        ServerName {domain_name}
                        ServerAdmin {admin}

                        DocumentRoot {document_path}

                        <Directory "{public_directory}">
                            AllowOverride All
                            Order allow,deny
                        </Directory>

                        LogLevel warn
                        ErrorLog ${APACHE_LOG_DIR}/{domain_slug}_error.log
                        CustomLog ${APACHE_LOG_DIR}/{domain_slug}_access.log combined
                    </VirtualHost>
                    """.format(domain_name=host, document_path=doc_path, public_directory=public_dir, domain_slug=slug)
        return self.template
