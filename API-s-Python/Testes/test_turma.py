import unittest
from app import create_app, db
from app.models.turma import Turma  # Ajuste conforme necessário

class TestTurma(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes."""
        cls.app = create_app('testing')  # Use a configuração de teste
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all()  # Cria as tabelas

    @classmethod
    def tearDownClass(cls):
        """Executado uma vez após todos os testes."""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all()  # Remove as tabelas

    def setUp(self):
        """Executado antes de cada teste."""
        self.turma_data = {
            'nome': 'Turma A',
            'nivel': 'Fundamental',
            'ano': 2024,
            'observacoes': 'Turma com foco em Matemática'
        }

    def test_criar_turma(self):
        """Teste para criar uma turma."""
        response = self.client.post('/turmas/', json=self.turma_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Turma criada com sucesso!', response.data)

        # Verifique se a turma foi realmente adicionada
        turma = Turma.query.filter_by(nome='Turma A').first()
        self.assertIsNotNone(turma)

    def test_listar_turmas(self):
        """Teste para listar turmas."""
        self.client.post('/turmas/', json=self.turma_data)  # Cria uma turma
        response = self.client.get('/turmas/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Turma A', response.data)

    def test_atualizar_turma(self):
        """Teste para atualizar uma turma."""
        # Criação da turma para teste
        turma = Turma(**self.turma_data)
        db.session.add(turma)
        db.session.commit()

        updated_data = {
            'nome': 'Turma B',
            'nivel': 'Fundamental',
            'ano': 2025,
            'observacoes': 'Turma com foco em Ciências'
        }
        response = self.client.post(f'/turmas/{turma.id}', json=updated_data)
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar

        updated_turma = Turma.query.get(turma.id)
        self.assertEqual(updated_turma.nome, 'Turma B')

    def test_deletar_turma(self):
        """Teste para deletar uma turma."""
        turma = Turma(**self.turma_data)
        db.session.add(turma)
        db.session.commit()

        response = self.client.post(f'/turmas/delete/{turma.id}')
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar

        deleted_turma = Turma.query.get(turma.id)
        self.assertIsNone(deleted_turma)

if __name__ == '__main__':
    unittest.main()
