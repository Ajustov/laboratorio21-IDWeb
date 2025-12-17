class OperadorInvalidoError(Exception):
    pass

operacion = input("Ingresa la operación (ej: 10 / 2): ")

try:
    partes = operacion.split()
    num1 = float(partes[0])
    operador = partes[1]
    num2 = float(partes[2])

    if operador not in ["+", "-", "*", "/"]:
        raise OperadorInvalidoError("Operador inválido")

    if operador == "+":
        print(num1 + num2)
    elif operador == "-":
        print(num1 - num2)
    elif operador == "*":
        print(num1 * num2)
    elif operador == "/":
        if num2 == 0:
            raise ZeroDivisionError("No se puede dividir entre cero")
        print(num1 / num2)

except ValueError:
    print("Error: valores inválidos")
except ZeroDivisionError as e:
    print("Error:", e)
except OperadorInvalidoError as e:
    print("Error:", e)



