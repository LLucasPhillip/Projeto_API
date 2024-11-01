from .. import db  # Importa o db da aplicação

# Exceção personalizada para o modelo Professor
class ProfessorNaoEncontrado(Exception):
    pass

# Definição do modelo Professor
class Professor(db.Model):
    __tablename__ = 'professores'  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True)  # ID do professor
    nome = db.Column(db.String(100), nullable=False)  # Nome do professor
    idade = db.Column(db.Integer, nullable=False)  # Idade do professor
    materia = db.Column(db.String(100), nullable=False)  # Matéria que o professor ensina
    observacoes = db.Column(db.String(255))  # Observações adicionais sobre o professor
    turmas = db.relationship('Turma', backref='professor', lazy=True)  # Relacionamento com a tabela de turmas

    def __init__(self, nome, idade, materia, observacoes=None):
        self.nome = nome
        self.idade = idade
        self.materia = materia
        self.observacoes = observacoes

    def to_dict(self):
        """Converte a instância do Professor em um dicionário."""
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'materia': self.materia,
            'observacoes': self.observacoes,
            'turmas': [turma.id for turma in self.turmas]  # Lista de IDs das turmas associadas
        }

# Funções para manipulação dos dados dos professores

def professor_por_id(id_professor):
    """Obtém um professor pelo seu ID."""
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(f'Professor com ID {id_professor} não encontrado.')
    return professor.to_dict()

def listar_professores():
    """Lista todos os professores."""
    professores = Professor.query.all()
    return [professor.to_dict() for professor in professores]

def adicionar_professor(professor_data):
    """Adiciona um novo professor ao banco de dados."""
    novo_professor = Professor(
        nome=professor_data['nome'],
        idade=professor_data['idade'],
        materia=professor_data['materia'],
        observacoes=professor_data.get('observacoes')  # Observações são opcionais
    )
    db.session.add(novo_professor)
    db.session.commit()

def atualizar_professor(id_professor, novos_dados):
    """Atualiza as informações de um professor existente."""
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(f'Professor com ID {id_professor} não encontrado.')
    professor.nome = novos_dados.get('nome', professor.nome)
    professor.idade = novos_dados.get('idade', professor.idade)
    professor.materia = novos_dados.get('materia', professor.materia)
    professor.observacoes = novos_dados.get('observacoes', professor.observacoes)
    db.session.commit()

def excluir_professor(id_professor):
    """Remove um professor do banco de dados."""
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado(f'Professor com ID {id_professor} não encontrado.')
    db.session.delete(professor)
    db.session.commit()