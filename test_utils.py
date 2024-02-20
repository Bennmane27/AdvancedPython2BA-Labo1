import pytest
import utils

def test_fact():
    # À compléter...

    # Teste si la fonction lève une exception pour une valeur négative
    with pytest.raises(ValueError):
        utils.fact(-1)


def test_roots():
    # À compléter...

    # Teste si la fonction retourne une liste de deux éléments
    assert len(utils.roots(1, 0, -1)) == 2


def test_integrate():
    # À compléter...

    
    # Teste si la fonction retourne une valeur plus petite que 2 pour l'intégrale de x**2 - 1 de -1 à 1
    result = utils.integrate('x ** 2 - 1', -1, 1)
    assert abs(result) < 2, "L'intégrale de x**2 - 1 de -1 à 1 devrait être proche de 0"