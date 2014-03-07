import os
gettext = lambda s: s

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
PROGRAM = 'python'
PRODUCT = 'vFense'
AGENT_PRODUCT = 'vFense Agent'
RUNASUSER = 'toppatch'

###########################################
# Configuration and source files
###########################################
ROOT = '/usr/local'
ROOT_ETC = os.path.join(ROOT, 'etc/%s' %(PRODUCT))
ROOT_ETC_SCHED = os.path.join(ROOT_ETC, 'scheduler')
ROOT_BIN = os.path.join(ROOT, 'bin/%s' %(PRODUCT))
ROOT_LIB = os.path.join(ROOT, 'lib/%s' %(PRODUCT))
ROOT_SRC = os.path.join(ROOT, 'src/%s' %(PRODUCT))
ROOT_LOG = '/var/log/%s' % (PRODUCT)
ROOT_SRC_PATCHES = os.path.join(ROOT_SRC, 'patches')
ROOT_PLUGINS = os.path.join(ROOT_SRC, 'plugins')
RECEIVER_DIR = os.path.join(ROOT_SRC, 'receiver')
RVSCHEDULER = os.path.join(ROOT_SRC, 'scheduler/rvscheduler.py')

DB_CONFIG_FILE = os.path.join(ROOT_ETC, 'database.conf')
EMAIL_TEMPLATES = os.path.join(ROOT_ETC, 'emailer/templates')


###########################################
# PIDs
###########################################
ROOT_RUN = '/run/%s' %(PRODUCT)
PIDFILE = os.path.join(ROOT_RUN, '%s.pid' % (PRODUCT))
RVSCHEDULER_PIDFILE = os.path.join(ROOT_RUN, 'rvscheduler-9002.pid')

###########################################
# Patch and CVE directories
###########################################
ROOT_PKG_CACHE = '/var/cache/%s/packages' % (PRODUCT)
ROOT_PLUGINS_CVE_XLS = os.path.join(ROOT_PLUGINS, 'cve/data/xls')
ROOT_PLUGINS_CVE_XML = os.path.join(ROOT_PLUGINS, 'cve/data/xml')
ROOT_PLUGINS_CVE_UBUNTU = os.path.join(ROOT_PLUGINS, 'cve/data/html/ubuntu')

############################################
# Agent settings
############################################
AGENT_PIDFILE = os.path.join(ROOT_RUN, 'TopPatchAgent.pid')
AGENT_SRC = os.path.join(ROOT_SRC, 'agent')
AGENT_BIN = os.path.join(AGENT_SRC, 'agent.py')

############################################
# TMP
############################################
ROOT_TMP = '/tmp/%s' % (PRODUCT)
ROOT_TMP_PKG = os.path.join(ROOT_TMP, 'packages')

###########################################
# systemd
###########################################
INIT_SCRIPT_SRC = os.path.join(ROOT_SRC, 'daemon/%s' % (PRODUCT))
INIT_SCRIPT_DST = '/etc/init.d/%s' % (PRODUCT)

###########################################
# RethinkDB paths
###########################################
RETHINK_PATH = '/usr/share/rethinkdb'
RETHINK_USER = 'rethinkdb'
RETHINK_GROUP = 'rethinkdb'
RETHINK_DB_SERVER = '%s_server' % (PRODUCT)
RETHINK_INSTANCES_PATH = '/etc/rethinkdb/instances.d'
RETHINK_VFENSE_ROOT = '/var/lib/rethinkdb/%s' % (PRODUCT)
RETHINK_VFENSE_ROOT_DATA = os.path.join(RETHINK_VFENSE_ROOT, 'data')
RETHINK_SOURCE_CONF = os.path.join(ROOT_ETC, 'rethinkdb_%s.conf', % (PRODUCT))
RETHINK_CONF = '/etc/rethinkdb/instances.d/%s.conf' % (PRODUCT)
RETHINK_WEB = '/usr/share/rethinkdb/web'
RETHINK_PID_FILE = '/var/run/rethinkdb/%s/pid_file' % (PRODUCT)

###########################################
# nginx paths
###########################################
NGINX_CONFIG = '/etc/nginx/sites-available/%s.conf' % (PRODUCT)
NGINX_CONFIG_ENABLED = '/etc/nginx/sites-enabled/%s' % (PRODUCT)

class Default():
    Customer = 'default'
    User = 'system'
