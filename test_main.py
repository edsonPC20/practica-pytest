import pytest
from funcions import (
    trobar_edat_maxima, 
    trobar_producte_mes_car, 
    comptar_empleats_per_departament,
    productes as llista_productes_global
)

# ========== TESTS PER A trobar_edat_maxima ==========

@pytest.mark.parametrize("persones, resultat_esperat", [
    ([{'nom': 'A', 'edat': 25}, {'nom': 'B', 'edat': 67}], 67),
    ([], -1),
    ([{'nom': 'A', 'edat': 25}, {'nom': 'B'}], -1),
    ([{'nom': 'A', 'edat': '25'}], -1),
    ([{'edat': 30}], -1)
])
def test_trobar_edat_maxima(persones, resultat_esperat):
    """
    Testeja la funció trobar_edat_maxima amb diferents escenaris:
    èxit, llista buida, claus absents i tipus erronis.
    """
    assert trobar_edat_maxima(persones) == resultat_esperat

prod_ok = [
    {'nom': 'P1', 'preu': 10, 'categoria': 'X', 'stock': 1},
    {'nom': 'P2', 'preu': 50, 'categoria': 'Y', 'stock': 2}
]

@pytest.mark.parametrize("llista_input, resultat_esperat", [
    # Cas 1: Llista amb productes 
    (prod_ok, prod_ok[1]),
    # Cas 2: Llista buida
    ([], None)
])
def test_trobar_producte_mes_car(llista_input, resultat_esperat, monkeypatch):
    """
    Testeja trobar_producte_mes_car. Atès que la funció usa una variable global,
    utilitzem monkeypatch per simular l'estat de la variable 'productes'.
    """
    import funcions
    # Modifiquem la variable global dins del mòdul per al test
    monkeypatch.setattr(funcions, "productes", llista_input)
    
    assert funcions.trobar_producte_mes_car() == resultat_esperat


# ========== TESTS PER A comptar_empleats_per_departament ==========

empresa_ok = {
    'nom': 'Tech',
    'departaments': [
        {'nom': 'Dev', 'empleats': [{'nom': 'A'}, {'nom': 'B'}]},
        {'nom': 'RRHH', 'empleats': [{'nom': 'C'}]}
    ]
}

empresa_buida = {'nom': 'Empty', 'departaments': []}

@pytest.mark.parametrize("empresa, resultat_esperat", [
    # Cas 1: Empresa amb departaments i empleats
    (empresa_ok, {'Dev': 2, 'RRHH': 1}),
    # Cas 2: Empresa sense departaments
    (empresa_buida, {})
])
def test_comptar_empleats_per_departament(empresa, resultat_esperat):
    """
    Verifica que el recompte d'empleats per departament sigui correcte
    retornant un diccionari amb els noms i les quantitats.
    """
    # Executem la funció i comparem el diccionari resultant
    resultat = comptar_empleats_per_departament(empresa)
    assert resultat == resultat_esperat