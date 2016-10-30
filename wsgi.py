#!/usr/bin/python
import os
import sys

sys.path.insert(0, os.path.dirname(__file__) or '.')

PY_DIR = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], "python")

virtenv = PY_DIR + '/virtenv/'

PY_CACHE = os.path.join(virtenv,
                        'lib',
                        os.environ['OPENSHIFT_PYTHON_VERSION'],
                        'site-packages')

os.environ['PYTHON_EGG_CACHE'] = os.path.join(PY_CACHE)
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')

try:
    exec(open(virtualenv).read(), dict(__file__=virtualenv))
except IOError:
    pass
    
from spex import app as application

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#
