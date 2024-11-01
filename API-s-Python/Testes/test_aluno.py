import unittest
from app import create_app, db
from app.models.aluno import Aluno  # Ajuste se necessário
from flask import json

class TestAluno(unittest.TestCase):
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
        self.aluno_data = {
            'nome': 'Teste Aluno',
            'idade': 20,
            'turma_id': 1,  # Altere conforme necessário
            'data_nascimento': '2003-01-01'
        }

    def test_criar_aluno(self):
        """Teste para criar um aluno."""
        response = self.client.post('/alunos', data=self.aluno_data)
        self.assertEqual(response.status_code, 302)  # Redireciona após criar
        # Verifique se o aluno foi realmente adicionado
        aluno = Aluno.query.filter_by(nome='Teste Aluno').first()
        self.assertIsNotNone(aluno)

    def test_listar_alunos(self):
        """Teste para listar alunos."""
        response = self.client.get('/alunos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teste Aluno', response.data)

    def test_atualizar_aluno(self):
        """Teste para atualizar um aluno."""
        aluno = Aluno(**self.aluno_data)
        db.session.add(aluno)
        db.session.commit()

        # Dados de atualização
        updated_data = {
            'nome': 'Aluno Atualizado',
            'idade': 21,
            'turma_id': 1,
            'data_nascimento': '2002-01-01'
        }
        response = self.client.post(f'/alunos/{aluno.id}', data=updated_data)
        self.assertEqual(response.status_code, 302)  # Redireciona após atualizar

        updated_aluno = Aluno.query.get(aluno.id)
        self.assertEqual(updated_aluno.nome, 'Aluno Atualizado')

    def test_deletar_aluno(self):
        """Teste para deletar um aluno."""
        aluno = Aluno(**self.aluno_data)
        db.session.add(aluno)
        db.session.commit()

        response = self.client.post(f'/alunos/delete/{aluno.id}')
        self.assertEqual(response.status_code, 302)  # Redireciona após deletar

        deleted_aluno = Aluno.query.get(aluno.id)
        self.assertIsNone(deleted_aluno)

if __name__ == '__main__':
    unittest.main()
