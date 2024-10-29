from flask import jsonify, request
from .. import db
from ..models.professor import Professor

def criar_professor():
    dados = request.get_json()
    professor = Professor(**dados)
    db.session.add(professor)
    db.session.commit()
    return jsonify({"id": professor.id, "mensagem": "Professor criado com sucesso!"}), 201
