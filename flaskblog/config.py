import os

class Config:
    SECRET_KEY = '7b83e908c8721541ff126d1f51e7d2aa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = 'shashiflaskwebapp@gmail.com'#os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = 'eqqrsljfagugcfoa'#os.environ.get('EMAIL_PASS')
