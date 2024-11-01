from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from .alunos_model import AlunoNaoEncontrado, listar_alunos, aluno_por_id, adicionar_aluno, atualizar_aluno, excluir_aluno
from config import db

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/', methods=['GET'])
def getIndex():
    return "Meu index"

# ROTA PARA TODOS OS ALUNOS (Renderiza um template)
@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = listar_alunos()
    return render_template("alunos.html", alunos=alunos)

# ROTA PARA UM ALUNO (Renderiza um template)
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['GET'])
def get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_id.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA ACESSAR O FORMULÁRIO DE CRIAÇÃO DE UM NOVO ALUNO
@alunos_blueprint.route('/alunos/adicionar', methods=['GET'])
def adicionar_aluno_page():
    return render_template('criarAlunos.html')

# ROTA QUE CRIA UM NOVO ALUNO
@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    nome = request.form['nome']
    idade = request.form['idade']  # Adicionei idade
    turma_id = request.form['turma_id']  # Adicionei turma_id
    data_nascimento = request.form['data_nascimento']  # Adicionei data_nascimento

    novo_aluno = {
        'nome': nome,
        'idade': idade,
        'turma_id': turma_id,
        'data_nascimento': data_nascimento
    }
    
    adicionar_aluno(novo_aluno)
    return redirect(url_for('alunos.get_alunos'))

# ROTA PARA O FORMULÁRIO PARA EDITAR UM ALUNO
@alunos_blueprint.route('/alunos/<int:id_aluno>/editar', methods=['GET'])
def editar_aluno_page(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return render_template('aluno_update.html', aluno=aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA QUE EDITA UM ALUNO
@alunos_blueprint.route('/alunos/<int:id_aluno>', methods=['POST'])
def update_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        aluno_data = {
            'nome': request.form.get('nome', aluno['nome']),
            'idade': request.form.get('idade', aluno['idade']),
            'turma_id': request.form.get('turma_id', aluno['turma_id']),
            'data_nascimento': request.form.get('data_nascimento', aluno['data_nascimento']),
        }
        atualizar_aluno(id_aluno, aluno_data)
        return redirect(url_for('alunos.get_aluno', id_aluno=id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA QUE DELETA UM ALUNO
@alunos_blueprint.route('/alunos/delete/<int:id_aluno>', methods=['POST'])
def delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return redirect(url_for('alunos.get_alunos'))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA PARA TODOS OS ALUNOS (API, JSON response)
@alunos_blueprint.route('/api/alunos', methods=['GET'])
def api_get_alunos():
    return jsonify(listar_alunos())

# ROTA PARA UM ALUNO (API, JSON response)
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['GET'])
def api_get_aluno(id_aluno):
    try:
        aluno = aluno_por_id(id_aluno)
        return jsonify(aluno)
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA QUE CRIA UM NOVO ALUNO (API, JSON response)
@alunos_blueprint.route('/api/alunos', methods=['POST'])
def api_create_aluno():
    data = request.json
    adicionar_aluno(data)
    return jsonify(data), 201

# ROTA QUE EDITA UM ALUNO (API, JSON response)
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['PUT'])
def api_update_aluno(id_aluno):
    data = request.json
    try:
        atualizar_aluno(id_aluno, data)
        return jsonify(aluno_por_id(id_aluno))
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

# ROTA QUE DELETA UM ALUNO (API, JSON response)
@alunos_blueprint.route('/api/alunos/<int:id_aluno>', methods=['DELETE'])
def api_delete_aluno(id_aluno):
    try:
        excluir_aluno(id_aluno)
        return '', 204
    except AlunoNaoEncontrado:
        return jsonify({'message': 'Aluno não encontrado'}), 404

##