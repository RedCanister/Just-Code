"""
List Comprehension ou compreensão de listas é uma ferramenta 
do Python que simplifica a execução de listas, usando uma 
nova sintaxe e reduzindo as linhas até 1 são mais rápidas 
e fáceis de entender.

A sintaxe é a seguinte:

var = [EXPRESSION for ITEM in ITERABLE if CONDITION==True]

Um novo objeto será criado, e o original estará inalterado

Exemplo:
numbers = []
for i in range(1, 1001):
    numbers.append(i)

Usando compreensão de listas:
numbers = [i for i in range(1, 1001)]

E a seguir estão 8 exercíos feitos usando essa sintaxe.
Fonte: https://towardsdatascience.com/beginner-to-advanced-list-comprehension-practice-problems-a89604851313
"""

#Todos os exercíos envolvendos strings usam essas duas variáveis em sua solução
string = "Practice Problems to Drill List Comprehension in Your Head."
n_range = range(1,1000)

#1. Find all of the numbers from 1-1000 that are divisible by 8
# Encontre todos os números entre 1-1000 divisíveis por 8
numbers_1 = [num for num in n_range if num % 8 == 0]

#2. Find all the numbers from 1-1000 that have a 6 in them
# Encontre todos os números entre 1-1000 que contém 6
numbers_2 = [num for num in n_range if "6" in str(num)]

#3. Count the number of spaces in a string
# Conte o número de espaços em uma string
strings_1 = len([char for char in string if char == " "])

#4. Remove all of the vowels in a string
# Remova todas as vogais em uma string
vogais = ['a','e','i','o','u']
strings_2 = [char for char in string if char not in vogais]

#5. Find all of the words in a string that are less than 5 letters
# Encontre todas as palavras em uma string que tem menos de 5 letras
words = string.split(" ")
strings_3 = [char for char in words if len(char) < 5]

#6. Use a dictionary comprehension to count the length of each word in a sentence
# Use compreensão de dicionário para contar o tamanho de cada palavra em um sentença
dicts_1 = {word: len(word) for word in words}

#7. Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible
#by any single digit besides 1(2-9)
# Use a compreensão de listas aninhadas para encontrar todos os números de 1-1000 que são
#divisíveis por qualquer dígito além de 1(2-9)
nested_1 = [num for num in n_range if True in [True for div in range(2,10) if num % div == 0 ]]

#8. For all the numbers 1-1000, use a nested list/dictionary comprehension to find the
#highest single digit any of the numbers is divisible by
"""
qual o maior número capaz de dividir todos do conjunto?
for i in range(1,1000):
    for j in range of i:
        if i % j == 0:
            nested_2.append(j)
    
nested_2 = [[j for j in i if i % j == 0] for i in range(1,1000)]
"""
# Para todos os números 1-1000, use a compreensão de lista/dicionário para encontrar o
#maior número único capaz de dividir todos os números
nested_2 = {num:max([j for j in range(1,10) if num % j == 0]) for num in n_range}

if __name__ =='__main__':
    print("Aqui poderá conferir cada resultado das soluções dos exercícios")
    opcao = int(input("De 1 a 8, para cada exercício: "))
    match opcao:
        case 1:
            print(numbers_1)
        case 2:
            print(numbers_2)
        case 3:
            print(strings_1)
        case 4:
            print(strings_2)
        case 5:
            print(strings_3)
        case 6:
            print(dicts_1)
        case 7:
            print(nested_1)
        case 8:
            print(nested_2)
        
    
