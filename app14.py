'''14. Faça um programa que leia 3 números e “diga” qual é o maior deles.'''

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: ")) 

if num1 > num2 and num1 > num3:
    print("O primeiro número digitado foi o maior")
elif num2 > num1 and num2 > num3:
    print("O segundo número digitado foi o maior")
else:
    print("O terceiro número digitado foi o maior")