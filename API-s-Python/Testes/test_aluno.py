import unittest

class TestAluno(unittest.TestCase):
    def test_exemplo(self):
        self.assertEqual(1, 1)  # Teste básico que sempre passa

if __name__ == '__main__':
    unittest.main()
