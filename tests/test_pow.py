"""Tests para la función pow_(a, b) -> float."""

import pytest

from src.calculator import pow_


# --- EJEMPLO (no borrar) ---
def test_pow_base_positiva():
    """Ejemplo: 2 ** 3 debe dar 8."""
    assert pow_(2, 3) == 8


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Cualquier número elevado a 0 (resultado: 1)

def test_pow_elevado_cero():
    """Ejemplo: 2 ** 0 debe dar 1."""
    assert pow_(2, 0) == 1


#   - Número elevado a 1 (resultado: el mismo número)

def test_pow_elevado_neutro():
    """Ejemplo: 2 ** 1 debe dar 2."""
    assert pow_(2, 1) == 2


#   - Base negativa con exponente par (resultado positivo)

def test_pow_exponente_par():
    """Ejemplo: -2 ** 2 debe dar 4."""
    assert pow_(-2, 2) == 4


#   - Exponente decimal, ej: 9 ** 0.5 (raíz cuadrada)

def test_pow_raiz_cuadrada():
    """Ejemplo: 9 ** 0.5 debe dar 3."""
    assert pow_(9, 0.5) == 3


#
# Pista: podés usar @pytest.mark.parametrize para probar varios casos a la vez.
