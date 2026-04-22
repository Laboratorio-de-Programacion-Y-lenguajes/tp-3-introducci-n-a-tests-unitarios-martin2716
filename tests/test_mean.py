"""Tests para la función mean(values) -> float."""

import pytest

from src.calculator import mean


# --- EJEMPLO (no borrar) ---
def test_mean_lista_simple():
    """Ejemplo: el promedio de [2, 4, 6] debe dar 4.0."""
    assert mean([2, 4, 6]) == 4.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Lista con un solo elemento (el resultado debe ser ese mismo elemento)

def test_mean_lista_unicoelemento():
    """Ejemplo: el promedio de [4] debe dar 4."""
    assert mean([4]) == 4.0

#   - Lista con números negativos

def test_mean_lista_negativos():
    """Ejemplo: el promedio de [-2, -4, -6] debe dar -4.0."""
    assert mean([-2, -4, -6]) == -4.0

#   - Lista con números decimales (float)

def test_mean_lista_decimales():
    """Ejemplo: el promedio de [2.4, 4.2, 6.3] debe dar 4.3."""
    assert mean([2.4, 4.2, 6.3]) == 4.3

#   - Lista vacía → debe lanzar ValueError

def test_mean_lista_vacia():
     with pytest.raises(ValueError):
         mean([])

