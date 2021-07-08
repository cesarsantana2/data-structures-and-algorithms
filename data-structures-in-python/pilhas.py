# #Pilhas com Arranjos

# pilha = [1, 1, 2, 3, 5]
# print("Pilha: ", pilha)

# pilha.append(8)
# print("Inserindo um elemento: ", pilha)

# pilha.append(13)
# print("Inserindo outro elemento: ", pilha)

# pilha.pop()
# print("Removendo um elemento: ", pilha)

# pilha.pop()
# print("Removendo outro elemento: ", pilha)


# ---


#Pilhas com Estruturas Encadeadas

class Nodo:
    """Esta classe representa um nodo de uma estrutura encadead."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)


class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada"""

    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"


    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""

        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha. 
        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo. 
        self.topo = novo_nodo


    def remove(self):
        """Remove o elemento que está no topo da pilha"""

        assert self.topo, "Impossível remover valor da pilha vazia"

        self.topo = self.topo.anterior

# Cria uma pilha vazia.
pilha = Pilha()
print("Pilha vazia: ", pilha)

# Insere elementos na pilha.Pilha()
for i in range(5):
    pilha.insere(i)
    print("Insere o valor {0} no topo da pilha: {1}".format(i, pilha))

# Remove elementos na pilha
while pilha.topo != None:
    pilha.remove()
    print("Removendo elemento que está no topo da pilha: ", pilha)