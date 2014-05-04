# -*- coding: utf-8 -*-

from item import Item # So that wikidata.Item can be used.

from configReader import Config
from api import API

import errors

def start(configFile, Text=True):
    config = Config(configFile)
    if not config["api"]:
       raise errors.ConfigurationError("An API url needs to be defined in config.py")

    return API(config)

# There 2 ways of accessing config file
# - using a python script ( not recommended as of python 3.0 )
# - using a property file
# if you want to start configuration using a python script 
# use : 
#    api = start('config.py')
# if you want to start configuration using config.properties use 
#    api = start('config.properties', True)

# api = start('config.py') # disabled now
api =  start('pywikidata_config.properties', True)

#warning
# if you use script file, path searh is python sys.path
# if you use text, path search is current dir

