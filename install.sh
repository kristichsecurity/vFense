#!/bin/bash

PRODUCT="vFense"
AGENT_PRODUCT="${PRODUCT} Agent"
RUNASUSER="vfense"
SRC="$(pwd)/src"
CONF="$(pwd)/conf"
ROOT="/usr/local"
ROOT_ETC="${ROOT}/etc/${PRODUCT}"
ROOT_ETC_SCHED="${ROOT_ETC}/scheduler"
ROOT_BIN="${ROOT}/bin/${PRODUCT}"
ROOT_LIB="${ROOT}/lib/${PRODUCT}"
ROOT_LOG="/var/log/${PRODUCT}"
ROOT_SRC="${ROOT}/src/${PRODUCT}"
ROOT_RUN="/run/${PRODUCT}"
ROOT_CACHE="/var/cache/${PRODUCT}"
ROOT_SRC_PATCHES="${ROOT_SRC}/patches"
ROOT_SRC_PLUGINS="${ROOT_SRC}/plugins"
ROOT_SRC_RECEIVER="${ROOT_SRC}/receiver"
EMAIL_TEMPLATES="${ROOT_ETC}/emailer/templates"

# check if user exists
id $RUNASUSER > /dev/null 2>&1
OUT=$?
if [ $OUT -eq 1 ]; then
  adduser --disabled-password --gecos GECOS $RUNASUSER
fi

if [ ! -d '$ROOT_ETC' ]; then
  mkdir $ROOT_ETC
  mkdir $ROOT_ETC_SCHED

  cp "${CONF}/*" $ROOT_ETC
fi

if [ ! -d '$ROOT_BIN' ]; then
  mkdir $ROOT_BIN
fi

if [ ! -d '$ROOT_LIB' ]; then
  mkdir $ROOT_LIB
fi

if [ ! -d '$ROOT_RUN' ]; then
  mkdir $ROOT_RUN
fi

if [ ! -d '$ROOT_CACHE' ]; then
  mkdir $ROOT_CACHE
fi

if [ ! -d '$ROOT_SRC' ]; then
  mkdir $ROOT_SRC

  cp "${CONF}/patches/*" $ROOT_SRC_PATCHES
  cp -R "${SRC}/*" $ROOT_SRC
fi

if [ ! -d '$ROOT_LOG' ]; then
  mkdir $ROOT_LOG
fi

if [ ! -d '$EMAIL_TEMPLATES' ]; then
  mkdir $EMAIL_TEMPLATES
  cp "${SRC}/emailer/templates/*" $EMAIL_TEMPLATES
fi

sudo apt-get -qq update
echo "** Installing apt-add-repository"
sudo apt-get -y install python-software-properties curl pwgen
echo "** Adding chris-lea/redis-server ppa"
sudo apt-add-repository -y ppa:chris-lea/redis-server
echo "** Adding chris-lea/node.js ppa"
sudo apt-add-repository -y ppa:chris-lea/node.js
echo "** Adding rethinkdb ppa"
sudo add-apt-repository -y ppa:rethinkdb/ppa
echo "** Updating apt cache list"
sudo apt-get -y update
echo "** Installing vfense prerequisites"
sudo apt-get -y install \
                    python-setuptools \
                    python-pip \
                    python-lxml \
                    python-pycurl \
                    python-redis \
                    python-openssl \
                    python-tornado \
                    python-beautifulsoup \
                    python-roman \
                    python-bcrypt \
                    python-ipaddr \
                    python-tz \
                    python-urlgrabber \
                    python-netifaces \
                    redis-server \
                    nginx-extras \
                    python-jsonpickle \
                    openssh-server \
                    python-simplejson \
                    git-core \
                    g++ \
                    nodejs \
                    libprotobuf-dev \
                    libgoogle-perftools-dev \
                    libncurses5-dev \
                    libboost-all-dev

echo "** Installing rethinkdb prerequisites"
sudo apt-get install rethinkdb

echo "** Updating python setuptools"
curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | sudo python

echo "** Installing vfense python libraries"
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=cpp sudo pip install rq rethinkdb requests apscheduler tornado-redis xlrd

# # according to http://www.vfense.org/docs/installing-vfense-server/ the paths are hardcoded
# # so.. move it to the specific directory
# echo "** Moving /tmp/vfense-server to /top/TopPatch"
# sudo mv /tmp/vfense-server/* /opt/TopPatch/
# echo "** Changing directories to /opt/TopPatch"
# cd  /opt/TopPatch
# echo "** Linking TopPatch python source to dist-packages/vFense"
# sudo ln -s /opt/TopPatch/tp/src /usr/local/lib/python2.7/dist-packages/vFense
# HOSTNAME=`hostname`
# PASSWORD=`pwgen -1 -s 12`
# echo "** Starting initialize_vFense.py"
# echo ""
# echo "** The password that will be used is: ${PASSWORD}"
# echo "** Please make note of it and change it when you can"
# sudo python tp/src/scripts/initialize_vFense.py --dnsname="${HOSTNAME}" --password="${PASSWORD}"
# sudo service rethinkdb restart
# echo "** Starting nginx"
# sudo service nginx start
# echo "** Starting vFense"
# sudo /opt/TopPatch/tp/src/daemon/vFensed start
