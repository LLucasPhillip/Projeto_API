import unittest
from app import create_app, db
from app.models.professor import Professor 

class TestProfessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes."""
        cls.app = create_app('testing')  
        cls.client = cls.app.test_client()
        with cls.app.app_context():
            db.create_all() 

    @classmethod
    def tearDownClass(cls):
        """Executado uma vez após todos os testes."""
        with cls.app.app_context():
            db.session.remove()
            db.drop_all() 

    def setUp(self):
        """Executado antes de cada teste."""
        self.professor_data = {
            'nome': 'Prof. Silva',
            'idade': 40,
            'materia': 'Matemática',
            'observacoes': 'Especialista em Álgebra'
        }

    def test_criar_professor(self):
        """Teste para criar um professor."""
        response = self.client.post('/professores/', json=self.professor_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Professor criado com sucesso!', response.data)

        #
        professor = Professor.query.filter_by(nome='Prof. Silva').first()
        self.assertIsNotNone(professor)

    def test_listar_professores(self):
        """Teste para listar professores."""
        self.client.post('/professores/', json=self.professor_data) 
        response = self.client.get('/professores/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prof. Silva', response.data)

    def test_atualizar_professor(self):
        """Teste para atualizar um professor."""
        
        professor = Professor(**self.professor_data)
        db.session.add(professor)
        db.session.commit()

        updated_data = {
            'nome': 'Prof. Silva Atualizado',
            'idade': 41,
            'materia': 'Matemática Avançada',
            'observacoes': 'Agora especialista em Geometria'
        }
        response = self.client.post(f'/professores/{professor.id}', json=updated_data)
        self.assertEqual(response.status_code, 302)

        updated_professor = Professor.query.get(professor.id)
        self.assertEqual(updated_professor.nome, 'Prof. Silva Atualizado')

    def test_deletar_professor(self):
        """Teste para deletar um professor."""
        professor = Professor(**self.professor_data)
        db.session.add(professor)
        db.session.commit()

        response = self.client.post(f'/professores/delete/{professor.id}')
        self.assertEqual(response.status_code, 302) 

        deleted_professor = Professor.query.get(professor.id)
        self.assertIsNone(deleted_professor)

if __name__ == '__main__':
    unittest.main()
