def euclidiana():
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

if __name__ == '__main__':
    euclidiana()
