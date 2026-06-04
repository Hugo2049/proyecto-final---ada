from mtf import simular_mtf
from imtf import simular_imtf
from analysis import encontrar_minimo, encontrar_peor_caso

SEP = "=" * 60


def main():
    lista_base = [0, 1, 2, 3, 4]

    # ------------------------------------------------------------------ #
    # PREGUNTA 1                                                           #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 1")
    print(SEP)
    seq1 = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
    total1 = simular_mtf(lista_base, seq1)
    print(f"Costo total: {total1}\n")

    # ------------------------------------------------------------------ #
    # PREGUNTA 2                                                           #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 2")
    print(SEP)
    seq2 = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    total2 = simular_mtf(lista_base, seq2)
    print(f"Costo total: {total2}\n")

    # ------------------------------------------------------------------ #
    # PREGUNTA 3 - MINIMO COSTO                                           #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 3 - MINIMO COSTO")
    print(SEP)
    seq_min, _ = encontrar_minimo(lista_base, 20)
    print(f"Secuencia óptima encontrada: {seq_min}")
    print("Simulación:")
    total3 = simular_mtf(lista_base, seq_min)
    print(f"Costo mínimo total: {total3}\n")

    # ------------------------------------------------------------------ #
    # PREGUNTA 4 - PEOR CASO                                              #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 4 - PEOR CASO")
    print(SEP)
    seq_max, _ = encontrar_peor_caso(lista_base, 20)
    print(f"Secuencia de peor caso: {seq_max}")
    print("Simulación:")
    total4 = simular_mtf(lista_base, seq_max)
    print(f"Costo máximo total: {total4}\n")

    # ------------------------------------------------------------------ #
    # PREGUNTA 5 - PATRON DE REPETICION                                   #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 5 - PATRON DE REPETICION")
    print(SEP)

    seq5a = [2] * 20
    print("Secuencia A (elemento 2):")
    total5a = simular_mtf(lista_base, seq5a)
    print(f"Costo total secuencia A: {total5a}\n")

    seq5b = [3] * 20
    print("Secuencia B (elemento 3):")
    total5b = simular_mtf(lista_base, seq5b)
    print(f"Costo total secuencia B: {total5b}\n")

    print("Observación del patrón:")
    print("  Al repetir 20 veces un elemento x que se encuentra inicialmente en la")
    print("  posición i (1-indexed), el costo total es i + 19.")
    print("  El primer acceso cuesta i (hay que recorrer la lista hasta x);")
    print("  MTF lo mueve al frente, por lo que los 19 accesos restantes cuestan 1 cada uno.")
    print(f"  Elemento 2 (posición 3): 3 + 19 = 22  →  obtenido: {total5a}")
    print(f"  Elemento 3 (posición 4): 4 + 19 = 23  →  obtenido: {total5b}\n")

    # ------------------------------------------------------------------ #
    # PREGUNTA 6 - IMTF                                                   #
    # ------------------------------------------------------------------ #
    print(SEP)
    print("PREGUNTA 6 - IMTF")
    print(SEP)

    print("IMTF sobre mejor caso de MTF:")
    total6_best = simular_imtf(lista_base, seq_min)
    print(f"Costo total IMTF mejor caso: {total6_best}\n")

    print("IMTF sobre peor caso de MTF:")
    total6_worst = simular_imtf(lista_base, seq_max)
    print(f"Costo total IMTF peor caso: {total6_worst}\n")

    print("Comparación final:")
    print(f"Mejor caso  -> MTF: {total3} | IMTF: {total6_best}")
    print(f"Peor caso   -> MTF: {total4} | IMTF: {total6_worst}")
    print(SEP)


if __name__ == "__main__":
    main()
