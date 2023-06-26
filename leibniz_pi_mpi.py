# Por Marcos Rocha

from mpi4py import MPI

def leibniz_pi_part(n, start, end):
    pi = 0
    for i in range(start, end):
        term = (-1)**i / (2*i + 1)
        pi += term
    return pi

inicio = MPI.Wtime()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10000000

# calculando o intervalo para cada processo
start = rank*(n//size)
end = (rank+1)*(n//size)

# cada processo calcula sua parte
pi_part = leibniz_pi_part(n, start, end)

# reúne os resultados de todos os processos
pi_parts = comm.gather(pi_part, root=0)

# o processo mestre calcula a estimativa final de pi
if rank == 0:
    pi_approx = sum(pi_parts) * 4
    print(f"Valor de PI: {pi_approx}")
    tempo_gasto = MPI.Wtime()-inicio
    print(f"Tempo Gasto: {tempo_gasto:,.4}s")

