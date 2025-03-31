'''16. Faça um programa que leia dois números e efetua a adição. Se o valor somado for maior que 20, este deverá ser apresentado somando-se a ele 8; se o valor somado for menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2  

if soma > 20:
    print("O resultado da soma foi:", soma + 8)
else:
    print("O resultado da soma foi:", soma - 5)