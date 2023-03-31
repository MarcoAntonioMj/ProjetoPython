for i in range(5):
    # Lê o nome do aluno
    nome = input("Digite o nome do aluno " + str(i+1) + ": ")
    
    # Lê as três notas do aluno
    nota1 = float(input("Digite a primeira nota do aluno " + nome + ": "))
    nota2 = float(input("Digite a segunda nota do aluno " + nome + ": "))
    nota3 = float(input("Digite a terceira nota do aluno " + nome + ": "))
    
    # Calcula a média do aluno
    media = (nota1 + nota2 + nota3) / 3.0
    
    # Exibe a média do aluno
    print("A média do aluno", nome, "é:", media)




