import unittest
from app import create_app, db
from app.models.professor import Professor

class ProfessorTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()
        
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_criar_professor(self):
        response = self.client.post('/professores/', json={
            'nome': 'Caio Prado',
            'idade': 40,
            'materia': 'Matemática',
            'observacoes': 'Muito experiente'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'Professor criado com sucesso!', response.data)

if __name__ == '__main__':
    unittest.main()
