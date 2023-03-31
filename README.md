# ProjetoPython

## Repositório para treinar Python. Neste repositório, irei aprender e treinar Python, usando como base a lógica de programação que aprendi com Java.
"Irei criar 15 questões, 5 de exercícios sequenciais, 5 de repetição e 5 de condicionais.

## 5 exercicios sequenciais :

- Faça um programa que solicite ao usuário dois números e exiba a soma deles.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20sequencial/Exercicio1.py)
- Crie um programa que peça a idade do usuário e exiba a quantidade de dias que ele já viveu.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20sequencial/Exercicio1.py)
- Escreva um programa que calcule a área de um triângulo, solicitando ao usuário a base e a altura.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20sequencial/Exercicio3.py)
- Faça um programa que leia o nome e a idade de três pessoas e exiba a média das idades.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20sequencial/Exercicio4.py)
- Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20sequencial/Exercicio5.py)

## 5 Exercícios de repetição:

- Faça um programa que imprima todos os números pares de 0 a 100.
- Escreva um programa que solicite ao usuário números inteiros até que ele digite 0. Em seguida, exiba a soma dos números digitados.
- Crie um programa que leia o nome e 3 notas de cinco alunos e exiba a média de cada um.
- Faça um programa que exiba a tabuada de multiplicação de um número informado pelo usuário, de 1 a 10.
- Escreva um programa que leia números inteiros positivos do usuário e exiba a média deles, até que o usuário digite um número negativo.

## 5 Exercícios de condicional:

