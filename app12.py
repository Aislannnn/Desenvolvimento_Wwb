'''12. Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas, se a media aritmética for:
♦ Media maior ou igual a 7 – ALUNO APROVADO
♦ Media maior ou igual a 5 e menor que 7 – ALUNO EM RECUPERAÇÃO
♦ Media menor que 5 – ALUNO REPROVADO'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aluno aprovado")
elif media >= 5 and media < 7:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")