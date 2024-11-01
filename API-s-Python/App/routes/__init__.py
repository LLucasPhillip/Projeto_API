from flask import Blueprint

# Importa os blueprints de cada módulo
from .aluno_routes import alunos_blueprint
from .professor_routes import professor_blueprint
from .turma_routes import turma_blueprint

# Cria um blueprint principal para registrar os outros blueprints
main_blueprint = Blueprint('main', __name__)

# Registra os blueprints
main_blueprint.register_blueprint(alunos_blueprint)
main_blueprint.register_blueprint(professor_blueprint)
main_blueprint.register_blueprint(turma_blueprint)

# Define uma função para registrar o blueprint no aplicativo Flask
def init_app(app):
    app.register_blueprint(main_blueprint)
