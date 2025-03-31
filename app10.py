'''10. Faça um programa que leia um número, verifique se este número é positivo ou negativo. Se for negativo mostre a mensagem "Você digitou um numero negativo", Senão mostre:" Você digitou um número positivo.'''

numero = float(input("Digite um número: "))

if numero < 0:
    print(" Vocé digitou um número negativo")
else:
    print(" Vocé digitou um número positivo")