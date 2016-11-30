from functions import soma, subtracao, multiplicacao, divisao
from unittest import TestCase # , main


class tests(TestCase):

    def test_soma(self):
        self.assertEqual(soma(2, 1), 3)

    def test_sub(self):
        self.assertEqual(subtracao(2, 1), 1)

    def test_mul(self):
        self.assertEqual(multiplicacao(2, 1), 2)

    def test_div(self):
        self.assertEqual(divisao(2, 1), 2)

# if __name__ == '__main__':
#     main()
