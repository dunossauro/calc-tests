from operator import add, sub, mul, floordiv
# from unittest import TestCase


def soma(x, y):
    return add(x, y)


def subtracao(x, y):
    return sub(x, y)


def multiplicacao(x, y):
    return mul(x, y)


def divisao(x, y):
    return floordiv(x, y)


# class tests(TestCase):
#
#     def test_soma(self):
#         self.assertEqual(soma(2, 1), 3)
#
#     def test_sub(self):
#         self.assertEqual(subtracao(2, 1), 1)
#
#     def test_mul(self):
#         self.assertEqual(multiplicacao(2, 1), 2)
#
#     def test_div(self):
#         self.assertEqual(divisao(2, 1), 2)
#
# if __name__ == '__main__':
#     main()
