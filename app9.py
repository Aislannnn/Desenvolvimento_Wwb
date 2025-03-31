'''9. Faça um programa que leia o salário de um funcionário e o percentual de aumento, calcule e mostre o valor do aumento e o novo salário.'''

salario = float(input("Digite o salário: "))
aumento = float(input("Digite o percentual de aumento: ")) / 100

aumento_salario = salario * aumento

novo_salario = salario + aumento_salario

print("O aumento do salário foi de:", aumento_salario)
print("O novo salário é:", novo_salario)