class NodoLista:
    """Esta classe representa um nodo de uma lista encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo


    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    """Esta classe representa uma lista encadeada."""
    def __init__(self):
        self.cabeca = None

    
    def  __repr__(self):
        return "[" + str(self.cabeca) + "]"

    
def insere_no_inicio(lista, novo_dado):
    # 1) Cria um novo nodo com o dado a ser armazenado.
    novo_nodo = NodoLista(novo_dado)

    # 2) Faz com que o novo nodo seja a cabeça da lista. 
    novo_nodo.proximo = lista.cabeca

    # 3) Faz com que a cabeça da lista referencie o novo nodo.
    lista.cabeca = novo_nodo


# lista = ListaEncadeada()
# print("Lista vazia: ", lista)

# insere_no_inicio(lista, 5)
# print("Lista contém um único elemento:", lista)

# insere_no_inicio(lista, 10)
# print("Inserindo um novo elemento: ", lista)


def insere_depois(lista, nodo_anterior, novo_dado):
    assert nodo_anterior, "Nodo anterior precisa existir na lista."

    # Cria um novo nodo com o dado desejado.
    novo_nodo = NodoLista(novo_dado)

    # Faz o prõximo do novo nodo ser o próximo do nodo anterior.
    novo_nodo.proximo = nodo_anterior.proximo

    # Faz com o que o novo nodo seja
    nodo_anterior.proximo = novo_nodo

# lista = ListaEncadeada()
# print("Lista vazia:", lista)

# insere_no_inicio(lista, 5)
# print("Lista contém um único elemento:", lista)

# nodo_anterior = lista.cabeca
# insere_depois(lista, nodo_anterior, 10)
# print("Inserindo um novo elemento depois de um outro:", lista)


def busca(lista, valor):
    corrente = lista.cabeca
    while corrente and corrente.dado != valor:
        corrente = corrente.proximo
    return corrente


# lista = ListaEncadeada()
# for i in range(8):
#     insere_no_inicio(lista, i)
# print("Lista: ", lista)

# for i in range(8, -4, -2):
#     elemento = busca(lista, i)
#     if elemento:
#         print("Elemento {0} presente na lista!".format(i))
#     else:
#         print("Elemento {0} não encontrado.".format(i))


def remove(self, valor):
    assert self.cabeca, "Impossível remover valor de lista vazia."

    # Nodo a ser removido é a cabeça da lista.
    if self.cabeca.dado == valor:
        self.cabeca = self.cabeca.proximo
    else:
        # Encontra a posição do elemento a ser removido. 
        anterior = None
        corrente = self.cabeca
        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo
        # O nodo corrente é o nodo a ser removido.
        if corrente:
            anterior.proximo = corrente.proximo
        else:
            # O nodo corrente é a cauda da lista
            anterior.proximo = None


# lista = ListaEncadeada()
# for i in range(5):
#     insere_no_inicio(lista, i)
# print("Lista:", lista)

# print("Removendo elementos:")
# for i in range(5):
#     remove(lista, i)
#     print("Removendo o elemento {0}: {1}".format(i, lista))


def remove_duplicatas(lista):
    corrente = lista.cabeca
    while corrente:
        # Usa proximo_distinto para encontrar o próximo valor distinto na lista.
        proximo_distinto = corrente.proximo
        while proximo_distinto and proximo_distinto.dado == corrente.dado:
            proximo_distinto = proximo_distinto.proximo
        # Atualiza o próximo elemento, pulando todos os que forem iguais.
        corrente.proximo = proximo_distinto
        corrente = proximo_distinto
    return lista


def testa_remove_duplicatas():
    # Testa lista vazia.
    lista_vazia = ListaEncadeada()
    lista_vazia = remove_duplicatas(lista_vazia)
    assert str(lista_vazia) == "[None]"

    # Testa lista com um único elemento.
    lista_um_elemento = ListaEncadeada()
    insere_no_inicio(lista_um_elemento, 10)
    resultado = remove_duplicatas(lista_um_elemento)
    assert "[10 -> None]"

    # Testa lista com todos os elementos distintos.
    lista_elementos_distintos = ListaEncadeada()
    for i in range(5, 0, -1):
        insere_no_inicio(lista_elementos_distintos, i)
    resultado = remove_duplicatas(lista_elementos_distintos)
    assert str(resultado) == "[1 -> 2 -> 3 -> 4 -> 5 -> None]"

    # Testa remoção de duplicatas.
    lista_elementos_repetidos = ListaEncadeada()
    insere_no_inicio(lista_elementos_repetidos, 10)
    insere_no_inicio(lista_elementos_repetidos, 10)
    insere_no_inicio(lista_elementos_repetidos, 7)
    insere_no_inicio(lista_elementos_repetidos, 5)
    insere_no_inicio(lista_elementos_repetidos, 1)
    insere_no_inicio(lista_elementos_repetidos, 1)
    insere_no_inicio(lista_elementos_repetidos, 0)
    lista_elementos_repetidos = remove_duplicatas(lista_elementos_repetidos)
    assert str(lista_elementos_repetidos) == "[0 -> 1 -> 5 -> 7 -> 10 -> None]"

    print("Sucesso!")

testa_remove_duplicatas()