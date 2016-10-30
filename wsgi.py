#!/usr/bin/python
import os

if 'OPENSHIFT_APP_NAME' in os.environ:              #are we on OPENSHIFT?
    ip = os.environ['OPENSHIFT_PYTHON_IP']
    port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
else:
    ip = '0.0.0.0'                            #localhost
    port = 8051


from flaskapp import app as application
