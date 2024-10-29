from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .routes.professor_routes import professor_bp
    from .routes.turma_routes import turma_bp
    from .routes.aluno_routes import aluno_bp

    app.register_blueprint(professor_bp, url_prefix='/professores')
    app.register_blueprint(turma_bp, url_prefix='/turmas')
    app.register_blueprint(aluno_bp, url_prefix='/alunos')

    with app.app_context():
        db.create_all()

    return app
