import time
from multiprocessing import Pool, cpu_count

def leibniz_pi_partial(n, start, end):
    pi = 0
    for i in range(start, end):
        term = (-1) ** i / (2 * i + 1)
        pi += term
    return pi

def leibniz_pi_parallel(n, num_processes):
    partial_pis = []
    with Pool(processes=num_processes) as pool:
        # Distribui os cálculos entre os processos usando pool.starmap
        # Calcula leibniz_pi_partial para intervalos específicos e armazena os resultados
        results = pool.starmap(
            leibniz_pi_partial, 
            [(n, i * (n // num_processes), (i + 1) * (n // num_processes)) for i in range(num_processes)]
        )


    return sum(results) * 4

def main():
    inicio = time.time()
    num_processes = cpu_count()  # Usando a quantidade de núcleos lógicos
    n = 100000000

    pi_approx = leibniz_pi_parallel(n, num_processes)
    print(f"Valor de PI: {pi_approx}")
    
    tempo_gasto = time.time() - inicio
    print(f"Tempo Gasto: {tempo_gasto:,.4}s")

if __name__ == '__main__':
    main()
