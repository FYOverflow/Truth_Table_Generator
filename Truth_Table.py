from itertools import product  # Importar la función product de itertools
from tabulate import tabulate  # Importar la función tabulate de tabulate

# Pedir al usuario que ingrese la expresión
expression = input("Ingrese expresion> ")

if " " not in expression:
    if "," not in expression:
        table_data = []
        operators = {"^": " and ", "v": " or ", "-": " not ", "x": "!=", "|": "==", "/": "<="}
        
        # "^" and
        # "v" or
        # "-" not
        # "x" xor
        # "/" implication
        # "|" if and only if

        # Separar del input las variables y la expresion
        variables = sorted({i for i in expression if i.isalpha() and i != "v" and i != "x"})
        print(variables)
        # Reemplazar el símbolo a letras
        expression2 = expression

        for i in expression:
            if i in operators:
                expression2 = expression2.replace(i, operators[i])

        var = product([True, False], repeat=len(variables))
        for combination in var:
            table = dict(zip(variables, combination))
            result = eval(expression2, table)
            table_data.append([table[var] for var in variables] + [result])

        # Agregando primero las variables y luego la expresión a los encabezados de la tabla
        headers = list(variables) + [expression]

        print(tabulate(table_data, headers=headers, tablefmt="double_grid"))

    elif "," in expression:  # Si hay una coma en la expresión (dos expresiones separadas por coma)
        expression = expression.split(",")  # Dividir las dos expresiones
        
        # Obtener las dos expresiones separadas
        expression_1 = expression[0]
        expression_2 = expression[1]


        table_data = []  # Lista para almacenar los resultados
        operators = {"^": " and ", "v": " or ", "-": " not ", "X": "!=", "|": "==", "/": "<="}  # Definir los operadores lógicos y sus equivalentes en Python

        # Obtener las variables de cada expresión
        variables_1 = {i for i in expression_1 if i.isalpha() and i != "v" and i != "x"}
        variables_2 = {i for i in expression_2 if i.isalpha() and i != "v" and i != "x"}

        # Reemplazar los símbolos de operadores por sus equivalentes en Python para cada expresión
        expression2_1 = expression_1
        expression2_2 = expression_2
        for i in expression_1:
            if i in operators:
                expression2_1 = expression2_1.replace(i, operators[i])
        for i in expression_2:
            if i in operators:
                expression2_2 = expression2_2.replace(i, operators[i])

        # Generar todas las combinaciones posibles de valores de verdad para las variables de ambas expresiones
        var_1 = product([True, False], repeat=len(variables_1))
        var_2 = product([True, False], repeat=len(variables_2))

        # Evaluar ambas expresiones para todas las combinaciones posibles de valores de verdad de las variables
        for combination_1, combination_2 in zip(var_1, var_2):
            table_1 = dict(zip(variables_1, combination_1))  # Crear un diccionario que mapea las variables con sus valores de verdad correspondientes para la primera expresión
            table_2 = dict(zip(variables_2, combination_2))  # Crear un diccionario que mapea las variables con sus valores de verdad correspondientes para la segunda expresión
            result_1 = eval(expression2_1, table_1)  # Evaluar la primera expresión con los valores de verdad actuales
            result_2 = eval(expression2_2, table_2)  # Evaluar la segunda expresión con los valores de verdad actuales
            table_data.append([result_1, result_2])  # Agregar los resultados a la lista de resultados

        # Impresión de tabla de resultados con variables
        headers = [expression_1, expression_2]
        print("Tabla de Resultados:")
        print(tabulate(table_data, headers=headers, tablefmt="double_grid"))  # Imprimir la tabla de resultados

        # Comparación de los resultados de las dos expresiones
        if all(x == y for x, y in table_data):
            print("Las expresiones son equivalentes lógicas.")  # Si todos los pares de resultados son iguales, las expresiones son equivalentes lógicamente
        else:
            print("Las expresiones no son equivalentes lógicas.")  # Si hay al menos un par de resultados diferentes, las expresiones no son equivalentes lógicamente
    else:
        print("Entre las expresiones añada una coma(todo sin espacios).")
else:
    print("Ingrese los datos sin espacios.")
