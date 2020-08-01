# Quem tem medo dos dados?#2

Nesse segundo ep vimos um pouco sobre as estruturas de dados: listas

# formas de iniciar uma lista vazia
lista_a = list()
lista_b = []

# formas de iniciar um dict
dicio_a = dict()
dicio_b = {}

lista_a = list(range(1,100,2))

# pode acrescentar elementos no final da lista
lista_a.append(101)
print(lista_a)

# mas se você quer inserir em um local especifico use insert
lista_a.insert(1,2)
print(lista_a)

# poutz, eu coloquei duas vezes o 2 ali, e agora? Vai excluir o primeiro objeto que corresponder c/ o que você passou
lista_a.remove(2)

# com o pop retiramos o elemento passando a posição dele
lista_a.pop(1)

print(lista_a)



Para acessar os atributos e métodos: obj.<PRESSIONE TAB>
Importante lembrar que Listas são mutáveis, diferentemente das Tuplas que são imutáveis.

As duplas podem ser definidas de duas formas diferentes, sendo a primeira mais usual:

tupla_1 = (1,2,3,4,5)
type(tupla_1)

tupla_2 = 6,7,8,9,10
type(tupla_2)

Como conversamos, muitas pessoas não sabem, mas existe sim arrays em python:

import array

array_1 = array.array('d', [2.7,3.4,3.5])

array_2 = array.array('b', [2,7,3,4,3,5])

array_1.pop(1)
print(array_1)

array_2.reverse()
print(array_2)

