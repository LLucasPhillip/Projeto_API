from flask import Flask, jsonify, request

app = Flask(_name_)

# Dados em memória
professores = {}
turmas = {}
alunos = {}

# Entidades
class Professor:
    def _init_(self, id, nome, idade, materia, observacoes):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

class Turma:
    def _init_(self, id, descricao, professor_id, ativo=True):
        self.id = id
        self.descricao = descricao
        self.professor_id = professor_id  # Relacionamento com Professor via ID
        self.ativo = ativo
        self.alunos = []  # Lista de IDs de alunos

class Aluno:
    def _init_(self, id, nome, idade, turma_id, data_nascimento, nota_primeiro_semestre, nota_segundo_semestre):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id  # Relacionamento com Turma via ID
        self.data_nascimento = data_nascimento
        self.nota_primeiro_semestre = nota_primeiro_semestre
        self.nota_segundo_semestre = nota_segundo_semestre
        self.media_final = (nota_primeiro_semestre + nota_segundo_semestre) / 2

# Endpoints
@app.route('/professores', methods=['POST'])
def adicionar_professor():
    data = request.get_json()
    professor = Professor(id=data['id'], nome=data['nome'], idade=data['idade'],
                          materia=data['materia'], observacoes=data.get('observacoes', ''))
    professores[professor.id] = professor
    return jsonify({'mensagem': 'Professor adicionado com sucesso!'}), 201

@app.route('/professores', methods=['GET'])
def listar_professores():
    return jsonify([{ 'id': p.id, 'nome': p.nome, 'idade': p.idade, 'materia': p.materia, 'observacoes': p.observacoes }
                    for p in professores.values()])

@app.route('/turmas', methods=['POST'])
def adicionar_turma():
    data = request.get_json()
    turma = Turma(id=data['id'], descricao=data['descricao'], professor_id=data['professor_id'], ativo=data.get('ativo', True))
    turmas[turma.id] = turma
    return jsonify({'mensagem': 'Turma adicionada com sucesso!'}), 201

@app.route('/turmas', methods=['GET'])
def listar_turmas():
    return jsonify([{ 'id': t.id, 'descricao': t.descricao, 'professor_id': t.professor_id, 'ativo': t.ativo }
                    for t in turmas.values()])

@app.route('/alunos', methods=['POST'])
def adicionar_aluno():
    data = request.get_json()
    aluno = Aluno(id=data['id'], nome=data['nome'], idade=data['idade'], turma_id=data['turma_id'],
                  data_nascimento=data['data_nascimento'],
                  nota_primeiro_semestre=data['nota_primeiro_semestre'],
                  nota_segundo_semestre=data['nota_segundo_semestre'])
    alunos[aluno.id] = aluno
    # Associando aluno à turma
    if aluno.turma_id in turmas:
        turmas[aluno.turma_id].alunos.append(aluno.id)
    return jsonify({'mensagem': 'Aluno adicionado com sucesso!'}), 201

@app.route('/alunos', methods=['GET'])
def listar_alunos():
    return jsonify([{ 'id': a.id, 'nome': a.nome, 'idade': a.idade, 'turma_id': a.turma_id,
                      'data_nascimento': a.data_nascimento,
                      'nota_primeiro_semestre': a.nota_primeiro_semestre,
                      'nota_segundo_semestre': a.nota_segundo_semestre,
                      'media_final': a.media_final }
                    for a in alunos.values()])

@app.route('/turma/<int:turma_id>/alunos', methods=['GET'])
def listar_alunos_turma(turma_id):
    if turma_id not in turmas:
        return jsonify({'mensagem': 'Turma não encontrada!'}), 404
    turma_alunos = [alunos[aluno_id]._dict_ for aluno_id in turmas[turma_id].alunos]
    return jsonify(turma_alunos)

if _name_ == '_main_':
    app.run(debug=True)
    