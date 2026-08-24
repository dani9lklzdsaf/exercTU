import unittest
import buscaBinaria as bb


class TestBuscaBinaria(unittest.TestCase):

    def test_busca_elemento_meio(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bb.buscaBinaria(vetor, 3), 2)

    def test_busca_primeiro_elemento(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bb.buscaBinaria(vetor, 1), 0)

    def test_busca_ultimo_elemento(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bb.buscaBinaria(vetor, 5), 4)

    def test_vetor_com_quantidade_par(self):
        vetor = [1, 2, 3, 4, 5, 6]
        self.assertEqual(bb.buscaBinaria(vetor, 4), 3)

    def test_elemento_inexistente(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bb.buscaBinaria(vetor, 10), -1)

    def test_vetor_vazio(self):
        vetor = []
        self.assertEqual(bb.buscaBinaria(vetor, 10), -1)


if __name__ == '__main__':
    unittest.main()
