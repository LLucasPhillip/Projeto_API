from .. import db  # Importando o db da inicialização do app

# Exceção personalizada para o modelo Turma
class TurmaNaoEncontrada(Exception):
    pass

# Definição do modelo Turma
class Turma(db.Model):
    __tablename__ = 'turmas'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)  # ID da turma
    descricao = db.Column(db.String(100), nullable=False)  # Descrição da turma
    ativo = db.Column(db.Boolean, default=True)  # Indica se a turma está ativa
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)  # ID do professor responsável
    alunos = db.relationship('Aluno', backref='turma', lazy=True)  # Relacionamento com a tabela de alunos

    def __init__(self, descricao, professor_id, ativo=True):
        self.descricao = descricao
        self.professor_id = professor_id
        self.ativo = ativo

    def to_dict(self):
        """Converte a instância da Turma em um dicionário."""
        return {
            'id': self.id,
            'descricao': self.descricao,
            'ativo': self.ativo,
            'professor_id': self.professor_id,
            'alunos': [aluno.id for aluno in self.alunos]  # Lista de IDs dos alunos associados
        }

# Funções para manipulação dos dados das turmas

def turma_por_id(id_turma):
    """Obtém uma turma pelo seu ID."""
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada.')
    return turma.to_dict()

def listar_turmas():
    """Lista todas as turmas."""
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(turma_data):
    """Adiciona uma nova turma ao banco de dados."""
    nova_turma = Turma(
        descricao=turma_data['descricao'],
        professor_id=turma_data['professor_id'],
        ativo=turma_data.get('ativo', True)  # Ativo é verdadeiro por padrão
    )
    db.session.add(nova_turma)
    db.session.commit()

def atualizar_turma(id_turma, novos_dados):
    """Atualiza as informações de uma turma existente."""
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada.')
    turma.descricao = novos_dados.get('descricao', turma.descricao)
    turma.professor_id = novos_dados.get('professor_id', turma.professor_id)
    turma.ativo = novos_dados.get('ativo', turma.ativo)
    db.session.commit()

def excluir_turma(id_turma):
    """Remove uma turma do banco de dados."""
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada(f'Turma com ID {id_turma} não encontrada.')
    db.session.delete(turma)
    db.session.commit()
