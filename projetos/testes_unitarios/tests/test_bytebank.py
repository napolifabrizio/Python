from source.bytebank import Funcionario
from pytest import mark
import pytest

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = "13/03/2000"
        esperado = 24

        funcionario_teste = Funcionario("Teste", entrada, 1000)

        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Gold_Roger_deve_retornar_Roger(self):
        entrada = "Gold Roger"
        esperado = "Roger"

        gold = Funcionario(entrada, "11/11/1900", 100000000000)
        resultado = gold.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = "Nico Robin"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario("Ussop", "01/02/2003", entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1000000

            funcionario_teste = Funcionario("Ussop", "01/02/2003", entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    def test_retorno_str(self):
        entrada_nome = "Franky"
        entrada_nascimento = "7/7/7777"
        entrada_salario = 200000000

        esperado = f'Funcionario({entrada_nome}, {entrada_nascimento}, {entrada_salario})'

        funcionario_teste = Funcionario(entrada_nome, entrada_nascimento, entrada_salario)
        resultado = funcionario_teste.__str__()

        assert resultado == esperado