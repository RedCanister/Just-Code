
def hamming():
    dist = 0
    tupla = split(string1=input('Primeira palavra: '), string2=input('Segunda palavra: '))
    print(tupla)
    for i in range(len(tupla)):
        if tupla[i][0] != tupla[i][1]:
            dist += 1
        else:
            continue

    print('{}'.format(dist))

def split(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    if len(list1) != len(list2):
        print('Palavras de tamanhos diferentes. Tente novamente.')
        exit()
    else:
        pass
    amostra = zip(list1, list2)
    return tuple(amostra)

    # print("Não é possível calcular a distância.")

#len(string1) == len(string2)
#dist = 0
# for s1 != s2:
#     dist++
#     if i == len(string)
#         break

if __name__ == '__main__':
    hamming()