# Variable global que necesita el test
productes = []

def trobar_edat_maxima(persones):
    if not persones: 
        return -1
    for p in persones:
        if 'nom' not in p or 'edat' not in p or not isinstance(p['edat'], int):
            return -1
    return max(p['edat'] for p in persones)

def trobar_producte_mes_car():
    if not productes: 
        return None
    return max(productes, key=lambda p: p['preu'])

def comptar_empleats_per_departament(empresa):
    recompte = {}
    for dep in empresa.get('departaments', []):
        recompte[dep['nom']] = len(dep.get('empleats', []))
    return recompte