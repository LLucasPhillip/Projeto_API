from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.controllers.professor_controller import (
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor,
    criar_professor  # Supondo que essa função seja usada para criar um professor diretamente
)

# Criação do blueprint para professores
professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/', methods=["GET"])
def main():
    return 'Rotas para professor'

# Rota para criar um professor (via formulário)
@professor_blueprint.route('/professores/adicionar', methods=['GET'])
def adicionar_professor_page():
    return render_template('criarProfessores.html')

@professor_blueprint.route('/professores', methods=['POST'])
def create_professor():
    # Se você quiser criar um professor a partir do formulário
    data = request.form
    adicionar_professor(data)
    return redirect(url_for('professor.get_professores'))

# Rota para criar um professor (API)
@professor_blueprint.route('/professores/criar', methods=['POST'])
def criar_prof():
    return criar_professor()

@professor_blueprint.route('/professores', methods=['GET'])
def get_professores():
    professores = listar_professores()
    return render_template("professores.html", professores=professores)

@professor_blueprint.route('/professores/<int:id_professor>', methods=['GET'])
def get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor_id.html', professor=professor)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@professor_blueprint.route('/professores/<int:id_professor>/editar', methods=['GET'])
def editar_professor_page(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return render_template('professor_update.html', professor=professor)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

@professor_blueprint.route('/professores/<int:id_professor>', methods=['POST'])
def update_professor(id_professor):
    data = request.form
    atualizar_professor(id_professor, data)
    return redirect(url_for('professor.get_professor', id_professor=id_professor))

@professor_blueprint.route('/professores/delete/<int:id_professor>', methods=['POST'])
def delete_professor(id_professor):
    excluir_professor(id_professor)
    return redirect(url_for('professor.get_professores'))

# Rota para API - Listar todos os professores
@professor_blueprint.route('/api/professores', methods=['GET'])
def api_get_professores():
    return jsonify(listar_professores())

# Rota para API - Obter um professor por ID
@professor_blueprint.route('/api/professores/<int:id_professor>', methods=['GET'])
def api_get_professor(id_professor):
    try:
        professor = professor_por_id(id_professor)
        return jsonify(professor)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

# Rota para API - Criar um novo professor
@professor_blueprint.route('/api/professores', methods=['POST'])
def api_create_professor():
    data = request.json
    adicionar_professor(data)
    return jsonify(data), 201

# Rota para API - Atualizar um professor
@professor_blueprint.route('/api/professores/<int:id_professor>', methods=['PUT'])
def api_update_professor(id_professor):
    data = request.json
    atualizar_professor(id_professor, data)
    return jsonify(professor_por_id(id_professor))

# Rota para API - Deletar um professor
@professor_blueprint.route('/api/professores/<int:id_professor>', methods=['DELETE'])
def api_delete_professor(id_professor):
    excluir_professor(id_professor)
    return '', 204

##