- Faça um programa que leia a idade do usuário e informe se ele pode ou não dirigir.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20condicional/Exercicio-condicional1.py)
- Crie um programa que solicite ao usuário um número inteiro e informe se ele é par ou ímpar.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20condicional/Exercicio-condicional2.py)
- Escreva um programa que solicite ao usuário um número e informe se ele é positivo, negativo ou zero.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20condicional/Exercicio-condicional3.py)
- Faça um programa que leia o peso e a altura de uma pessoa e informe se ela está ou não dentro do peso ideal (IMC entre 18,5 e 25).[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20condicional/Exercicio-condicional4.py)
- Crie um programa que solicite ao usuário a idade e a altura de uma pessoa e informe se ela pode ou não entrar em um brinquedo de parque de diversões.[clique aqui para ver a resposta](https://github.com/MarcoAntonioMj/ProjetoPython/blob/main/Exercicios%20condicional/Exercicio-condicional5.py)

## EXEMPLO DE SINTAXE EM PYTHON
```
# Exemplo de estrutura básica em Python

# Exercício de sequencial
# Solicita dois números ao usuário e exibe a soma deles
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
soma = num1 + num2
print("A soma é:", soma)

# Exercício de repetição
# Exibe todos os números pares de 0 a 100
for i in range(0, 101, 2):
    print(i)

# Exercício de condicional
# Verifica se um número digitado pelo usuário é par ou ímpar
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```
## Programar em Python usando o Visual Studio Code
- Certifique-se de ter o Python instalado no seu computador. Você pode baixá-lo gratuitamente em python.org.

- Baixe e instale o Visual Studio Code em code.visualstudio.com.

- Abra o Visual Studio Code e crie um novo arquivo Python. Para fazer isso, vá em "File" (Arquivo) > "New File" (Novo arquivo) ou use o atalho "Ctrl+N" (Windows) ou     "Cmd+N" (Mac).

- Salve o arquivo com a extensão .py. Para fazer isso, vá em "File" (Arquivo) > "Save As" (Salvar como) e digite o nome do arquivo com a extensão .py (por exemplo,       "meu_programa.py").

- Comece a escrever o seu código Python no arquivo. O Visual Studio Code irá fornecer sugestões de código e erros em tempo real para ajudar a escrever código correto.

 - Para executar o seu programa Python, pressione "F5" ou vá em "Run" (Executar) > "Start Debugging" (Iniciar depuração). O Visual Studio Code irá executar o seu programa e mostrar a saída no terminal.

 ## Extensão Vscode para Python
   instalar extensões do Visual Studio Code para Python para obter recursos adicionais, como IntelliSense, linting e depuração avançada.
 ## IntelliSense :
 
IntelliSense é um recurso de autocompletar código que está disponível em muitos editores de código, incluindo o Visual Studio Code. Ele ajuda os desenvolvedores a escrever código mais rapidamente e com menos erros, fornecendo sugestões de código em tempo real enquanto o código está sendo digitado.
O IntelliSense funciona analisando o código que está sendo escrito e sugerindo a conclusão automática de palavras-chave, nomes de variáveis, métodos e funções relevantes. Ele também pode exibir informações contextuais sobre os itens sugeridos, como uma breve descrição do que eles fazem ou quais são seus parâmetros.

## linting :

Linting é um processo de análise estática de código que verifica automaticamente o código fonte em busca de problemas de formatação, erros de sintaxe, erros lógicos e outros problemas que possam afetar a qualidade do código. O objetivo do linting é ajudar a garantir que o código seja consistente, legível e fácil de manter.

Os linters podem ser usados em várias linguagens de programação e geralmente são executados durante a compilação ou antes da execução do código. Eles analisam o código fonte e procuram por problemas comuns, como variáveis não declaradas, declarações de retorno ausentes, espaços em branco desnecessários e muitos outros.

O linting é útil porque pode ajudar a encontrar erros de código antes que o programa seja executado, o que pode economizar muito tempo e esforço na depuração e correção de erros. Ele também pode ajudar a garantir que o código seja fácil de ler e entender, o que é especialmente importante em projetos grandes e complexos, onde várias pessoas podem estar trabalhando no mesmo código.

# O que eu aprendi fazendo a primeira lista :

## O comando input() : 
input(): a função input() é usada para solicitar ao usuário uma entrada a partir do teclado. Ela retorna uma string.
```
nome = input("Digite o seu nome: ")
```
## A função int : 
int(): a função int() é usada para converter uma string em um número inteiro.
```
idade = int(input("Digite a sua idade: "))
```
## O método  .format() :
 o método .format() é usado para formatar uma string, inserindo valores em espaços reservados por chaves {}. Os valores são passados como argumentos na ordem em que aparecem nas chaves.
 ```
nome = "João"
idade = 25
print("O meu nome é {} e eu tenho {} anos".format(nome, idade))
```
# O que eu aprendi fazendo a  lista de condicional :
## O comando if :
```
if condicao:
    # bloco de codigo a ser executado se a condicao for verdadeira
```
O if é uma estrutura condicional em Python que permite que um bloco de código seja executado apenas se uma determinada condição for verdadeira.
Ou seja, se a condição especificada após o if for verdadeira, o bloco de código indentado abaixo do if será executado. Caso contrário, o bloco de código não será executado.

Além disso, o if pode ser combinado com outras estruturas condicionais, como o else e o elif. A sintaxe completa fica assim:
```
if condicao1:
    # bloco de codigo a ser executado se a condicao1 for verdadeira
elif condicao2:
    # bloco de codigo a ser executado se a condicao2 for verdadeira e a condicao 1 for falsa
else:
    # bloco de codigo a ser executado se todas as condicoes anteriores forem falsas
```
## O comando float :
```
float é um tipo de dado em Python que representa números de ponto flutuante, ou seja, números com casas decimais.
x = float("3.14")
print(x) # exibe 3.14
```
## Indentação 
a indentação é usada para delimitar blocos de código, e a indentação do bloco if e dos blocos elif e else devem estar alinhados.
É recomendado utilizar quatro espaços em branco para a indentação em Python. Por exemplo:
```
if condicao:
    # bloco de codigo dentro do if, com 4 espaços de indentacao
    # aqui vao as instrucoes a serem executadas se a condicao for verdadeira
elif outra_condicao:
    # bloco de codigo dentro do elif, com 4 espaços de indentacao
    # aqui vao as instrucoes a serem executadas se a outra condicao for verdadeira
else:
    # bloco de codigo dentro do else, com 4 espaços de indentacao
    # aqui vao as instrucoes a serem executadas se todas as condicoes anteriores forem falsas
```
