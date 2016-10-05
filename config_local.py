import os
from logging import *

##########################################################################
# Application settings
##########################################################################

# Name of the application to display in the UI
APP_NAME = os.environ.get('PGADMIN_APP_NAME', 'pgAdmin 4')
APP_ICON = os.environ.get('PGADMIN_APP_ICON', 'icon-postgres-alt')

# Path to store persistant data, including the SQLite database
DATA_DIR = "/pgadmin-data"
STORAGE_DIR = os.path.join(DATA_DIR, 'storage')
SESSION_DB_PATH = os.path.join(DATA_DIR, 'sessions')
SQLITE_PATH = os.path.join(DATA_DIR, 'pgadmin4.db')
LOG_FILE = os.path.join(DATA_DIR, 'pgadmin4.log')

##########################################################################
# Server settings
##########################################################################

# The server mode determines whether or not we're running on a web server
# requiring user authentication, or desktop mode which uses an automatic
# default login.
#
# DO NOT DISABLE SERVER MODE IF RUNNING ON A WEBSERVER!!
SERVER_MODE = True

# This configuration otion allows the user to host the application on a LAN
# Default hosting is on localhost (DEFAULT_SERVER='localhost').
# To host pgAdmin4 over LAN set DEFAULT_SERVER='0.0.0.0' (or a specific
# adaptor address.
#
# NOTE: This is NOT recommended for production use, only for debugging
# or testing. Production installations should be run as a WSGI application
# behind Apache HTTPD.
DEFAULT_SERVER = os.environ.get('PGADMIN_SERVER_IP', '0.0.0.0')

# The default port on which the app server will listen if not set in the
# environment by the runtime
DEFAULT_SERVER_PORT = int(os.environ.get('PGADMIN_SERVER_PORT', '8080'))

# Enable CSRF protection?
CSRF_ENABLED = True

# Secret key for signing CSRF data. Override this in config_local.py if
# running on a web server
CSRF_SESSION_KEY = os.environ.get('PGADMIN_CSRF_SESSION_KEY', 'SuperSecret1')

# Secret key for signing cookies. Override this in config_local.py if
# running on a web server
SECRET_KEY = os.environ.get('PGADMIN_SECRET_KEY', 'SuperSecret2')

# Salt used when hashing passwords. Override this in config_local.py if
# running on a web server
SECURITY_PASSWORD_SALT = os.environ.get('PGADMIN_PASSWORD_SALT', 'SuperSecret3')

