"""Tests para la función add(a, b) -> float."""

import pytest

from src.calculator import add


# --- EJEMPLO (no borrar) ---
def test_add_suma_positivos():
    """Ejemplo: 1 + 2 debe dar 3."""
    assert add(1, 2) == 3


# --- TU TURNO ---
# Agregá tests para los siguientes casos:

#   - Sumar dos números negativos

def test_add_suma_negativos():
    """Ejemplo: -1 + (-2) debe dar -3."""
    assert add(-1, -2) == -3


#   - Sumar un número positivo y uno negativo

def test_add_suma_positivo_negativo():
    """Ejemplo: -1 + 2 debe dar 1."""
    assert add(-1, 2) == 1


#   - Sumar con cero

def test_add_suma_cero():
    """Ejemplo: 0 + 5 debe dar 5."""
    assert add(0, 5) == 5


#   - Sumar dos números decimales (float)

def test_add_suma_decimales():
    """Ejemplo: 1.55 + 3.25 debe dar 4.80"""
    assert add(1.55, 3.25) == 4.80


# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
#
# Ejemplo de test parametrizado:
#
# @pytest.mark.parametrize("a,b,expected", [
#     (..., ..., ...),
#     (..., ..., ...),
# ])
# def test_add_parametrizado(a, b, expected):
#     assert add(a, b) == expected
