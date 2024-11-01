from flask import jsonify, request
from app.models.turma import Turma
from app import db

def adicionar_turma():
    data = request.get_json()

    # Verificando se todos os dados necessários estão presentes
    if not all(key in data for key in ('id', 'descricao', 'professor_id')):
        return jsonify({'mensagem': 'Dados incompletos para adicionar a turma!'}), 400

    turma = Turma(**data)
    
    try:
        db.session.add(turma)
        db.session.commit()
        return jsonify({'mensagem': 'Turma adicionada com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao adicionar turma: ' + str(e)}), 500

def listar_turmas():
    try:
        turmas = Turma.query.all()
        return jsonify([{
            'id': t.id,
            'descricao': t.descricao,
            'professor_id': t.professor_id,
            'ativo': t.ativo
        } for t in turmas]), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao listar turmas: ' + str(e)}), 500

def obter_turma(turma_id):
    try:
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({'mensagem': 'Turma não encontrada!'}), 404
        return jsonify({
            'id': turma.id,
            'descricao': turma.descricao,
            'professor_id': turma.professor_id,
            'ativo': turma.ativo
        }), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao obter turma: ' + str(e)}), 500

def atualizar_turma(turma_id):
    data = request.get_json()
    try:
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({'mensagem': 'Turma não encontrada!'}), 404

        # Atualizando os dados da turma
        for key, value in data.items():
            setattr(turma, key, value)

        db.session.commit()
        return jsonify({'mensagem': 'Turma atualizada com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao atualizar turma: ' + str(e)}), 500

def deletar_turma(turma_id):
    try:
        turma = Turma.query.get(turma_id)
        if not turma:
            return jsonify({'mensagem': 'Turma não encontrada!'}), 404

        db.session.delete(turma)
        db.session.commit()
        return jsonify({'mensagem': 'Turma deletada com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao deletar turma: ' + str(e)}), 500
