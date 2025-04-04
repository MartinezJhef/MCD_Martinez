class CalculadoraMCD:
    def __init__(self, a=None, b=None):
        """
        Inicializa la calculadora de MCD con dos números enteros positivos.

        Args:
        a (int): Primer número entero positivo (opcional).
        b (int): Segundo número entero positivo (opcional).
        """
        self._a = a
        self._b = b

    @property
    def a(self):
        """Getter para el primer número."""
        return self._a

    @a.setter
    def a(self, valor):
        """Setter para el primer número con validación."""
        valido, num = self.validar_numero(valor)
        if valido:
            self._a = num

    @property
    def b(self):
        """Getter para el segundo número."""
        return self._b

    @b.setter
    def b(self, valor):
        """Setter para el segundo número con validación."""
        valido, num = self.validar_numero(valor)
        if valido:
            self._b = num

    def validar_numero(self, num):
        """
        Valida si el número ingresado es un entero positivo.

        Args:
        num: Valor a validar.

        Returns:
        tuple: (bool, int) donde bool indica si es válido y int es el número validado.
        """
        try:
            num = int(num)
            if num <= 0:
                print("Por favor, ingrese un número entero positivo.")
                return False, None
            return True, num
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            return False, None

    def calcular_mcd(self):
        """
        Calcula el Máximo Común Divisor (MCD) de los números almacenados.

        Returns:
        int: El MCD de los números, o None si no se han establecido ambos números.
        """
        if self._a is None or self._b is None:
            print("Error: Ambos números deben estar establecidos.")
            return None

        a = self._a
        b = self._b
        while b != 0:
            a, b = b, a % b
        return a

    def solicitar_numeros(self):
        """Solicita al usuario que ingrese los dos números enteros positivos."""
        while True:
            entrada = input("Ingrese el primer número entero positivo: ")
            valido, num = self.validar_numero(entrada)
            if valido:
                self._a = num
                break

        while True:
            entrada = input("Ingrese el segundo número entero positivo: ")
            valido, num = self.validar_numero(entrada)
            if valido:
                self._b = num
                break


# Ejemplo de uso
if __name__ == "__main__":
    calculadora = CalculadoraMCD()

    # Opción 1: Establecer números mediante setters
    # calculadora.a = input("Ingrese el primer número entero positivo: ")
    # calculadora.b = input("Ingrese el segundo número entero positivo: ")

    # Opción 2: Solicitar números interactivamente
    calculadora.solicitar_numeros()

    # Calcular y mostrar el MCD
    mcd = calculadora.calcular_mcd()
    if mcd is not None:
        print(f"El Máximo Común Divisor de {calculadora.a} y {calculadora.b} es: {mcd}")