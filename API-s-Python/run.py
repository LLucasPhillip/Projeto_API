import os
from config import db, create_app  # Importando o db e a função create_app do config
from app.routes.aluno_routes import aluno_bp  # Certifique-se de que os nomes estão corretos
from app.routes.professor_routes import professor_bp
from app.routes.turma_routes import turma_bp

# Criação da aplicação Flask
app = create_app()

# Registro dos blueprints
app.register_blueprint(aluno_bp, url_prefix='/alunos')
app.register_blueprint(professor_bp, url_prefix='/professores')
app.register_blueprint(turma_bp, url_prefix='/turmas')

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()  # Cria todas as tabelas definidas nos modelos

# Execução da aplicação
if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
