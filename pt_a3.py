zebras = ['zebras=', 'bege', 'branco', 'preto', 'marrom']
cavalos = ['cavalos=', 'vermelho', 'roxo', 'azul', 'mesclado']
galinhas = ['galinhas=', 'vermelho e branco', 'branco ovo', 'pintada', 'galo']
patos = ['patos=', 'violeta', 'ciano', 'laranja', 'branco gelo']
pasto1 = [zebras, cavalos, galinhas, patos]
pasto2 = []

####################### FUNCTIONS #######################


def print_list(my_list):
    for i, x in enumerate(my_list):
        print(i, x)


# MODO 1:
def modo1(l1, l2, index):
    l2.extend(l1)
    l2.pop(index)

    for x in l2:
        if x in l1:
            l1.remove(x)


# MODO 2:
def modo2(l1, l2, index):
    for i, x in list(enumerate(l1)):
        if i != index:
            l1.remove(x)
            l2.append(x)

#############################################################


print_list(pasto1)

indice = int(input('\nDigite o índice do animal a ser mantido no pasto 1: '))


# modo1(pasto1, pasto2, indice)
modo2(pasto1, pasto2, indice)

print('')
print(f"{'FINAL':=^30}")
print('\npasto 1:')
print_list(pasto1)
print('\npasto 2:')
print_list(pasto2)
