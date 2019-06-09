import os,logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCOUNT_DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'username': None,
    'password': None,
    'path': "%s/db" % BASE_DIR
}

BASE_DATABASE = {
    'engine': 'file_storage',
    'name': 'base',
    'username': None,
    'password': None,
    'path': "%s/db" % BASE_DIR
}

DEFAULT_ADMIN_ACCOUNT = 'admin'
DEFAULT_ADMIN_PASSWORD = 'admin'

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'access': 'access.log',
}
