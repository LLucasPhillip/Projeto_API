from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.controllers.turma_controller import (
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma,
)

# Criação do blueprint para turmas
turma_blueprint = Blueprint('turma', __name__)

@turma_blueprint.route('/', methods=["GET"])
def main():
    return 'Rotas para turma'

# Rota para listar todas as turmas (Renderiza um template)
@turma_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return render_template("turmas.html", turmas=turmas)

# Rota para listar uma turma por ID (Renderiza um template)
@turma_blueprint.route('/turmas/<int:id_turma>', methods=['GET'])
def get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_id.html', turma=turma)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

# Rota para acessar o formulário de criação de uma nova turma
@turma_blueprint.route('/turmas/adicionar', methods=['GET'])
def adicionar_turma_page():
    return render_template('criarTurmas.html')

# Rota que cria uma nova turma (API, JSON response)
@turma_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.form
    adicionar_turma(data)
    return redirect(url_for('turma.get_turmas'))

# Rota para acessar o formulário para editar uma turma
@turma_blueprint.route('/turmas/<int:id_turma>/editar', methods=['GET'])
def editar_turma_page(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return render_template('turma_update.html', turma=turma)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

# Rota que edita uma turma
@turma_blueprint.route('/turmas/<int:id_turma>', methods=['POST'])
def update_turma(id_turma):
    data = request.form
    atualizar_turma(id_turma, data)
    return redirect(url_for('turma.get_turma', id_turma=id_turma))

# Rota que deleta uma turma
@turma_blueprint.route('/turmas/delete/<int:id_turma>', methods=['POST'])
def delete_turma(id_turma):
    excluir_turma(id_turma)
    return redirect(url_for('turma.get_turmas'))

# Rota para API - Listar todas as turmas
@turma_blueprint.route('/api/turmas', methods=['GET'])
def api_get_turmas():
    return jsonify(listar_turmas())

# Rota para API - Obter uma turma por ID
@turma_blueprint.route('/api/turmas/<int:id_turma>', methods=['GET'])
def api_get_turma(id_turma):
    try:
        turma = turma_por_id(id_turma)
        return jsonify(turma)
    except Exception as e:
        return jsonify({'message': str(e)}), 404

# Rota para API - Criar uma nova turma
@turma_blueprint.route('/api/turmas', methods=['POST'])
def api_create_turma():
    data = request.json
    adicionar_turma(data)
    return jsonify(data), 201

# Rota para API - Atualizar uma turma
@turma_blueprint.route('/api/turmas/<int:id_turma>', methods=['PUT'])
def api_update_turma(id_turma):
    data = request.json
    atualizar_turma(id_turma, data)
    return jsonify(turma_por_id(id_turma))

# Rota para API - Deletar uma turma
@turma_blueprint.route('/api/turmas/<int:id_turma>', methods=['DELETE'])
def api_delete_turma(id_turma):
    excluir_turma(id_turma)
    return '', 204
