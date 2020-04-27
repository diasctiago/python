# -*- coding: utf-8 -*-

# importando bibliotecas
import sys

input ('Pressione ENTER para iniciar...')
print ('\n')
calc = input ('Qual cáculo deseja realizar? \n1 - Até que idade eu tenho dinheiro?\n2 - Quanto de despesas até os 100 anos?\n3 - Quanto preciso guardar para ter o valor desejado?\n4 - Quanto de poupança preciso para viver até os 100 anos? \n')

# FÓRMULA JUROS SIMPLES
# M = C * i * t
# M é o montante final obtido na aplicação
# i é a taxa de juros aplicada, em porcentagem
# C é o capital ou valor inicial aplicado
# t é o tempo total da aplicação.

# FÓRMULA JUROS COMPOSTOS
# M = C * (1 + i)**t
# M é o montante final obtido na aplicação
# i é a taxa de juros aplicada, em porcentagem
# C é o capital ou valor inicial aplicado
# t é o tempo total da aplicação.

despesas = int(input('Informe o valor de suas despesas anuais: '))
poupanca = int(input('Informe o valor de sua poupança hoje: '))
idade = int(input('Informe a sua idade: '))
taxa = 0.12
inflacao = 0.0637
desejado = int(input('Informe o valor desejado aos 100 anos: '))

# O saldo da Poupança está sendo atualizado com taxa de 6% a.a (Percentual de rendimentos da poupança) que facilmente pode ser encontrada no mercado investimentos de baixo risco com taxa melhores, mas o valor das despensa está sendo corrigido com uma taxa de inflação anual de 3,98% (média da inflação no ano de 2019) taxa que está de certa forma otimista e pode subir com o passar dos anos.
p = poupanca
d = despesas
i = idade
while calc == '1' and p >= d  and i < 100:
	s = p - d
	print( 'Saldo da poupança com ' , i, ' anos é de ' , '%.2f' % s )
	p = s * (1 + taxa)
	d = d * (1 + inflacao)
	i = i + 1
	print( 'Saldo da poupança para ' , i, ' anos é de ' , '%.2f' % p  )
	print( 'O valor das despesas para ' , i, ' anos é de ' , '%.2f' % d )
	print( '\n'  )

# Quanto de despesas até os 100 anos?
a = idade
c = despesas
t = 1
while calc == '2' and a <= 100:
    print ( 'O valor das despesas acumulado para ' , a, ' anos é de ' , '%.2f' % c )
    c = c + (despesas * (1 + inflacao)**t)
    a = a + 1
    t = t + 1

# Quanto preciso guardar com a idade de hoje para ter aos 100 anos
v = desejado    
if calc == '3':
    valor = v / ( (1 + taxa) ** (100 - idade) )
    print ('\n')
    print(' O valor necessário aos ', idade, ' anos é de ' , '%.2f' % valor )

# Quanto eu preciso ter de Poupança para viver até os 100 anos?
k = 0
inicial = 0
time = 0
saldo = 0
while calc == '4' and time < 100:
    k = inicial + 1000
    inicial = k
    x = idade
    y = despesas
    while k >= y and x <= 100:
        saldo = k - y
        k = saldo * (1 + taxa)
        y = y * (1 + inflacao)
        x = x + 1
        time = x

if calc == '4':
    print ('\n')
    print('O valor inicial de poupança é ', '%.2f' % inicial, ' para uma despesa anual de ', despesas, ' aos ', idade, ' anos.' )

print ('\n')
input ('Pressione ENTER para finalizar...')
sys.exit()
