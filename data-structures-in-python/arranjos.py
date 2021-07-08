import random


#DUPLICADOS
def encontra_elementos_duplicados(lista, m): 
    """ 
    Imprime os números que aparecem mais de uma vez na lista de entrada.
    É garantido que todos os números na lista de entrada estão no intervalo [0, m].
    """
    #Retorna zero se a lista de entrada estiver vazia.
    if not lista:
        return []

    # Procura por elementos repetidos na lista.
    duplicatas = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista [j]:
                duplicatas.append(lista[j])
    
    # A saída do algoritmo é a lista de elementos repetidos.
    return duplicatas

# elementos_duplicados = encontra_elementos_duplicados([1, 1, 20, 3, 3, 80, 7, 2, 25, 99, 75, 80], 100)
# print("Elementos duplicados: ", elementos_duplicados)



def encontra_elementos_duplicados_frequencia(lista, m):
    """
    Imprime os números que aparecem mais de uma vez na lista de entrada.
    É garantido que todos os números na lista de entrada estão no intervalo[0, m]
    """ 
    # Retorna zero se a lista de entrada estiver vazia.
    if not lista:
        return []

    # Procura por elementos repetidos na lista.
    tabela_frequencia = [0] * m
    duplicatas = []
    for elemento in lista:
        tabela_frequencia[elemento] += 1
        if tabela_frequencia[elemento] > 1:
            duplicatas.append(elemento)

    # A saída do algoritmo é a lista de elementos repetidos.
    return duplicatas

elementos_duplicados = encontra_elementos_duplicados_frequencia([1, 1, 20, 3, 3, 80, 7, 2, 25, 99, 75, 80], 100)
print("Elementos duplicados: ", elementos_duplicados)



#INVERTE
def inverte(nums):
    """Inverte o counteúdo da lista de entrada."""
    inicio = 0
    fim = len(nums) - 1
    while inicio < fim:
        # Note a forma de elegante de trocarmos o coteúdo das variáveis.
        nums[inicio], nums[fim] = nums[fim], nums[inicio]
        inicio += 1
        fim -= 1
    return nums

print(inverte([1, 2, 3, 4, 5, 6, 7]))


def confere_inversao(n, m):
    """Checa o resultado da função `inverte` em n listas de tamanho m geradas aleatoriamente."""

    for _ in range(n):
        # Cria uma lista com números aleatórios no intervalo [0, m].
        nums1 = [random.randint(0, m) for _ in range(m)]

        # Cria uma lista com os mesmos elementos de nums1.
        nums2 = list(nums1)

        # Inverte a lista nums1 usando a biblioteca padrão do Python.
        nums1.reverse()

        # Invoca nosso algoritmo para inverter nums2 e confere o resultado.
        assert(inverte(nums2) == nums1)

    print("Sucesso!")

# Checa o resultado do nosso algoritmo em 500 listas geradas aleatoriamente
confere_inversao(500, 500)

def move_zeros_tres_etapas(nums):
    # Etapa 1: Conta o número de zeros na lista de números.
    zeros = nums.count(0)
    if zeros == 0:
        return nums

    # Etapa 2: Move todos os números diferentes de zero para frente da lista. 
    atual = 0
    for i, num in enumerate(nums):
        if num != 0:
            nums[atual] = nums[i]
            atual += 1

    # Etapa 3: Coloca os zeros no final da lista. 
    tamanho = len(nums) - 1
    for i in range(zeros):
        nums[tamanho - i] = 0

    return nums

print(move_zeros_tres_etapas([0, 1, 0, 3, 12]))

