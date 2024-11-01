from flask import jsonify, request
from app.models.professor import Professor
from app import db

def criar_professor():
    dados = request.get_json()

    # Verificando se todos os dados necessários estão presentes
    if not all(key in dados for key in ('id', 'nome', 'idade', 'materia')):
        return jsonify({'mensagem': 'Dados incompletos para criar o professor!'}), 400

    # Criar uma nova instância de Professor
    professor = Professor(**dados)
    
    try:
        db.session.add(professor)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao criar professor: ' + str(e)}), 500

    return jsonify({"id": professor.id, "mensagem": "Professor criado com sucesso!"}), 201

def listar_professores():
    try:
        professores = Professor.query.all()
        return jsonify([{
            'id': p.id,
            'nome': p.nome,
            'idade': p.idade,
            'materia': p.materia,
            'observacoes': p.observacoes
        } for p in professores]), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao listar professores: ' + str(e)}), 500

def obter_professor(professor_id):
    try:
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({'mensagem': 'Professor não encontrado!'}), 404
        return jsonify({
            'id': professor.id,
            'nome': professor.nome,
            'idade': professor.idade,
            'materia': professor.materia,
            'observacoes': professor.observacoes
        }), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao obter professor: ' + str(e)}), 500

def atualizar_professor(professor_id):
    dados = request.get_json()
    try:
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({'mensagem': 'Professor não encontrado!'}), 404

        # Atualizando os dados do professor
        for key, value in dados.items():
            setattr(professor, key, value)

        db.session.commit()
        return jsonify({'mensagem': 'Professor atualizado com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao atualizar professor: ' + str(e)}), 500

def deletar_professor(professor_id):
    try:
        professor = Professor.query.get(professor_id)
        if not professor:
            return jsonify({'mensagem': 'Professor não encontrado!'}), 404

        db.session.delete(professor)
        db.session.commit()
        return jsonify({'mensagem': 'Professor deletado com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao deletar professor: ' + str(e)}), 500
