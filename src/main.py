def calculate(operation:str) -> float:
    info = operation.split()
    a = info[0]
    b = info[2]

    op=info[1]

    if op=="+":
        suma(a,b)
    elif op=="-"
        resta(a,b)
    elif op=="*"
        multiplicacion(a,b)
    else:
        division(a,b)
    pass


def suma(a, b):
    return a + b

def division(a,b):
    return a / b

def resta(a, b):
    return a - b

def multiplicacion(a,b):
    return a * b
