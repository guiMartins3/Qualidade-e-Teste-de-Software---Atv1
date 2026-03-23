import pytest
from simple_math import SimpleMath

# Fixture
@pytest.fixture
def math():
    return SimpleMath()

def test_soma(math):
    assert math.sum(2, 3) == 5

def test_soma_negativo(math):
    assert math.sum(-2, -3) == -5

def test_soma_decimal(math):
    assert math.sum(2.5, 3.5) == 6.0
    
def test_soma_tipó_invalido(math):
    with pytest.raises(TypeError):
        math.sum("a", 2)

def test_subtracao(math):
    assert math.subtraction(5, 3) == 2

def test_multiplicacao(math):
    assert math.multiplication(4, 0) == 0

def test_multiplicacao_negativo(math):
    assert math.multiplication(-2, 3) == -6

def test_divisao(math):
    assert math.division(10, 2) == 5

def test_divisao_pZero(math):
    assert math.division(10, 0) == 0

def test_media(math):
    assert math.mean(4, 6) == 5

def test_raiz_quadrada(math):
    assert math.square_root(9) == 3

def test_raiz_quadrada_negativo(math):
    with pytest.raises(ValueError):
        math.square_root(-4)

# TESTE COM MÚLTIPLAS ASSERTIONS
def test_multiple_operations(math):
    assert math.sum(2, 2) == 4
    assert math.subtraction(5, 2) == 3
    assert math.multiplication(3, 3) == 9
    assert math.mean(2, 4) == 3

# TESTE COM MÚLTIPLAS FUNÇÕES
def test_combined_operations(math):
    result = math.sum(2, 3)
    result = math.multiplication(result, 2)
    result = math.subtraction(result, 4)
    assert result == 6

