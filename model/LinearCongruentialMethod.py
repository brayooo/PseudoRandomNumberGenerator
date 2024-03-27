import numpy as np

from model.Utils.MathUtils import MathUtils


class LinearCongruentialMethod:
    """
    Esta clase implementa el Método de Congruencia Lineal para la generación de números pseudoaleatorios.
    """

    def __init__(self, xo, k, c, g, min_value, max_value, total_iterations):
        """
        Este es el método constructor de la clase LinearCongruentialMethod.

        Parámetros:
            xo (int): Valor inicial de la semilla.
            k (int): Varible utilizada para calcular el multiplicador.
            c (int): Incremento.
            g (int): Varible utilizada para calcular la m.
            min_value (int): Valor mínimo para el rango de los números generados.
            max_value (int): Valor máximo para el rango de los números generados.
            total_iterations (int): Número total de iteraciones o números a generar.
        """
        self.ni_values = []
        self.ri_values = []
        self.xi_values = []
        self.xo = xo
        self.a = 1 + (2 * k)
        self.c = c
        self.g = g
        self.m = np.power(2, g)
        self.min = min_value
        self.max = max_value
        self.total_iterations = total_iterations

    def generate_numbers_tested(self):
        """
        Genera números Ri filtrados y asegura no exceder el total de iteraciones.
        Actualiza la semilla y el módulo si es necesario.
        """
        ri_result = []
        while len(ri_result) < self.total_iterations:
            ri = self.filter_ri_numbers(self.generate_numbers_by_linear_congruential(100))
            ri_result.extend(ri[:self.total_iterations - len(ri_result)])  # Asegurar no exceder total_iterations
            self.xo += 100
            if self.m <= self.xo:
                while self.m <= self.xo:
                    self.g += 1
                    self.m = np.power(2, self.g)
        self.ri_values = ri_result
        self.create_ni_values()


    def generate_numbers_by_linear_congruential(self, iterations):
        """
        Genera números pseudoaleatorios Ri utilizando el método de congruencia lineal.

        Parámetros:
            iterations (int): Número de iteraciones para generar números Ri.

        Retorna:
            list: Lista de números Ri generados.
        """
        xi = self.xo
        self.ri_values.clear()
        for _ in range(iterations):
            xi = (self.a * xi + self.c) % self.m
            ri = xi / (self.m - 1)
            self.xi_values.append(MathUtils.truncate(xi))
            self.ri_values.append(MathUtils.truncate(ri))
        return self.ri_values

    def create_ni_values(self):
        """
        Crea y almacena los valores Ni a partir de los valores Ri generados.
        """
        for ri in self.ri_values:
            ni = self.min + (self.max - self.min) * ri
            self.ni_values.append(MathUtils.truncate(ni))

    def filter_ri_numbers(self, ri):
        """
        Filtra los números Ri para eliminar valores repetidos, cero, uno o negativos.

        Parámetros:
            ri (list): Lista de números Ri a filtrar.

        Retorna:
            list: Lista de números Ri filtrados.
        """
        first = ri[0]
        result = []
        for number in ri[1:]:  # Comienza desde el segundo elemento
            if number == first or number in {0.0, 1.0} or '-' in str(number):
                # Detiene el bucle si encuentra una repetición del primer elemento
                # o si el número es 0.0, 1.0 o negativo.
                continue
            result.append(MathUtils.truncate(number))
        return result

    def get_xi_values_array(self):
        """
        Devuelve el arreglo de valores Xi generados.

        Retorna:
            list: Lista de valores Xi.
        """
        return self.xi_values

    def get_ri_values_array(self):
        """
        Devuelve el arreglo de valores Ri generados.

        Retorna:
            list: Lista de valores Ri.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
        Devuelve el arreglo de valores Ni generados.

        Retorna:
            list: Lista de valores Ni.
        """
        return self.ni_values
