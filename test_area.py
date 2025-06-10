# Archivo con las funciones de testing

import pytest
from areadeltriangulo import area

def test_area_valida():
    assert area(5, 7) == 17.5

def test_base_negativa():
    with pytest.raises(ValueError, match="base"):
        area(-3, 4)

def test_altura_negativa():
    with pytest.raises(ValueError, match="altura"):
        area(3, -4)

def test_base_cero():
    with pytest.raises(ValueError, match="base"):
        area(0, 4)
