from config import db  # Importando o db da configuração

# Definição do modelo Aluno
class Aluno(db.Model):
    __tablename__ = 'alunos'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)  # ID do aluno
    nome = db.Column(db.String(100), nullable=False)  # Nome do aluno
    idade = db.Column(db.Integer, nullable=False)  # Idade do aluno
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)  # ID da turma
    data_nascimento = db.Column(db.String(10), nullable=False)  # Data de nascimento
    nota_primeiro_semestre = db.Column(db.Float, nullable=True)  # Nota do primeiro semestre
    nota_segundo_semestre = db.Column(db.Float, nullable=True)  # Nota do segundo semestre
    media_final = db.Column(db.Float, nullable=True)  # Média final

    def __init__(self, nome, idade, turma_id, data_nascimento):
        self.nome = nome
        self.idade = idade
        self.turma_id = turma_id
        self.data_nascimento = data_nascimento

    def calcular_media(self):
        if self.nota_primeiro_semestre is not None and self.nota_segundo_semestre is not None:
            self.media_final = (self.nota_primeiro_semestre + self.nota_segundo_semestre) / 2

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'turma_id': self.turma_id,
            'data_nascimento': self.data_nascimento,
            'nota_primeiro_semestre': self.nota_primeiro_semestre,
            'nota_segundo_semestre': self.nota_segundo_semestre,
            'media_final': self.media_final
        }

# Exceção personalizada
class AlunoNaoEncontrado(Exception):
    pass

# Funções para manipulação dos dados dos alunos
def aluno_por_id(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno com ID {id_aluno} não encontrado.')
    return aluno.to_dict()

def listar_alunos():
    alunos = Aluno.query.all()
    return [aluno.to_dict() for aluno in alunos]

def adicionar_aluno(aluno_data):
    novo_aluno = Aluno(
        nome=aluno_data['nome'],
        idade=aluno_data['idade'],
        turma_id=aluno_data['turma_id'],
        data_nascimento=aluno_data['data_nascimento']
    )
    db.session.add(novo_aluno)
    db.session.commit()

def atualizar_aluno(id_aluno, novos_dados):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno com ID {id_aluno} não encontrado.')
    aluno.nome = novos_dados.get('nome', aluno.nome)
    aluno.idade = novos_dados.get('idade', aluno.idade)
    aluno.turma_id = novos_dados.get('turma_id', aluno.turma_id)
    aluno.data_nascimento = novos_dados.get('data_nascimento', aluno.data_nascimento)
    db.session.commit()

def excluir_aluno(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    if not aluno:
        raise AlunoNaoEncontrado(f'Aluno com ID {id_aluno} não encontrado.')
    db.session.delete(aluno)
    db.session.commit()
