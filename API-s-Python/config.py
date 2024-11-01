# config.py

import os

# Caminho base do projeto para facilitar o acesso ao diretório
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configurações gerais para todos os ambientes."""
    HOST = '0.0.0.0'
    PORT = 8000
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'minha_chave_secreta_padrao')  # Segurança para cookies e sessões
    SESSION_COOKIE_SECURE = True  # Para HTTPS em produção
    CSRF_ENABLED = True  # Proteção contra CSRF


class DevelopmentConfig(Config):
    """Configurações específicas para o ambiente de desenvolvimento."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'dev.db')}"


class TestingConfig(Config):
    """Configurações específicas para o ambiente de teste."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'test.db')}"
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False  # Para evitar erro de contexto em testes


class ProductionConfig(Config):
    """Configurações específicas para o ambiente de produção."""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")
    SESSION_COOKIE_SECURE = True  # Exige HTTPS
    DEBUG = False
    CSRF_ENABLED = True


# Dicionário para mapear as configurações pelos ambientes
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
