#Calcular média de três  pessoas
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade de {}: ".format(nome1)))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade de {}: ".format(nome2)))

nome3 = input("Digite o nome da terceira pessoa: ")
idade3 = int(input("Digite a idade de {}: ".format(nome3)))

media_idades = (idade1 + idade2 + idade3) / 3

print("A média das idades é:", media_idades)
