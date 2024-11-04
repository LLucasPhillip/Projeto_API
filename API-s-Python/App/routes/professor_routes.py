from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.controllers.professor_controller import (
    listar_professores,
    professor_por_id,
    criar_professor,
    atualizar_professor,
    excluir_professor
)

professor_blueprint = Blueprint('professor', __name__)

@professor_blueprint.route('/', methods=["GET"])
def main():
    return 'Rotas para professor'

@professor_blueprint.route('/adicionar', methods=['GET'])
def adicionar_professor_page():
    return render_template('criarProfessores.html')

@professor_blueprint.route('/', methods=['POST'])
def create_professor():
    data = request.form
    criar_professor() 
    return redirect(url_for('professor.get_professores'))
