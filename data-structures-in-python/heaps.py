def menor_elemento(A):
    return A[1]

def filho_esquerda(A, i):
    return A[2 * i]

def filho_direita(A, i):
    return A[(2 * i) + 1]

def pai(A, i):
    return A[i // 2]

def eh_heap_maximo(A):
    for i in range(2, len(A)):
        if A[i] > A[i // 2]:
            return False
        return true

def eh_heap_minimo(A):
    for i in range(2, len(A)):
        if A[i] < A[i // 2]:
            return False
        return true

# Inserção em heaps máximos
# Inserção em heaps mínimos
# Remoção heaps máximos
# Remoção heaps mínimos

def promove(A, n):

    i = n

    while True:
        #Elemento chegou na raiz da árvore.
        if i == 1:
            break

        #Elemento chegou na posição correta.
        if A[p] >= A[i]:
            break

        #Troca elemento de lugar com o pai.
        A[p], A[i] = A[i], A[p]
        i = p


def demove(A, n):
    i = 1
    while True:
        c = 2 * i

        # Elemento não tem mais filhos.
        if c > n:
            break

        # Encontra o índice do maior dos filhos.
        if c + 1 <= n:
            if A[c + 1] > A[c]:
                c += 1

        # O elemento é menor que seu maior filho.
        if A[i] <= A[c]:
            break

        # Troca elemento de lugar com o maior filho.
        A[c], A[i] = A[i], A[c]
        i = c
