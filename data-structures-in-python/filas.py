class Nodo:
    """Esta classe representa um nodo de uma estrutura duplatamente encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo


    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""

    def __init__(self):
        self.primeiro =  None
        self.ultimo = None


    def __repr__(self):
        return "[" + str(self.primeiro) + "]"


    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""

        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

        # Insere em uma fila vazia.
        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila
            self.ultimo.proximo = novo_nodo

            # Faz com que o último da fila referencie o novo nodo.
            self.ultimo = novo_nodo

    def remove(self):
        """Remove o último elemento da fila."""

        assert self.primeiro != None, "Impossível remover o elemento da fila vazia."

        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo == None

# Cria uma fila vazia.
fila = Fila()
print("Fila vazia: ", fila)

# Insere elementos na fila.
for i in range(5):
    fila.insere(i)
    print("Insere o valor {0} final da fila: {1}".format(i, fila))

# Remove elementos da fila.
while fila.primeiro != None:
    fila.remove()
    print("Removendo elemento que está no começo da fila: ", fila)