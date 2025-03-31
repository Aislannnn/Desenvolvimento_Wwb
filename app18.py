# Pedir ao usuário a temperatura e a unidade de entrada
temperatura = float(input("Digite a temperatura: "))
entrada = input("Digite a unidade da temperatura inserida (Celsius, Fahrenheit ou Kelvin): ").strip().capitalize()
saida = input("Digite a unidade para a qual deseja converter (Celsius, Fahrenheit ou Kelvin): ").strip().capitalize()

# Conversão para Celsius
if entrada == "Fahrenheit":
    celsius = (temperatura - 32) * 5/9
elif entrada == "Kelvin":
    celsius = temperatura - 273.15
else:
    celsius = temperatura  # Se já for Celsius, mantém

# Converter para a unidade desejada
if saida == "Celsius":
    resultado = celsius
elif saida == "Fahrenheit":
    resultado = (celsius * 9/5) + 32
elif saida == "Kelvin":
    resultado = celsius + 273.15
else:
    print("Unidade de saída inválida!")
    exit()

# Exibir o resultado
print(f"A temperatura em {saida} é: {resultado:.2f}")
