from vgen.core.template import Template


class TwoPointFour(Template):

    def get_template(self):

        self.template = """
<VirtualHost *:80>
    ServerName {domain_name}
    ServerAdmin {admin}

    DocumentRoot {public_directory}

    <Directory "{public_directory}">
        AllowOverride All
        Order allow,deny
    </Directory>

    LogLevel warn
    ErrorLog {log_path}/{domain_slug}_error.log
    CustomLog {log_path}/{domain_slug}_access.log combined
</VirtualHost>
""".format(domain_name=self.setup['host'], public_directory=self.setup['public_path'],
           domain_slug=self.setup['slug'], log_path=self.log_path, ip=self.ip, port=self.port)
        return self.template
