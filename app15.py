'''15. Faça um programa que leia a idade de um nadador e classifique-o numa das seguintes categorias abaixo:
• Idoso (idade >= 65);
• Adulto (idade >= 21);
• Juvenil (idade >= 14);
• Infantil (idade >=9);
• Mirim (Idade < 9).'''

idade = int(input("Digite a idade do nadador: "))

if idade >= 65:
    print("Idoso")
elif idade >= 21:
    print("Adulto")
elif idade >= 14:
    print("Juvenil")
elif idade >= 9:
    print("Infantil")
else:
    print("Mirim")