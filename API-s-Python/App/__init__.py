from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import logging
from logging.handlers import RotatingFileHandler
import os

# BDD
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Carrega a configuração do ambiente
    app.config.from_object(config[config_name])
    
    # Inicialização de extensões
    db.init_app(app)
    migrate.init_app(app, db)

    configure_logging(app)
    
    register_blueprints(app)

    register_error_handlers(app)

    # Inicializa o banco de dados no primeiro contexto de aplicação
    with app.app_context():
        db.create_all() 

    return app

def register_blueprints(app):
    from .routes.professor_routes import professor_bp
    from .routes.turma_routes import turma_bp
    from .routes.aluno_routes import aluno_bp

    app.register_blueprint(professor_bp, url_prefix='/professores')
    app.register_blueprint(turma_bp, url_prefix='/turmas')
    app.register_blueprint(aluno_bp, url_prefix='/alunos')

def configure_logging(app):
    if not app.debug:
        log_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'logs')
        os.makedirs(log_dir, exist_ok=True)  # Cria o diretório de logs se não existir
        
        file_handler = RotatingFileHandler(os.path.join(log_dir, 'app.log'), maxBytes=10240, backupCount=10)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('Application startup')

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found", "message": "Rota não encontrada"}), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return jsonify({"error": "Internal Server Error", "message": "Erro no servidor"}), 500

    @app.errorhandler(400)
    def bad_request_error(error):
        return jsonify({"error": "Bad Request", "message": "Requisição inválida"}), 400

    @app.errorhandler(405)
    def method_not_allowed_error(error):
        return jsonify({"error": "Method Not Allowed", "message": "Método HTTP não permitido"}), 405
