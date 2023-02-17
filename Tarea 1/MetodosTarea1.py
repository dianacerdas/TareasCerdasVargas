import math  # Se importa la librería math  para utilizar el valor de pi
# FUNCIÓN DIVIDE_STRING

# Funcionalidad: Toma un string como entrada y un entero. Dependiendo del
# valor del entero va a realizar dos operaciones distintas en el string.
# En caso de que el entero sea igual a 1, entonces separa el string en dos
# grupos, uno en el que se tienen las mayúsculas y los números y otra en
# la que se tienen las minúsculas y los símbolos. En caso de que el entero
# sea igual a 2, entonces se divide el string por la mita y en caso de que
# la cantidad de caracteres sea impar, la parte 1 contiene la mayoría de los
#  caracteres.
# Entradas: str(frase), int(opcion)
# salidas str(part1), str(part2)


def divide_string(Frase, Operacion):
    part1 = ""  # Variables de salida
    part2 = ""

    # Verifica que la frase sea un string
    if not type(Frase) == str:
        print("La frase no es string")
        return 0  # Código único para este caso

    # Verificar que Operacion sea un número entero
    if not type(Operacion) == int:
        print("No es entero")  # Si no es entero envía por consola este mensaje
        return 1  # Código único para este caso

    # Separa el string en dos grupos: 1.Mayusculas con números
    # 2. Minusculas con símbolos
    if Operacion == 1:
        print("Operacion 1")
        for letter in Frase:  # Recorre caracter por caracter la frase
            if letter.isalpha():  # Determina si es una letra
                if letter.islower():  # Si es minuscula la pone en part2
                    part2 += letter
                elif letter.isupper():  # Si es mayuscula se coloca en part1
                    part1 += letter
            elif letter.isnumeric():  # Si es un numero lo agrega a la part1
                part1 += letter
            else:  # Si son caracteres especiales los agrega a la part2
                part2 += letter

# Divide el string por la mitad, en caso de ser impar la primera mitad tendrá
# la mayor cantidad de caracteres
    elif Operacion == 2:
        print("Operacion 2")
        i = 1  # Contador que inicia en 1 para saber la cantidad de letras

    # El siguiente if/else define el numero de caracter en el que se debe
    # detener la parte 1
        if len(Frase) % 2 == 0:
            cambio = len(Frase) / 2
        else:
            cambio = ((len(Frase) - 1) / 2) + 1

    # For va caracter por caracter asignando a la parte 1 hasta que el contador
    # llega al valor definido anteriormente, luego se comienzan a asignar en
    # la parte 2
        for letter in Frase:
            if i <= cambio:
                part1 += letter
            else:
                part2 += letter
            i += 1


# Si no se da una operacion conocida (entero diferenete de 1 o 2)
    else:
        print("No se conoce la operación")
        return 2  # Código único para este caso

    return part1, part2  # Resultados de la función

# FUNCIÓN MEASURE_AREA

# Funcionalidad: Recibe un valor entero y calcula el área de un círculo y
# cuadrado, tomando el valor entero como el lado y radio respectivamente.
# Entradas: int(valor)
# salidas areaCirculo, areaCuadrado


def measure_area(valor):

    # Inicializa los valores necesarios en al función
    cuadrado = 0
    circulo = 0

    # Verificar que el valor sea un número entero
    if not type(valor) == int:
        print("No es entero")
        return 1

    pi = math.pi  # Define el valor de pi
    cuadrado = valor * valor  # Calculo del área del cuadrado
    circulo = pi * cuadrado  # Calculo del área del círculo
    print("El área del cuadrado es " + str(cuadrado))
    print("El área del circulo es " + str(circulo))

    return cuadrado, circulo  # Salida de la función
    print(divide_string("StringValido 1234", 2))
