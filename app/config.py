class Config():
    SECRET_KEY = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"
    SQLALCHEMY_DATABASE_URI = "sqlite:///base.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False

    #MAIL
    MAIL_SERVER = "mail.hosting.reg.ru"
    MAIL_PORT = 465
    MAIL_USERNAME = "info@sokt-profcom.ru"
    MAIL_PASSWORD = "sokt-profcom"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True