"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são?

Teste é a forma de se testar unidades individuais de código fonte.

Unidades individuais podem ser: funções, métodos, classes, módulos etc.

# OBS: Teste unitário nãp é específico da linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir de então
ganhamos todos os 'assertions' presentes no módulo.

from unittest import TestCase

Para rodar os testes, utlizamos unittest.main()

TestCase -> casos de testes para sua unidade.

# Conhecendo as assertions
https://docs.python.org/3/library/unittest.html

Método                              checa que

assertEqual(a, b)                   a == b
assertNotEqual(a, b)                a != b
assertTrue(x)                       x é verdadeiro
assertFalse(x)                      x é falso
assertIs(a, b)                      a é b
assertIsNot(a, b)                   a não é b
assertIsNone(x)                     x é None
assertIsNotNone(x)                  x não é None
assertIn(a, b)                      a está em b
assertNotIn(a, b)                   a não está em b
assertIsInstance(a, b)              a é instância de b
assertNotIsInstance(a, b)           a não é instância de b

Por convenção, todos os testes em um test case, devem ter seu nomoe iniciado com test_
"""

# Prática - Utilizando a abordagem TDD

from unittest import TestCase, main
from testes.atividades import comer, dormindo_acordado


class AtividadesTestes(TestCase):
    def test_nao_comendo(self):
        self.assertEqual(comer(False), 'Não estou comendo')

    def test_comendo(self):
        self.assertEqual(comer(True), 'Estou comendo')

    def test_dormindo_as_23_horas(self):
        self.assertEqual(dormindo_acordado(23), 'Estou dormindo')

    def test_dormindo_as__7_horas(self):
        self.assertEqual(dormindo_acordado(7), 'Estou dormindo')

    def test_dormindo_as_24_horas(self):
        self.assertEqual(dormindo_acordado(24), 'Estou dormindo')

    def test_acordado_as_22_horas(self):
        self.assertEqual(dormindo_acordado(22), 'Estou acordado')

    def test_acordado_as_8_horas(self):
        self.assertEqual(dormindo_acordado(8), 'Estou acordado')

    def tet_acordado_as_12_horas(self):
        self.assertEqual(dormindo_acordado(12), 'Estou acordado')


if __name__ == '__main__':
    main()
