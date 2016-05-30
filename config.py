import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'xd6\xc3\xfb0tw\x92\x9b\x81+?b\rn7D\x96n\x89\x7f\xf8\x969\xd3'
    
class ProductionConfig(Config):
    DEBUG = False
    
class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    
class TestingConfig(Config):
    TESTING = True
