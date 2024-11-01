import unittest

# Importar os testes dos módulos
from test_aluno import TestAluno
from test_professor import TestProfessor
from test_turma import TestTurma

# Criar uma suíte de testes
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAluno))
    test_suite.addTest(unittest.makeSuite(TestProfessor))
    test_suite.addTest(unittest.makeSuite(TestTurma))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
