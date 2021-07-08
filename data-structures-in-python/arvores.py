# Árvores Binárias

## Representação de Árvores Binárias
class NodoArvore:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)


# raiz = NodoArvore(3)
# raiz.esquerda = NodoArvore(5)
# raiz.direita = NodoArvore(1)
# print("Árvore: ", raiz)

# Árvores Binárias de Pesquisa (ou Binary Search Tress - BSTs, do Inglês) 

# raiz = NodoArvore(40)

# raiz.esquerda = NodoArvore(20)
# raiz.direita = NodoArvore(60)

# raiz.direita.esquerda = NodoArvore(50)
# raiz.direita.direita = NodoArvore(70)
# raiz.esquerda.esquerda = NodoArvore(10)
# raiz.esquerda.direita = NodoArvore(30)

def em_ordem(raiz):
    if not raiz:
        return
    
    # Visita filho da esqueda.
    em_ordem(raiz.esquerda)

    # Visita nodo corrente.
    print(raiz.chave)

    # Visita filhp da direita.
    em_ordem(raiz.direita)

# print("EM ORDEM")
# em_ordem(raiz)
# print("\n\n")

def pre_ordem(raiz):
    if not raiz:
        return

    # Visita nodo corrente.
    print(raiz.chave)

    # Visita filho da esqueda.
    pre_ordem(raiz.esquerda)

    # Visita filhp da direita.
    pre_ordem(raiz.direita)

# print("PRE ORDEM")
# pre_ordem(raiz)
# print("\n\n")


def pos_ordem(raiz):
    if not raiz:
        return
    
    # Visita filho da esqueda.
    pos_ordem(raiz.esquerda)
    
    # Visita filhp da direita.
    pos_ordem(raiz.direita)

    # Visita nodo corrente.
    print(raiz.chave)

# print("PÓS ORDEM")
# pos_ordem(raiz)


def insere(raiz, nodo):
    """Insere um nodo em uma árvore binária de pesquisa."""
    # Nodo deve ser inserido na raiz.raiz
    if raiz is None:
        raiz  = nodo
    
    # Nodo deve ser inserido na subárvore direita
    elif raiz.chave < nodo.chave:
        if raiz.direita is None:
            raiz.direita = nodo
        else:
            insere(raiz.direita, nodo)

    # Nodo deve ser inserido na subárvore esquerda
    else:
        if raiz.esquerda is None:
            raiz.esquerda = nodo
        else:
            insere(raiz.esquerda, nodo)

# # Cria uma árvore binária de pesquisa
# raiz = NodoArvore(40)
# for chave in [20, 60, 50, 70, 10, 30]:
#     nodo = NodoArvore(chave)
#     insere(raiz, nodo)
# # Imprime o caminhamento em ordem da árvore
# print("EM ORDEM")
# em_ordem(raiz)


def busca(raiz, chave):
    """Procure por uma chave em uma árvore binária de pesquisa"""
    # Trata o caso em que a chave procurada não está presente. 
    if raiz is None:
        return None

    # A chave procurada está na raiz da árvore. 
    if raiz.chave == chave:
        return raiz

    # A chave procurada é maior que a da raiz. 
    if raiz.chave < chave:
        return busca(raiz.direita, chave)

    # A chave procurada é menor que a da raiz. 
    return busca(raiz.esquerda, chave)

# Cria uma árvore binária de pesquisa. 
raiz = NodoArvore(40)
for chave in [20, 60, 50, 70, 10, 30]:
    nodo = NodoArvore(chave)
    insere(raiz, nodo)

# Procuira por valores na árvore. 
for chave in [-50, 10, 30, 70, 100]:
    resultado = busca(raiz, chave)
    if resultado:
        print("Busca pela chave {}: Sucesso!".format(chave))
    else:
        print("Busca pela chave {}: Falha!".format(chave))


def menor_elemento(raiz):
    nodo = raiz
    while nodo.esquerda is not None:
        nodo = nodo.esquerda
    return nodo.chave


def maior_elemento(raiz):
    nodo = raiz
    while nodo.direita is not None:
        nodo = nodo.direita
    return nodo.chave


def identicas(a, b):
    # 1. As duas árvores são vazias.
    if a is None and b is None:
        return True

    # 2. Nenhuma das árvores é vazia. Precisamos compará-las.
    if a is not None and b is not None:
        return ((a.chave == b.chave) and
                identicas(a.esquerda, b.esquerda)and
                identicas(a.direita, b.direita))

    # 3. Uma árvore é vazia mas a outra não
    return False


def altura(raiz):
    if raiz is None:
        return 0
    return max(altura(raiz.esquerda), altura(raiz.direita)) + 1


def balanceada(raiz):
    # Uma árvore binária vazia é balanceada.
    if raiz is None:
        return True

    altura_esq = altura(raiz.esquerda)
    altura_dir = altura(raiz.direita)
    # Alturas diferem em que mais de uma unidade. 
    if abs(altura_esq - altura_dir) > 1:
        return False
    
    return balanceada(raiz.esquerda) and balanceada(raiz.direita)


def checa_simetria(raiz):
    def simetrias(subarvore_esq, subarvore_dir):
        if not subarvore_esq and not subarvore_dir:
            return True
        elif subarvore_esq and subarvore_dir:
            return (subarvore_esq.chave == subarvore_dir.chave and
                    simetricas(subarvore_esq.esquerda, subarvore_dir.direita) and
                    simetricas(subarvore_esq.direita, subarvore_dir.esquerda))
        # Uma sub-árvore é vazia e a outra não
        return False
    return not raiz or simetricas(raiz.esquerda, raiz.direita)
