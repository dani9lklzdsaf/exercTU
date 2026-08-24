import unittest
import bubbleSort as bs


class TestBubbleSort(unittest.TestCase):

    def test_vetor_ja_ordenado(self):
        vetor = [1, 2, 3, 4, 5]
        self.assertEqual(bs.bubbleSort(vetor), [1, 2, 3, 4, 5])

    def test_vetor_decrescente(self):
        vetor = [5, 4, 3, 2, 1]
        self.assertEqual(bs.bubbleSort(vetor), [1, 2, 3, 4, 5])

    def test_elementos_repetidos(self):
        vetor = [3, 1, 2, 3, 1]
        self.assertEqual(bs.bubbleSort(vetor), [1, 1, 2, 3, 3])

    def test_negativos_e_positivos(self):
        vetor = [-3, 5, -1, 2, 0]
        self.assertEqual(bs.bubbleSort(vetor), [-3, -1, 0, 2, 5])

    def test_vetor_vazio(self):
        vetor = []
        self.assertEqual(bs.bubbleSort(vetor), [])

    def test_um_elemento(self):
        vetor = [7]
        self.assertEqual(bs.bubbleSort(vetor), [7])


if __name__ == '__main__':
    unittest.main()
