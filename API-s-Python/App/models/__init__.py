from flask_sqlalchemy import SQLAlchemy

# Inicialização do banco de dados
db = SQLAlchemy()

# Importação dos modelos
from .professor import Professor
from .turma import Turma
from .aluno import Aluno

# Funções auxiliares ou exceções que você deseja expor
from .aluno import (
    aluno_por_id,
    listar_alunos,
    adicionar_aluno,
    atualizar_aluno,
    excluir_aluno,
    AlunoNaoEncontrado,
)

from .professor import (
    professor_por_id,
    listar_professores,
    adicionar_professor,
    atualizar_professor,
    excluir_professor,
    ProfessorNaoEncontrado,
)

from .turma import (
    turma_por_id,
    listar_turmas,
    adicionar_turma,
    atualizar_turma,
    excluir_turma,
    TurmaNaoEncontrada,
)

# Aqui você pode definir outras importações ou inicializações, se necessário.
