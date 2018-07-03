#String
prefixo = "py"
prefixo  = prefixo + "thon"
print (prefixo[0 : 3])


string = 'Iuthan'
print (string[3:])

string = 'Iuthan'
print (string[:3])

#List

# Example 00
lista = ['Maria', 'josefa', 'toninho', 'juriscleide', 'betaniuda']
print (lista[1:3])


# Example 01
lista_one = ['banana', 'maça', "goiaba"]
lista.append(lista_one)
print (lista)

# Example 02
lista.insert(-1, lista_one)
print (lista)

# Example 03

list_two = ['cadeira', 'bolacha', 'arvore']
list_three = ['ovo', 'cebola', 'cenoura']

list_for = [list_two, list_three]
print (list_for)

# Example 04
a , b = 0 , 1
print (b)

while b < 10:
	print (b)
	a , b = b, a + b

Defining function
string = "Uma dia eu fui|maria foi na casa do joao|porta aberta|Eita"
def transforma_string(string):
	return string.split('|')

lista =  transforma_string(string)
print (lista)

numero = 10 


#If
palavra = str(input("Digite uma frase"))
if palavra == "banana":
    print("Acertou")
elif palavra == "nanana":
    print("Quase")
else:
    print("Errou") 

#For
palavras = ['gato','cachorro','papagaio']
for palavra in palavras:
	print(palavra, len(palavra))

#Caso queria manipular a lista dentro de um for e necessario usar [:],
#  isso faz uma copia da lista
for palavra  in palavras[:]:
	if len(palavra) > 6:
		palavras.insert(-1, palavra + "aumentou")
print(palavras)

#Range()
# Exemplo 01
for index in range(5):
  print (index)

# Exemplo 02
frutas = ['banana', 'maça', 'goiaba', 'melancia', 'laranja']
for index in range(5):
	print (frutas[index])

# Exemplo 03(inicio, fim, intervalo)
for index in range(-100, 10, 2):
	print (index)

# Exemplo 04
lista = list(range(10))
print (lista)

#Data structures


lista_original = ['banana', 'maca', 'goiaba', 'laranja', 'limao', 'manga']
lista_teste = ['miguel', 'angelica', 'italo', 'alex', 'priscila', 'joaquim']
variable = 'kiwi'

# append -- Adicione um item ao final da lista.
lista_original.append(variable)
print (lista_original)

# extend -- Estenda a lista anexando todos os itens do iterável
lista_original.extend(lista_teste)
print (lista_original)

# insert -- Insira um item em uma determinada posição.
lista_original.insert(0, 'batata')
print(lista_original)

# remove -- Remova o primeiro item da lista cujo valor é x
print(lista_original)
lista_original.remove('banana')
print(lista_original)

# pop -- Remova o item na posição dada na lista e devolva-o. 
			Caso não passe valor no parametro o ultimo valor e removido
print (lista_original)
lista_original.pop(1)
print (lista_original)

# clear -- Remova todos os itens da lista. Equivalente
print (lista_original)
lista_original.clear()
print (lista_original)

# index -- Retorna o índice baseado em zero na lista do primeiro item cujo valor é x
print(lista_original)
print (lista_original.index('maca'))

# count -- Retorna o número de vezes que x aparece na lista ou string.
string = 'eu eu fui na casa da minha vozinha'
print (string.count('eu'))
print (lista_original.count('banana'))

# sort -- Classifique os itens da lista no lugar
lista_original.sort()
print (lista_original)

# reverser -- Inverta os elementos da lista no lugar.
lista_original.reverse()
print (lista_original)
Devolva uma cópia superficial da lista
print (lista_original.copy())

print ('banana' in lista_original)

print ('|'.join(lista_original))
print (lista_original in 'banana')

#queue --Para implementar uma fila, use o collections
# .dequeque foi projetado para ter anexos rápidos
#  e pops de ambas as extremidades.
from collections import deque
queue = deque(['banana', 'maca', 'perâ'])
print(queue)
queue.append('goiaba')
print(queue)
queue.popleft()

#lista comprenssões
feira = ['pastel', 'verdura', 'frutas']
#Exemplo 00
feira = ['tio' + x for x in feira if x != 'verdura']
#Exemplo 01
quadrados = [x**2 for x in range(10)]
print(feira)
print(quadrados)

##Abordagens de lista aninhada
matriz = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

[print(linha) for linha in matriz]

##Dicionarios
values = {'jack': 'silva', 'marcos': 1234}
#Tecnicas de looping
for k, v in values.items():
	print (k,v)

for index, value in enumerate(['tic', 'tac', 'toe']):
	print (index, value)

frutas = ['banana', 'maça', 'goiaba']
verduras = ['rabanete', 'cenoura', 'batata']

#interar lista em paralelo
for fruta, verdura in zip(frutas, verduras):
    print(fruta, verdura)

string, string1, string2 = 'a', 'b', 'c'
eta = string or string1 or string2 
print (eta)


import modules
from modules import value
print (value)
modules.helloworld()
print (dir(modules))