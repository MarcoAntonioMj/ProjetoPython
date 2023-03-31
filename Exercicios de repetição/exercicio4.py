# Lê o número da tabuada
numero = int(input("Digite um número para exibir a tabuada de multiplicação: "))

# Loop para exibir a tabuada de multiplicação
for i in range(1, 11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)


