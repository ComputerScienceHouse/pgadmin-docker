#!/bin/bash
# pgAdmin Runner for Docker
# Author: Steven Mirabito (smirabito@csh.rit.edu)

cd /usr/lib/python2.7/site-packages/pgadmin4-web

if [ ! -f ~/.pgadmin/pgadmin4.db ]; then
    echo "---> Performing first time setup..."
    python setup.py
fi

echo "---> Starting pgAdmin..."
gunicorn --chdir=/usr/lib/python2.7/site-packages/pgadmin4-web --workers=${PGADMIN_WORKERS:-4} --bind ${PGADMIN_SERVER_IP:-0.0.0.0}:${PGADMIN_SERVER_PORT:-8080} pgAdmin4:app

