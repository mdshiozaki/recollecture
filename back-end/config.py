import os

# You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
# SQLALCHEMY_DATABASE_URI = "C:/Users/Brandon/Documents/Brandon/University of Waterloo/4A Term/project/test.db"
SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"