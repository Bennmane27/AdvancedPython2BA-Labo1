import pytest
import utils

def test_fact():
    # À compléter...

    # Teste si la fonction lève une exception pour une valeur négative
    with pytest.raises(ValueError):
        utils.fact(-1)

    pass

def test_roots():
    # À compléter...

    # Teste si la fonction retourne une liste de deux éléments
    assert len(utils.roots(1, 0, -1)) == 2


    pass

def test_integrate():
    # À compléter...

    # Teste si la fonction retourne une valeur proche de 8/3
    assert abs(utils.integrate('x ** 2 - 1', -1, 1) - 8/3) < 1e-6
    
    pass
