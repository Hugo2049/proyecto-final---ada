def imtf_access(lista, solicitud, secuencia_restante):
    """
    Accede al elemento igual que MTF, pero solo lo mueve al frente si aparece
    en los próximos (posición - 1) elementos de la secuencia restante.
    Retorna (costo, nueva_lista, se_movio).
    """
    i = lista.index(solicitud)
    costo = i + 1  # posición 1-indexed
    # look-ahead: revisar los próximos i elementos de la secuencia restante
    # (i = posición_1indexed - 1)
    proximos = secuencia_restante[:i]
    mover = solicitud in proximos

    if mover:
        nueva_lista = [solicitud] + lista[:i] + lista[i + 1:]
    else:
        nueva_lista = lista[:]

    return costo, nueva_lista, mover


def simular_imtf(lista_inicial, secuencia):
    """Simula IMTF sobre la secuencia completa, imprime cada paso y retorna el costo total."""
    lista = lista_inicial[:]
    costo_total = 0
    for idx, solicitud in enumerate(secuencia):
        secuencia_restante = secuencia[idx + 1:]
        costo, nueva_lista, mover = imtf_access(lista, solicitud, secuencia_restante)
        movido_str = "Sí" if mover else "No"
        print(
            f"Lista: {lista} | Solicitud: {solicitud} | Costo: {costo} "
            f"| Movido: {movido_str} | Nueva lista: {nueva_lista}"
        )
        costo_total += costo
        lista = nueva_lista
    return costo_total
