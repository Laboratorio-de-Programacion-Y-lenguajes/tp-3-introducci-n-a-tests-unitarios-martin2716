"""Tests para la función div(a, b) -> float."""

import pytest 
import math

from src.calculator import div


# --- EJEMPLO (no borrar) ---
def test_div_normal():
    """Ejemplo: 6 / 3 debe dar 2.0."""
    assert div(6, 3) == 2.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - División que da resultado decimal (float)

def test_div_decimal():
    """Ejemplo: 3 / 6 debe dar 0.5"""
    assert div(3, 6) == 0.5

#   - División con números negativos

def test_div_negativos():
    """Ejemplo: -3 / 6 debe dar -0.5"""
    assert div(-3, 6) == -0.5

#   - División por cero → debe lanzar ZeroDivisionError

def test_div_cero():
    with pytest.raises(ZeroDivisionError) as excinfo: div(3, 0)


