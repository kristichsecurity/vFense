import os
gettext = lambda s: s

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
ROOT = '/usr/local'
ROOT_ETC = os.path.join(ROOT, 'etc/vfense')
ROOT_BIN = os.path.join(ROOT, 'bin/vfense')
ROOT_LIB = os.path.join(ROOT, 'lib/vfense')
ROOT_SRC = os.path.join(ROOT, 'src/vfense')
ROOT_SRC_PATCHES = os.path.join(ROOT_SRC, 'patches')
ROOT_RUN = '/run/vfense'
ROOT_LOG = '/var/log/vfense'
ROOT_PKG_CACHE = '/var/cache/vfense/packages'
ROOT_TMP = '/tmp/vfense'
ROOT_TMP_PKG = os.path.join(ROOT_TMP, 'packages')
RETHINK_PATH = '/usr/share/rethinkdb'
RETHINK_USER = 'rethinkdb'
RETHINK_INSTANCES_PATH = '/etc/rethinkdb/instances.d'
RETHINK_VFENSE_ROOT = '/var/lib/rethinkdb/vFense'
RETHINK_VFENSE_ROOT_DATA = os.path.join(RETHINK_VFENSE_ROOT, 'data')
RETHINK_SOURCE_CONF = os.path.join(ROOT_ETC, 'rethinkdb_vFense.conf')

RETHINK_CONF = '/etc/rethinkdb/instances.d/vFense.conf'
RETHINK_WEB = '/usr/share/rethinkdb/web'
RETHINK_PID_FILE = '/var/run/rethinkdb/vFense/pid_file'

NGINX_CONFIG = '/etc/nginx/sites-available/vFense.conf'
NGINX_CONFIG_ENABLED = '/etc/nginx/sites-enabled/vFense.conf'

class Default():
    Customer = 'default'
    User = 'system'
