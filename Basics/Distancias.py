def euclidiana(): # A distância entre dois pontos
    soma = ['Pontos:']
    while True:
        p = int(input('P: '))
        q = int(input('Q: '))
        euclid = (p - q)**2
        soma.append(euclid)
        print(soma)

        stop = input('Parar? Y/Any: ')
        if stop == 'y' or stop == 'Y':
            break
        else:
            pass

    soma.remove('Pontos:')

    dist = sum(soma)**0.5
    dist_avg = sum(soma) / 3
    dist_norm = (dist - dist_avg) / (max(soma) - min(soma))

    print('Max:',max(soma),' ', 'Min:',min(soma))
    print('{}'.format(dist_norm))

def hamming(): 
    # O número de posições diferentes entre string de mesmo comprimento
    # O menor número de substituições para uma string ser a outra
    # O número de erros que transformaram uma na outra
    dist = 0  
    tupla = split(string1=input('Primeira palavra: '), string2=input('Segunda palavra: '))
    print(tupla)
    for i in range(len(tupla)):
        if tupla[i][0] != tupla[i][1]:
            dist += 1
        else:
            continue

    print('{}'.format(dist))

def split(string1, string2):# The Hamming Split!
    list1 = list(string1)
    list2 = list(string2)
    if len(list1) != len(list2):
        print('Palavras de tamanhos diferentes. Tente novamente.')
        exit()
    else:
        pass
    amostra = zip(list1, list2)
    return tuple(amostra)

def minkowski():# É uma métrica de distância em um espaço vetorial normado
    d = int(input('Valor d: '))
    soma = ['Pontos:']
    while True:
        p = int(input('P: '))
        q = int(input('Q: '))
        euclid = (p - q)**d
        soma.append(euclid)
        print(soma)

        stop = input('Parar? Y/Any: ')
        if stop == 'y' or stop == 'Y':
            break
        else:
            pass

    soma.remove('Pontos:')
    dist = sum(soma) ** (1 / d)
    print('{}'.format(dist))    

def manhattan(): # Ou City Block | A distância entre dois pontos é a soma das diferenças absolutas de suas coordenadas.
    soma = ['Pontos:']
    while True:
        p = int(input('P: '))
        q = int(input('Q: '))
        cBlock = (p - q)
        soma.append(cBlock)
        print(soma)

        stop = input('Parar? Y/Any: ')
        if stop == 'y' or stop == 'Y':
            break
        else:
            pass

    soma.remove('Pontos:')
    dist = sum(soma)
    print('{}'.format(dist))

if __name__ == '__main__':
    print("Exercício da matéria de Aprendizado de Máquina sobre o calculo de distâncias")
    print("1 - Euclidiana | 2 - Hamming | 3 - Minkowski | 4 - Manhattan")

    opcao = int(input("Que distância deseja calcular? "))
    if opcao == 1:
        euclidiana()
    if opcao == 2:
        hamming()
    if opcao == 3:
        minkowski()
    if opcao == 4:
        manhattan() 
    