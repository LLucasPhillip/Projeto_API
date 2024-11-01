import os
from config import app, db
from app.routes.alunos_routes import alunos_blueprint  # Ajuste o caminho se necessário
from app.routes.professor_routes import professor_blueprint  # Ajuste o caminho se necessário

# Registro dos blueprints
app.register_blueprint(alunos_blueprint)
# app.register_blueprint(professor_blueprint)  # Descomente se necessário

# Criação das tabelas no banco de dados
with app.app_context():
    db.create_all()

# Execução da aplicação
if __name__ == '__main__':
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])

    ##