"""
Unittest - Antes e após hooks


----
hooks - são os testes em si. Ou seja, a execução dos testes
----

setUp() -> é excutado antes de cada método de teste. É utils para criarmos instâncias de objetos e outros dados;

tearDown() -> é executado ao final de cada método do teste. É útil para excluir dados ou fechar conexões com banco
             de dados.

"""

# Exemplo

from unittest import TestCase


class ModuloTest(TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass

    def test_primeiro(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

    def test_segundo(self):
        # setUp() vai rodar antes do teste
        # tearDown() vai rodar após o teste.
        pass

