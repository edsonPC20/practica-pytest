# ========== Lògica per a trobar_edat_maxima ==========

def trobar_edat_maxima(persones):
    """
    Retorna l'edat màxima d'una llista de diccionaris.
    Retorna -1 si la llista és buida, falta la clau 'edat' o el tipus no és int.
    """
    if not persones:
        return -1
    
    max_edat = -1
    for p in persones:
        # Verifiquem que la clau existeixi i que sigui un enter
        if 'edat' not in p or not isinstance(p['edat'], int):
            return -1
        
        if p['edat'] > max_edat:
            max_edat = p['edat']
            
    return max_edat


# ========== Lògica per a trobar_producte_mes_car ==========

# Aquesta és la variable global que el test modifica amb monkeypatch
productes = []

def trobar_edat_maxima(persones):
    if not persones:
        return -1
    
    max_edat = -1
    for p in persones:
        # El test falla porque espera -1 si falta el 'nom' o 'edat' no es correcto
        if 'nom' not in p or 'edat' not in p or not isinstance(p['edat'], int):
            return -1
        
        if p['edat'] > max_edat:
            max_edat = p['edat']
            
    return max_edat


# ========== Lògica per a comptar_empleats_per_departament ==========

def comptar_empleats_per_departament(empresa):
    """
    Retorna un diccionari amb el recompte d'empleats per cada departament.
    """
    recompte = {}
    
    # Accedim a la llista de departaments de l'empresa
    departaments = empresa.get('departaments', [])
    
    for dep in departaments:
        nom_dep = dep['nom']
        num_empleats = len(dep.get('empleats', []))
        recompte[nom_dep] = num_empleats
        
    return recompte