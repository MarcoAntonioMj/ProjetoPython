print('Programa para ver se tem altura e a idade necessaria para entrar no brinquedo : ')
altura = float(input("Digite a sua altura : "))
idade = float(input("Digite a sua idade : "))
if altura < 1.60 or idade < 15:
    print("Não pode entrar ")
else:
    print("Pode entrar")
