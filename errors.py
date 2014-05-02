# -*- coding: utf-8 -*-

class ConfigurationError(Exception):
    pass

class ItemIDMismatch(Exception):
    pass

class PermissionError(Exception):
    pass

class UnknownError(Exception):
    pass

class ItemNotFoundError(Exception):
    pass

class BadTokenError(Exception):
    pass

class SaveFailedError(Exception):
    pass     

class NoSuchEntityIdError(Exception): 
    pass

class FailSavedError(Exception):
    pass
