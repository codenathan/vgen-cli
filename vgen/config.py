# Required Configurations

OPERATING_SYSTEM = 'mac'  # mac | windows | ubuntu | centos
PATH_ENABLED = '/Applications/MAMP/conf/apache/vhosts'  # Path enabled to .conf files include
DOCUMENT_ROOT = '/Users/admin/Code'  # where all web document roots will go
WEB_SERVER = 'apache'  # apache | ngnix
WEB_SERVER_VERSION = 2.2  # 2.2 | 2.4
PORT = 80
IP_ADDRESS = '*'

# Optional Configurations

DISABLE_EXT = '.bak'  # when host disabled if PATH_DISABLE is NONE all files will be suffixed with this ext
PATH_DISABLE = None  # Path disable to .conf files
DEV_ENVIRONMENT = 'mamp'  # None | mamp | xampp | homestead
ARCHIVE_DOCS = None  # path to move archived sites to archive folder
LOGS_PATH = '/Users/admin/Code/errors'  # required if APACHE_LOG_DIR is not defined
