def calculate(operation: str):
    import re

    operation = operation.strip()

    if operation.lower() == 'c':
        print("Operación borrada.")
        return None

    tokens = tokenize(operation.replace(" ", ""))
    postfix = to_postfix(tokens)
    result = evaluate_postfix(postfix)

    # Si el resultado es un número entero exacto, retorna como int
    if result == int(result):
        return int(result)
    return result


def tokenize(expression):
    import re
    # Captura números con signo negativo y operadores
    pattern = r'(?<!\d)-?\d+\.?\d*|[+\-*/]'
    return re.findall(pattern, expression)


def to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []

    for token in tokens:
        if is_number(token):
            output.append(token)
        elif token in precedence:
            while operators and precedence.get(operators[-1], 0) >= precedence[token]:
                output.append(operators.pop())
            operators.append(token)
        else:
            raise ValueError(f"Token inválido: {token}")

    while operators:
        output.append(operators.pop())

    return output


def evaluate_postfix(postfix):
    stack = []

    for token in postfix:
        if is_number(token):
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("División por cero.")
                stack.append(a / b)

    return stack[0]


def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False