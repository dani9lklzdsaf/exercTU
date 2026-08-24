import unittest
import buscaSequencial as bs


class TestBuscaSequencial(unittest.TestCase):

    def test_elemento_no_inicio(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bs.buscaSequencial(vetor, 1), 0)

    def test_elemento_no_meio(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bs.buscaSequencial(vetor, 3), 2)

    def test_elemento_no_fim(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bs.buscaSequencial(vetor, 5), 4)

    def test_elemento_inexistente(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bs.buscaSequencial(vetor, 10), -1)

    def test_vetor_vazio(self):
        vetor = []
        self.assertEqual(bs.buscaSequencial(vetor, 10), -1)


if __name__ == '__main__':
    unittest.main() 
