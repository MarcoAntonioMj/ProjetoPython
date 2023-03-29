print('Programa que ler peso e a altura é indica se esta no peso ideal IMC')
altura = float(input("Digite a sua altura : "))
peso = float(input("Digite a seu peso : "))
altura = altura ** 2
imc = peso / altura
if imc < 18.5:
    print("O seu imc é  {:.1f} é abaixo do peso normal ".format(imc))
if imc > 18.5 and imc < 24.5:
    print("O seu imc é  {:.1f} e está  no peso normal ".format(imc))
if imc > 25.5 and imc < 29.9:
    print("O seu imc é   {:.1f} e está  em Excesso de peso ".format(imc))
if imc > 30.0 and imc < 34.9:
    print("O seu imc é   {:.1f} e está  obesidade classe 1  ".format(imc))
if imc > 35.0 and imc < 39.9:
    print("O seu imc é   {:.1f} e está  obesidade classe 2 ".format(imc))
if imc >= 40:
    print("O seu imc é   {:.1f} e está  obesidade classe 3 ".format(imc))
