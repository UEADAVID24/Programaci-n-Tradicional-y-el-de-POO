# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Introduce las temperaturas diarias (en °C):")
    for i in range(7):  # Semana tiene 7 días
        temp = float(input(f"Día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f} °C")

# Llamada al programa principal
if __name__ == "__main__":
    main()


