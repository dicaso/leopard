# -*- coding: utf-8 -*-
"""Leopard configuration

This module organizes the configuration for leopard reporting.

"""

import configparser, os
configFileOptions = [
    'leopard.cfg', # in current working dir
    os.path.expanduser('~/.leopard.cfg'),
    '/usr/local/etc/leopard.cfg'
]

# Default configuration
config = configparser.ConfigParser()
config['leopard'] = {
    'reportdir': os.path.expanduser('~/Reports/'),
    'scriptdir': os.path.expanduser('~/Reports/scripts/'),
    'csvsep': ';',
    'csvdec': ','
}

# Read configuration file
for configFile in configFileOptions:
    if os.path.exists(configFile):
        config.read(configFile)
        break #only reads the first config file found
