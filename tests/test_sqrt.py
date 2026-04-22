"""Tests para la función sqrt(x) -> float."""

import pytest

from src.calculator import sqrt


# --- EJEMPLO (no borrar) ---
def test_sqrt_cuadrado_perfecto():
    """Ejemplo: la raíz de 9 debe dar 3.0."""
    assert sqrt(9) == 3.0


# --- TU TURNO ---
# Agregá tests para los siguientes casos:
#   - Raíz de 0 (resultado: 0.0)

def test_sqrt_raiz_cero():
    """Ejemplo: la raíz de 0 debe dar 0."""
    assert sqrt(0) == 0.0


#   - Raíz de un número que no es cuadrado perfecto (resultado decimal)

def test_sqrt_NO_cuadrado_perfecto():
    """Ejemplo: la raíz de 11 debe dar 3.3166."""
    assert sqrt(11) == pytest.approx(3.3166, rel=1e-4)


#   - Raíz de un número negativo → debe lanzar ValueError

def test_sqrt_negativo():
     with pytest.raises(ValueError):
         sqrt(-4)

#
# Pista: para testear excepciones usá pytest.raises:
#
# def test_sqrt_negativo():
#     with pytest.raises(ValueError):
#         sqrt(-4)
