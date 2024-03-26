#Calculator's Project

"""Create a simple calculator program that 
can perform basic arithmetic operations like addition,
subtraction, multiplication, and division. 
Allow the user to input two numbers 
and select an operation to performCreate a simple calculator
program that can perform basic arithmetic operations like:
addition, subtraction, multiplication,and division. 
Allow the user to input two numbers and select an operation to perform"""



n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
operacao = str(input("Digite a operação: ")).upper().strip()
if operacao == '+' or operacao == 'SOMA':
    print(f'Resultado: {n1} + {n2} = {n1+n2}')
if operacao == '-' or operacao == 'Subtração':
    print(f'Resultado: {n1} - {n2} = {n1-n2}')
if operacao == '*' or operacao == 'MULTIPLICAÇÃO':
    print(f'Resultado: {n1} * {n2} = {n1*n2}')
if operacao == '/' or operacao == 'DIVISÃO':
    print(f'Resultado: {n1} / {n2} = {n1/n2}')
simnao = str(input('Deseja fazer um novo calculo? ')).strip().lower()
while simnao == 'sim' or simnao == 's':
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    operacao = str(input("Digite a operação: ")).upper().strip()
    if operacao == '+' or operacao == 'SOMA':
        print(f'Resultado: {n1} + {n2} = {n1+n2}')
    if operacao == '-' or operacao == 'Subtração':
        print(f'Resultado: {n1} - {n2} = {n1-n2}')
    if operacao == '*' or operacao == 'MULTIPLICAÇÃO':
        print(f'Resultado: {n1} * {n2} = {n1*n2}')
    if operacao == '/' or operacao == 'DIVISÃO':
        print(f'Resultado: {n1} / {n2} = {n1/n2}')
    simnao = str(input('Deseja fazer um novo calculo? ')).strip().lower()
    