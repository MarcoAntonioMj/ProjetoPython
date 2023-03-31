# Inicializa a soma e o contador
soma = 0
contador = 0

# Loop para ler os números
while True:
    # Lê o número do usuário
    numero = int(input("Digite um número inteiro positivo (ou um número negativo para sair): "))
    
    # Sai do loop se o número for negativo
    if numero < 0:
        break
    
    # Atualiza a soma e o contador
    soma += numero
    contador += 1

# Verifica se foi digitado pelo menos um número positivo
if contador > 0:
    # Calcula a média e exibe o resultado
    media = soma / contador
    print("A média dos números positivos é:", media)
else:
    print("Nenhum número positivo foi digitado.")












# Exemplo de loop while que executa 5 iterações
#contador = 0
#while contador < 5:
    # Código que será executado em cada iteração
    #print("Iteração", contador)
    #contador += 1


