import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta_padrao')  # Segurança para cookies e sessões!!!
    SESSION_COOKIE_SECURE = True 
    CSRF_ENABLED = True  # Proteção contra CSR

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'dev.db')}"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
    SESSION_COOKIE_SECURE = True  # Exige HTTPS
    DEBUG = False
    CSRF_ENABLED = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
