from flask import jsonify, request
from app.models.aluno import Aluno
from app import db

def adicionar_aluno():
    data = request.get_json()

    if not all(key in data for key in ('id', 'nome', 'idade', 'turma_id', 'data_nascimento', 'nota_primeiro_semestre', 'nota_segundo_semestre')):
        return jsonify({'mensagem': 'Dados incompletos para adicionar o aluno!'}), 400

    aluno = Aluno(**data)

    try:
        db.session.add(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno adicionado com sucesso!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao adicionar aluno: ' + str(e)}), 500

def listar_alunos():
    try:
        alunos = Aluno.query.all()
        return jsonify([{
            'id': a.id,
            'nome': a.nome,
            'idade': a.idade,
            'turma_id': a.turma_id,
            'data_nascimento': a.data_nascimento,
            'nota_primeiro_semestre': a.nota_primeiro_semestre,
            'nota_segundo_semestre': a.nota_segundo_semestre,
            'media_final': a.media_final
        } for a in alunos]), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao listar alunos: ' + str(e)}), 500

def obter_aluno(aluno_id):
    try:
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({'mensagem': 'Aluno não encontrado!'}), 404
        return jsonify({
            'id': aluno.id,
            'nome': aluno.nome,
            'idade': aluno.idade,
            'turma_id': aluno.turma_id,
            'data_nascimento': aluno.data_nascimento,
            'nota_primeiro_semestre': aluno.nota_primeiro_semestre,
            'nota_segundo_semestre': aluno.nota_segundo_semestre,
            'media_final': aluno.media_final
        }), 200
    except Exception as e:
        return jsonify({'mensagem': 'Erro ao obter aluno: ' + str(e)}), 500

def atualizar_aluno(aluno_id):
    data = request.get_json()
    try:
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({'mensagem': 'Aluno não encontrado!'}), 404

        # Atualizand dados do aluno (Tulio)
        
        for key, value in data.items():
            setattr(aluno, key, value)

        db.session.commit()
        return jsonify({'mensagem': 'Aluno atualizado com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao atualizar aluno: ' + str(e)}), 500

def deletar_aluno(aluno_id):
    try:
        aluno = Aluno.query.get(aluno_id)
        if not aluno:
            return jsonify({'mensagem': 'Aluno não encontrado!'}), 404

        db.session.delete(aluno)
        db.session.commit()
        return jsonify({'mensagem': 'Aluno deletado com sucesso!'}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': 'Erro ao deletar aluno: ' + str(e)}), 500
