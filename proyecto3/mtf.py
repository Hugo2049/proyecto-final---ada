def mtf_access(lista, solicitud):
    """Accede al elemento y lo mueve al frente. Retorna (costo, nueva_lista)."""
    i = lista.index(solicitud)
    costo = i + 1  # posición 1-indexed
    nueva_lista = [solicitud] + lista[:i] + lista[i + 1:]
    return costo, nueva_lista


def simular_mtf(lista_inicial, secuencia):
    """Simula MTF sobre la secuencia completa, imprime cada paso y retorna el costo total."""
    lista = lista_inicial[:]
    costo_total = 0
    for solicitud in secuencia:
        costo, nueva_lista = mtf_access(lista, solicitud)
        print(f"Lista: {lista} | Solicitud: {solicitud} | Costo: {costo} | Nueva lista: {nueva_lista}")
        costo_total += costo
        lista = nueva_lista
    return costo_total
