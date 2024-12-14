class ClimaSemanal:
    def __init__(self):
        # Lista para almacenar temperaturas diarias
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("Introduce las temperaturas diarias (en °C):")
        for i in range(7):  # Semana tiene 7 días
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        # Cálculo del promedio semanal
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    # Crear una instancia de la clase ClimaSemanal
    clima = ClimaSemanal()

    # Ingresar temperaturas
    clima.ingresar_temperaturas()

    # Calcular y mostrar el promedio semanal
    promedio = clima.calcular_promedio()
    print(f"\nEl promedio semanal de temperaturas es: {promedio:.2f} °C")

# Llamada al programa principal
if __name__ == "__main__":
    main()
