def pesquisa_linear(arranjo, elemento_desejado):
    for elemento in arranjo:
        if elemento == elemento_desejado:
            print("Elemento {} está presente no arranjo.".format(elemento_desejado))
            return
    print("Elemento {} não está presente no arranjo.".format(elemento_desejado))


arranjo = list(range(1, 100))

# Pesquisa por elemento presente.
pesquisa_linear(arranjo, 83)

# Pesquisa por elemento ausente.
pesquisa_linear(arranjo, 200)


def pesquisa_linear_in(arranjo, item):
    return item in arranjo

arranjo = list(range(1, 100))

# Pesquisa por elemento presente.
print("O elemento {} está presente no arranjo? {}".format(83, pesquisa_linear_in(arranjo, 83)))

# Pesquisa por elemento ausente.
print("O elemento {} está presente no arranjo? {}".format(200, pesquisa_linear_in(arranjo, 200)))

def pesquisa_linear_index(arranjo, item):
    try:
        return arranjo.index(item)
    except ValueError:
        return -1

arranjo = list(range(1, 100))

# Pesquisa por elemento presente.
print("O elemento {} está no índice {} do arranjo.".format(83, pesquisa_linear_index(arranjo, 83)))

# Pesquisa por elemento ausente.
print("O elemento {} está no índice {} do arranjo.".format(200, pesquisa_linear_index(arranjo, 200)))