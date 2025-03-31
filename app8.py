'''8. Faça programa que leia uma temperatura em graus Kelvin, calcular e escrever o valor correspondente em graus Fahrenheit e Celsius.'''

kelvin = float(input("Digite a temperatura em Kelvin: "))

celsius = kelvin - 273.15

fahrenheit = (celsius * 9/5) + 32 

print("A temperatura em Celsius é:", celsius)
print("A temperatura em Fahrenheit é:", fahrenheit)