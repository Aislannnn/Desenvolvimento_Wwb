'''7. Faça programa que leia uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit e Kelvin.'''

celsius = float(input("Digite a temperatura em celsius: "))

fahrenheit = (celsius * 9/5) + 32

kelvin = celsius + 273.15

print("A temperatura em farenheit é:", fahrenheit)
print("A temperatura em Kelvin é:", kelvin)