import unittest
from app import create_app, db
from app.models.turma import Turma

class TurmaModelTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app('testing')
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_adicionar_turma(self):
        turma = Turma(descricao='Turma de Teste', professor_id=1)
        db.session.add(turma)
        db.session.commit()
        self.assertIsNotNone(turma.id)

    def test_listar_turmas(self):
        turmas = Turma.query.all()
        self.assertGreater(len(turmas), 0)

    def test_atualizar_turma(self):
        turma = Turma(descricao='Turma de Atualização', professor_id=1)
        db.session.add(turma)
        db.session.commit()

        turma.descricao = 'Turma Atualizada'
        db.session.commit()

        self.assertEqual(turma.descricao, 'Turma Atualizada')

    def test_excluir_turma(self):
        turma = Turma(descricao='Turma a ser excluída', professor_id=1)
        db.session.add(turma)
        db.session.commit()
        id_turma = turma.id

        db.session.delete(turma)
        db.session.commit()
        self.assertIsNone(Turma.query.get(id_turma))

if __name__ == '__main__':
    unittest.main()
