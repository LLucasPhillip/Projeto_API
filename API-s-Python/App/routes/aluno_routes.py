from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from ..models.aluno import Aluno, AlunoNaoEncontrado
from ..controllers.aluno_controller import (
    adicionar_aluno,
    listar_alunos,
    aluno_por_id,
    atualizar_aluno,
    excluir_aluno
)
from config import db

alunos_blueprint = Blueprint('alunos', __name__)

# ---------------------------------------- index
@alunos_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Bem-vindo ao índice de alunos!"

# ----------------------- 
@alunos_blueprint.route('/', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("alunos.html", alunos=alunos)

# ---------------------------------
@alunos_blueprint.route('/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ---------------------------------- rota acesso para criação de novo aluno
@alunos_blueprint.route('/adicionar', methods=['GET'])
def adicionar_aluno_page():
    return render_template('criarAlunos.html')

# --------------------------------------
@alunos_blueprint.route('/', methods=['POST'])
def create_aluno():
    data = request.form
    novo_aluno = {
        'nome': data['nome'],
        'idade': data['idade'],
        'turma_id': data['turma_id'],
        'data_nascimento': data['data_nascimento']
    }
    
    adicionar_aluno(novo_aluno)
    return redirect(url_for('alunos.get_alunos'))

# ------------------------------------------------
@alunos_blueprint.route('/<int:id_aluno>/editar', methods=['GET'])
def editar_aluno_page(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ---------------------------------------------------
@alunos_blueprint.route('/<int:id_aluno>', methods=['POST'])
def update_aluno(id_aluno):
    try:
        aluno_data = {
            'nome': request.form.get('nome'),
            'idade': request.form.get('idade'),
            'turma_id': request.form.get('turma_id'),
            'data_nascimento': request.form.get('data_nascimento'),
        }
        atualizar_aluno(id_aluno, aluno_data)
        return redirect(url_for('alunos.get_aluno', id_aluno=id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# --------------------------------------------------------
@alunos_blueprint.route('/delete/<int:id_aluno>', methods=['POST'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return redirect(url_for('alunos.get_alunos'))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# --------------------------------- rota para todos alunos (API, JSON)
@alunos_blueprint.route('/api/alunos', methods=['GET'])
def api_get_alunos():
    return jsonify(listar_alunos())

# R---------------------------------- rota para 1 aluno (API, JSON)
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['GET'])
def api_get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ----------------------------
@alunos_blueprint.route('/api/alunos', methods=['POST'])
def api_create_aluno():
    data = request.json
    adicionar_aluno(data)
    return jsonify(data), 201

# ----------------------------------- edita alunos
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['PUT'])
def api_update_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# --------------------------------------- deleta aluno
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['DELETE'])
def api_delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404
