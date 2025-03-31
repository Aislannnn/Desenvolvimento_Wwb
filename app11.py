'''11. Faça um programa que leia um número, verifique se este número é positivo, negative ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou zero”.'''

numero = float(input("Digite um número: "))

if numero < 0:
    print(" Vocé digitou um número negativo")
elif numero == 0:
    print(" Vocé digitou zero")
else:
    print(" Vocé digitou um número positivo")