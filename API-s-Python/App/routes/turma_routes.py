from flask import Blueprint, request, jsonify
from ..models.turma import Turma, adicionar_turma, listar_turmas, turma_por_id, atualizar_turma, excluir_turma

turma_bp = Blueprint('turmas', __name__)

@turma_bp.route('/', methods=['GET'])
def get_turmas():
    turmas = listar_turmas()
    return jsonify(turmas), 200

@turma_bp.route('/', methods=['POST'])
def create_turma():
    data = request.get_json()
    adicionar_turma(data)
    return jsonify({'message': 'Turma adicionada com sucesso!'}), 201

@turma_bp.route('/<int:id>', methods=['GET'])
def get_turma(id):
    try:
        turma = turma_por_id(id)
        return jsonify(turma), 200
    except TurmaNaoEncontrada as e:
        return jsonify({'error': str(e)}), 404

@turma_bp.route('/<int:id>', methods=['PUT'])
def update_turma(id):
    data = request.get_json()
    try:
        atualizar_turma(id, data)
        return jsonify({'message': 'Turma atualizada com sucesso!'}), 200
    except TurmaNaoEncontrada as e:
        return jsonify({'error': str(e)}), 404

@turma_bp.route('/<int:id>', methods=['DELETE'])
def delete_turma(id):
    try:
        excluir_turma(id)
        return jsonify({'message': 'Turma excluída com sucesso!'}), 204
    except TurmaNaoEncontrada as e:
        return jsonify({'error': str(e)}), 404
