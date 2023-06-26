# Cálculo de Aproximação de π utilizando a Série de Leibniz em Python com MPI

Este repositório contém uma implementação da Série de Leibniz para calcular a aproximação de π. Ele apresenta duas versões do mesmo algoritmo, uma versão serial e uma versão paralela usando a biblioteca MPI em Python.

## Como a Série de Leibniz funciona?

A Série de Leibniz para π é uma série infinita que converge para π. A série é a seguinte:

π = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...)

$$ \sum_{n=0}^{\infty } \frac{(-1)^{n}}{2n+1} $$

## Instalação

Para executar este projeto, você precisará instalar o seguinte:

- Python 3.x
- mpi4py: `pip install mpi4py`

## Uso

1. Clone este repositório em sua máquina local.
2. Navegue até a pasta onde o repositório foi clonado.
3. Execute o programa serial com `python leibniz_pi_serial.py`.
4. Execute o programa paralelo com `mpiexec -n 4 python leibniz_pi_mpi.py`, onde `-n 4` é o número de processos que você deseja iniciar.

## Contribuição

Pull requests são bem-vindos. Para mudanças importantes, abra um problema primeiro para discutir o que você gostaria de alterar.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
