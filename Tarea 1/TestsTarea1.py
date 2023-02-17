# Se importan las funciones que se van a verificar
from MetodosTarea1 import divide_string, measure_area

# Se define una variable string para probar string_divide
Frase = "StringValido 1234"

# Se crea el test para comprobar que ambas opciones funcionan correctamente
# (1y2)


def test_divide_string_correcto():
    # Assert que verifica el resultado de la operación 1 utilizando str(Frase)
    assert divide_string(Frase, 1) == ("SV1234", "tringalido ")
    # Assert que verifica el resultado de la operación 2 utilizando str(Frase)
    assert divide_string(Frase, 2) == ("StringVal", "ido 1234")

# Se crea el test para comprobar que la función retorna el código de error
# asignado cuando la entrada no es de tipo string


def test_divide_string_errorstr():
    # Assert que verifica que si se ingresa un dato NO string la función
    # retorna el código de error 0
    assert divide_string(4820, 1) == 0

# Se crea el test para comprobar que la función retorna el código de error
# asignado cuando la entrada no es de tipo entero


def test_divide_string_errorint():
    # Assert que verifica que si se ingresa un dato NO int la función
    # retorna el código de error 1
    assert divide_string(Frase, "AABB") == 1

# Se crea el test para comprobar que la función measure_area funciona
# correctamente


def test_measure_area_correcto():
    # Assert que verifica que el área del cuadrado y del círculo sean
    # calculadas correctamente con una entrada de 10
    assert measure_area(10) == (100, 314.1592653589793)

# Se crea el test para comprobar que la función measure_area retorna el código
# de error asignado cuando la entrada no es de tipo entero


def test_measure_area_error():
    # Assert que verifica que si se ingresa un dato NO int la función
    # retorna el código de error 1
    assert measure_area("aaa") == 1
