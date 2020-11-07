'''
Preencha duas tuplas de 5 elementos cada com números aleatórios. Concatene as duas tuplas e
exiba a tupla resultante.
Exemplo:
Suponha que as tuplas com os números aleatórios sejam:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1)
Para estas tuplas, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1)
'''

from random import randint

tupla1 = ()
tupla2 = ()

for i in range(5):
    n = randint(1, 10)
    tupla1 = tupla1 + (n,)

    n = randint(1, 10)
    tupla2 = tupla2 + (n,)

print('Primeira Tupla:', tupla1)
print('Segunda Tupla:', tupla2)

tupla3 = tupla1 + tupla2
print('Tupla Resultante:', tupla3)
