from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.join(path.dirname(__file__), ''))
load_dotenv()


class Config:
    APP_NAME = environ.get('APP_NAME')
    API_KEY = environ.get('API_KEY')
    SECRET_KEY = environ.get('API_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URI') \
        or 'sqlite:///' + path.join(basedir, 'db/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    server_ip = "127.0.0.1"
    server_port = "7070"
    flask_debug = True

    # TODO
    # update the code to use config parser and a config file
    # https://docs.python.org/3/library/configparser.html

    # TODO
    # create class setter and getter values for config specifics
    # set a config value, then update the config file

# class Development(Config):
#     ''' Development config. '''
#
#     DEBUG = True
#     ENV = 'dev'
#
#
# class Staging(Config):
#     ''' Staging config. '''
#
#     DEBUG = True
#     ENV = 'staging'
#
#
# class Production(Config):
#     ''' Production config '''
#
#     DEBUG = False
#     ENV = 'production'
#
#
# config = {
#     'development': Development,
#     'staging': Staging,
#     'production': Production,
# }
