def manhattan():

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

#d(p,q) = ([p1 - q1]**d + ... + [pn - qn]** d) ** 1 / d

if __name__ == '__main__':
    manhattan()