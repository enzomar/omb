class Config(object):
    DEBUG = True
    MYSQL_DATABASE_USER = 'webserver'
    MYSQL_DATABASE_PASSWORD = 'webserver'
    MYSQL_DATABASE_DB = 'easycontainer' 
    MYSQL_DATABASE_HOST = "127.0.0.1"   
    

class PRDConfig(Config): 
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    MYSQL_DATABASE_HOST = "mysql"   

class LOCALConfig(Config):
    DEBUG = True    
    SESSION_COOKIE_SECURE = False
    MYSQL_DATABASE_HOST = "mysql"   

