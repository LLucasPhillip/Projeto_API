from flask import Blueprint

# Importa os blueprints de cada módulo
from .aluno_routes import aluno_bp  # Corrija o nome se necessário
from .professor_routes import professor_bp
from .turma_routes import turma_bp

# Cria um blueprint principal para registrar os outros blueprints
main_blueprint = Blueprint('main', __name__)

# Registra os blueprints
main_blueprint.register_blueprint(aluno_bp, url_prefix='/alunos')  # Adiciona o prefixo, se desejado
main_blueprint.register_blueprint(professor_bp, url_prefix='/professores')
main_blueprint.register_blueprint(turma_bp, url_prefix='/turmas')

# Define uma função para registrar o blueprint no aplicativo Flask
def init_app(app):
    app.register_blueprint(main_blueprint)
