# Exibe os número digitados ate o usuario digitar 0 em seguida some todos os números 
soma = 0
numero = int(input("Digite um número inteiro: "))

while numero != 0:
    soma += numero
    numero = int(input("Digite um número inteiro: "))

print("A soma dos números digitados é:", soma)

