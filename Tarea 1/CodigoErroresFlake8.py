# Funcionalidad: Este código obtiene los valores de corriente y potencia para
# un componente resistivo a partir de su valor y del voltaje en ella.
# Entradas: int(voltaje) e int(resistencia)
# Salidas: float(corriente) e float(potencia)

def PruebaCorrientePotencia(voltaje, resistencia):
    corriente = 0  # Se definen las salidas de la función
    potencia = 0
    if resistencia == 0:  # Verificación de división por cero
        return 5  # Error de división por cero
    else:
        corriente = voltaje / resistencia  # Calculo de corriente Ley de Ohm
        potencia = voltaje*corriente  # Calculo de potencia
        return corriente, potencia  # Resultados de la función
