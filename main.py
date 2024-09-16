### Calculadora do Macauli ###

digite = input("""""
    Digite quais das operações deseja realizar!: 
    [+] Soma
    [-] Subtração
    [*] Multiplicação
    [/] Divisão               
    [f] Encerrar              
    """"")

def soma():
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    result = a + b
    print(f"O resultado da soma de {a} + {b} é: ",result)
    


def subtracao():
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    result = a - b
    print(f"O resultado da subtração de {a} - {b} é: ",result)

def multiplicacao():
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    result = a * b
    print(f"O resultado da multiplicação de {a} * {b} é: ",result)

def divisao():
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))
    result = a / b
    print(f"O resultado da divisão de {a} / {b} é: ",result)

def encerrar():
    print("Código encerrado")
    
    


if digite == "+":
    soma()
elif digite == "-":
    subtracao()
elif digite == "*":
    multiplicacao()
elif digite == "/":
    divisao()
elif digite == "f":
    encerrar()
else:
    print("Operação invalida seu animal")



    





    
    