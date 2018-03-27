"""Generic settings and variables

The following settings and variables provide an idea of all the static configuration you might need in order to
setup a YellowAnt (YA) application in Python. You may need additional configuration for Python frameworks.
"""
import os

### database config ###
APP_DB_NAME = os.environ.get("APP_DB_NAME") # database name
APP_DB_USER = os.environ.get("APP_DB_USER") # database user
APP_DB_PASSWORD = os.environ.get("APP_DB_PASSWORD") # database password
APP_DB_HOST = os.environ.get("APP_DB_HOST") # database hostname

### YellowAnt App config ###
# Numerical ID generated when you register your application through the YA developer console
YA_APP_ID = os.environ.get("YA_APP_ID")
# Client ID generated from the YA developer console. Required to identify requests from this application to YA
YA_CLIENT_ID = os.environ.get("YA_CLIENT_ID")
# Client secret generated from the YA developer console. Required to identify requests from this application to YA
YA_CLIENT_SECRET = os.environ.get("YA_CLIENT_SECRET")
# Verification token generated from the YA developer console. This application can verify requests from YA as they will
# carry the verification token
YA_VERIFICATION_TOKEN = os.environ.get("YA_VERIFICATION_TOKEN")