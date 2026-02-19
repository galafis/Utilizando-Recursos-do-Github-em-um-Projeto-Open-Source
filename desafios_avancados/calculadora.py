def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        return a / b if b != 0 else "Erro: divisão por zero"
    else:
        return "Operação inválida"


if __name__ == '__main__':
    print(calcular(10, 2, "+"))
