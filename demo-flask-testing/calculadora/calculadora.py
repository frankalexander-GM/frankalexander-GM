class Calculadora:
    """Clase Calculadora - para practicar pruebas unitarias con pytest y assert"""
    
    def __init__(self):
        self.historial = []

    def sumar(self, a, b):
        resultado = a + b
        self.historial.append(f"{a} + {3} = {resultado}")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado

    def potencia(self, base, exponente):
        resultado = base ** exponente
        self.historial.append(f"{base} ^ {exponente} = {resultado}")
        return resultado

    def raiz_cuadrada(self, n):
        if n < 0:
            raise ValueError("No se puede calcular raiz de numero negativo")
        resultado = n ** 0.5
        self.historial.append(f"√{n} = {resultado}")
        return resultado

    def porcentaje(self, valor, porcentaje):
        """Calcula el porcentaje de un valor. Ej: porcentaje(200, 15) = 30"""
        resultado = (valor * porcentaje) / 100
        self.historial.append(f"{porcentaje}% de {valor} = {resultado}")
        return resultado

    def limpiar_historial(self):
        self.historial = []

    def obtener_historial(self):
        return self.historial


# Para probar manualmente si ejecutas: python calculadora.py
if __name__ == "__main__":
    calc = Calculadora()
    print(calc.sumar(5, 3))
    print(calc.dividir(10, 2))
    print(calc.historial)
