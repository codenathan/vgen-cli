# current validation only on lists(tuples) and path

REQUIRED = ('OPERATING_SYSTEM', 'PATH_ENABLED', 'DOCUMENT_ROOT', 'WEB_SERVER', 'WEB_SERVER_VERSION')
NOT_REQUIRED = ('DISABLE_EXT', 'PATH_DISABLE', 'DEV_ENVIRONMENT', 'ARCHIVE_DOCS')

VARIABLE = ('WEB_SERVER_VERSION', 'DISABLE_EXT')
PATH = ('PATH_ENABLED', 'DOCUMENT_ROOT', 'PATH_DISABLE', 'ARCHIVE_DOCS')

OPERATING_SYSTEM = ('mac', 'windows', 'ubuntu', 'centos')
WEB_SERVER = ('apache', 'ngnix')
DEV_ENVIRONMENT = ('mamp', 'xampp', 'homestead')


