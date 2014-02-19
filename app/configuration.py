# -*- encoding: utf-8 -*-
"""
Python Application Template
Licence: GPLv3
"""


class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    BOOTSTRAP_FONTAWESOME = True
    SECRET_KEY = "AAAFcWVy_hkiululGrty.h_EnOCsNZc"
    CSRF_ENABLED = True

#Get your reCaptche key on: https://www.google.com/recaptcha/admin/create
#RECAPTCHA_PUBLIC_KEY = "6LffFNwSAAAAAFcWVy__EnOCsNZcG2fVHFjTBvRP"
#RECAPTCHA_PRIVATE_KEY = "6LffFNwSAAAAAO7UURCGI7qQ811SOSZlgU69rvv7"


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
