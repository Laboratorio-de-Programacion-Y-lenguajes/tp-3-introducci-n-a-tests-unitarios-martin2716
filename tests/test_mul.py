"""Tests para la función mul(a, b) -> float."""

import pytest

from src.calculator import mul


# --- EJEMPLO (no borrar) ---
def test_mul_positivos():
    """Ejemplo: 3 * 4 debe dar 12."""
    assert mul(3, 4) == 12


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Multiplicar por cero

def test_mul_cero():
    """Ejemplo: 3 * 0 debe dar 0."""
    assert mul(3, 0) == 0


#   - Multiplicar dos números negativos (resultado positivo)

def test_mul_negativos():
    """Ejemplo: -3 * -2 debe dar 6."""
    assert mul(-3, -2) == 6


#   - Multiplicar un positivo y un negativo (resultado negativo)

def test_mul_negativoypositivo():
    """Ejemplo: -3 * 2 debe dar -6."""
    assert mul(-3, 2) == -6


#   - Multiplicar por 1 (elemento neutro)

def test_mul_neutro():
    """Ejemplo: -3 * 1 debe dar -3."""
    assert mul(-3, 1) == -3


#   - Multiplicar dos decimales (float)

def test_mul_decimales():
    """Ejemplo: 3.2 * 2.1 debe dar 6.72."""
    assert mul(3.02 , 2.01) == 6.0702


#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
