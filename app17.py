'''17. Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor da compra for menor que 20,00; caso contrário, o lucro será de 30%. Ler o valor do produto e imprimir o valor da venda, conforme as taxas do enunciado.'''

produto = float(input("Digite o valor do produto: "))

if produto < 20:
    venda = produto * 1.45
else:
    venda = produto * 1.30

print("O valor da venda foi:", venda)