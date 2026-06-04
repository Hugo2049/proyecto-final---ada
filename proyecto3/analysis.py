def _costo_mtf(lista_inicial, secuencia):
    """Calcula el costo total de MTF sin imprimir (auxiliar interno)."""
    lista = lista_inicial[:]
    total = 0
    for solicitud in secuencia:
        i = lista.index(solicitud)
        total += i + 1
        lista = [solicitud] + lista[:i] + lista[i + 1:]
    return total


def encontrar_minimo(lista_inicial, longitud=20):
    """
    Encuentra la secuencia de `longitud` solicitudes que minimiza el costo total en MTF.
    Estrategia: el mínimo se logra repitiendo siempre el elemento en la posición 1,
    ya que su costo es 1 en cada acceso. Se prueban también alternaciones de pares
    para confirmar que ninguna supera esa cota.
    """
    elementos = lista_inicial[:]
    mejor_secuencia = None
    mejor_costo = float('inf')

    # Probar repetir cada elemento 20 veces
    for elem in elementos:
        secuencia = [elem] * longitud
        costo = _costo_mtf(lista_inicial, secuencia)
        if costo < mejor_costo:
            mejor_costo = costo
            mejor_secuencia = secuencia[:]

    # Probar alternaciones de pares de elementos
    for i in range(len(elementos)):
        for j in range(len(elementos)):
            if i != j:
                secuencia = ([elementos[i], elementos[j]] * longitud)[:longitud]
                costo = _costo_mtf(lista_inicial, secuencia)
                if costo < mejor_costo:
                    mejor_costo = costo
                    mejor_secuencia = secuencia[:]

    return mejor_secuencia, mejor_costo


def encontrar_peor_caso(lista_inicial, longitud=20):
    """
    Construye la secuencia de `longitud` solicitudes que maximiza el costo total en MTF.
    Estrategia greedy: en cada paso se elige el elemento al fondo de la lista actual
    (el de mayor costo posible), forzando siempre el costo máximo.
    """
    lista = lista_inicial[:]
    secuencia = []
    for _ in range(longitud):
        solicitud = lista[-1]  # el elemento más costoso es el último
        secuencia.append(solicitud)
        i = lista.index(solicitud)
        lista = [solicitud] + lista[:i] + lista[i + 1:]

    costo = _costo_mtf(lista_inicial, secuencia)
    return secuencia, costo
