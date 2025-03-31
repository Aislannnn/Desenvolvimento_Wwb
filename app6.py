'''6. Faça programa que leia uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius e Kelvin.'''

fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

kelvin = celsius + 273.15

print("A temperatura em Celsius é:", celsius)
print("A temperatura em Kelvin é:", kelvin)