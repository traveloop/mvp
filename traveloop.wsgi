#!/usr/bin/env python
import sys
import config

activate_this = config.BASE_URI + '/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
sys.path.insert(0, config.BASE_URI)

from traveloop import app as application
