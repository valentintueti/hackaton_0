def calculate(operation: str) -> float:
    info = operation.split()
    if len(info) != 3:
        raise ValueError("Operación no válida. Usa el formato: número operador número (ej. 2 + 2)")

    a = float(info[0])
    b = float(info[2])
    op = info[1]

    if op == "+":
        return suma(a, b)
    elif op == "-":
        return resta(a, b)
    elif op == "*":
        return multiplicacion(a, b)
    elif op == "/":
        return division(a, b)
    else:
        raise ValueError("Operador no reconocido")


def suma(a, b):
    return a + b

def resta(a, b):
    return a - b