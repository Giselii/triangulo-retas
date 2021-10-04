#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.
r1 = float(input('Valor da reta 1: '))
r2 = float(input('valor da reta 2: '))
r3 = float(input('valor da reta 3: '))

if ((r1 + r2) > r3) & ((r1 + r3) > r2) & ((r2 + r3) > r1):
    print('Temos um triângulo!!')
else:
    print('Não é possível existir um triângulo!')
