# Por Marcos Rocha
# Explicação e prova: https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
# Equação em Latex: \sum_{n=0}^{\infty } \frac{(-1)^{n}}{2n+1}

import random
import time

def leibniz_pi_serial(num_terms):
    pi = 0
    for i in range(num_terms):
        term = (-1)**i / (2*i + 1)
        pi += term
    return pi * 4


def main():
    inicio = time.time()
    tamanho = 524288*2
    num_terms = 10000000
    print(f"Valor de PI: {leibniz_pi_serial(num_terms)}")
    tempo_gasto = time.time()-inicio
    print(f"Tempo Gasto: {tempo_gasto:,.4}s")


if __name__ == '__main__':
    main()