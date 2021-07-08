def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente"""
    #1. Caso base: o elemento não está presente
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2

    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo
    if A[meio] == item:
        return meio

    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca.
    elif A[meio] > item:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

# A = [0, 10, 20, 30, 40, 50, 60, 70]
# print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 20))
# print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 0))
# print("Pesquisa com sucesso:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 70))
# print("Pesquisa com falha:", pesquisa_binaria_recursiva(A, 0, len(A) - 1, 100))

def pesquisa_binaria(A, item):
    """Implemente pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria(A, 20))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 0))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 70))
print("Pesquisa com falha:", pesquisa_binaria(A, 100))


import random

def procura_entrada_igual_ao_indice(A):
    """Usa busca binária para encontrar um elemento igual ao índice."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        diferenca = A[meio] - meio
        if diferenca == 0:
            return meio
        elif diferenca > 0:
            direita = meio - 1
        else:  # diferenca < 0.
            esquerda = meio + 1
    return -1


def procura_entrada_igual_ao_indice_linear(A):
    """Usa busca sequencial para encontrar um elemento igual ao índice."""
    for i, a in enumerate(A):
        if a == i:
            return i
    return -1


def testa_procura_entrada_igual_ao_indice():
    for _ in range(1000):
        # Gera o tamanho da lista aleatoriamente.
        n = random.randint(1, 1000)

        # Gera a sequência de números aleatoriamente.
        A = random.sample(range(0, 1000), n)

        # Ordena a sequência.
        A.sort()

        # Obtém resposta usando pesquisa binária.
        res_busca_binaria = procura_entrada_igual_ao_indice(A)

        # Verifica resposta.
        if res_busca_binaria != -1:
            assert res_busca_binaria == A[res_busca_binaria]
        else:
            assert res_busca_binaria == procura_entrada_igual_ao_indice_linear(A)

    print("Sucesso!")

testa_procura_entrada_igual_ao_indice()

import random

def encontra_minimo(A, esquerda, direita):
    """Usa busca binária para encontrar o menor
    elemento em uma lista ordenada rotacionada."""

    # A sequência de entrada pode não estar rotacionada.
    if direita < esquerda:
        return A[0]

    # Só há um elemento restante.
    if direita == esquerda:
        return A[esquerda]

    meio = (esquerda + direita) // 2

    # Verifica se elemento A[meio + 1] é o menor.
    if meio < direita and A[meio + 1] < A[meio]:
        return A[meio + 1]

    # Verifica se elemento A[meio] é o menor.
    if meio > esquerda and A[meio] < A[meio - 1]:
        return A[meio]

    # Decide qual metade do arranjo verificar.
    if A[direita] > A[meio]:
        return encontra_minimo(A, esquerda, meio - 1)
    else:
        return encontra_minimo(A, meio + 1, direita)


def testa_encontra_minimo():
    for _ in range(1000):
        # Gera a sequência de números aleatoriamente.
        A = list(set(random.sample(range(-1000, 1000), 1000)))

        # Ordena lista.
        A.sort()

        # Tamanho da lista.
        n = len(A)

        # Encontra ponto para rotacionar a lista.
        k = random.randint(1, n)

        # Rotaciona a lista.
        A = A[k:n] + A[0:k]

        # Verifica resposta.
        assert encontra_minimo(A, 0, len(A) - 1) == min(A)

    print("Sucesso!")

testa_encontra_minimo()
