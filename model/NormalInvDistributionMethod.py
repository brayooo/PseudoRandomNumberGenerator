import math

from scipy.stats import norm


class NormalInvDistributionMethod:
    """
        Esta clase implementa el método de distribución inversa normal para generar números pseudoaleatorios.
    """

    def __init__(self, intervals_amount, mean, standard_deviation, ri_values):
        """
        Inicializa una instancia de la clase NormalInvDistributionMethod.

        Parámetros:
            intervals_amount (int): Número de intervalos para la distribución.
            mean (float): Media de la distribución normal.
            standard_deviation (float): Desviación estándar de la distribución normal.
            ri_values (list): Lista de valores Ri utilizados para generar los números pseudoaleatorios.
        """
        self.mean = mean
        self.standard_deviation = standard_deviation
        self.intervals_amount = intervals_amount  # Numero de iteraciones
        self.ri_values = ri_values  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni
        self.frequencies = [0] * intervals_amount
        self.intervals = [0] * intervals_amount

    def execute_method(self):
        """
        Ejecuta el método de distribución inversa normal para generar los valores Ni y calcular los intervalos y frecuencias.
        """
        self.fill_ni_values()
        self.calculate_intervals()
        self.fill_frequencies()

    def fill_ni_values(self):
        """
            Este método calcula y almacena los valores de Ni basándose en los valores de Ri utilizando la distribución inversa de la normal.
        """
        for i in range(len(self.ri_values)):
            #TODO cambiar round
            self.ni_values.append(round(norm.ppf(self.ri_values[i], loc=self.mean, scale=self.standard_deviation), 5))

    def fill_frequencies(self):
        """
        Calcula las frecuencias de los valores Ni en los intervalos definidos.
        """
        if not self.ni_values:
            raise ValueError("ni_values is empty")

        # Filtrar los valores NaN
        filtered_ni_values = [value for value in self.ni_values if not math.isnan(value)]

        if not filtered_ni_values:
            raise ValueError("All ni_values are NaN")

        min_value = min(filtered_ni_values)
        interval_size = self.intervals[1] - self.intervals[0] if len(self.intervals) > 1 else 1

        for number in filtered_ni_values:
            print(number)
            interval_index = int((number - min_value) // interval_size)
            if interval_index >= self.intervals_amount:
                interval_index = self.intervals_amount - 1  # Asegurarse de no exceder el índice máximo
            self.frequencies[interval_index] += 1

    def calculate_intervals(self):
        """
        Calcula los intervalos para la distribución de los valores Ni.
        """
        if not self.ni_values:
            raise ValueError("ni_values is empty")

        if self.intervals_amount <= 1:
            raise ValueError("intervals_amount must be greater than 1")

        _range = max(self.ni_values) - min(self.ni_values)
        interval_length = _range / (self.intervals_amount - 1)
        self.intervals[0] = min(self.ni_values)
        for i in range(1, self.intervals_amount):
            self.intervals[i] = self.intervals[i - 1] + interval_length

    def get_ri_values_array(self):
        """
        Devuelve el arreglo de valores Ri utilizados en el método.

        Retorna:
            list: Lista de valores Ri.
        """
        return self.ri_values

    def get_ni_values_array(self):
        """
        Devuelve el arreglo de valores Ni generados por el método.

        Retorna:
            list: Lista de valores Ni.
        """
        return self.ni_values

    def get_intervals(self):
        """
        Devuelve el arreglo de intervalos definidos para la distribución de los valores Ni.

        Retorna:
            list: Lista de intervalos.
        """
        return self.intervals

    def get_frequencies(self):
        """
        Devuelve el arreglo de frecuencias de los valores Ni en los intervalos definidos.

        Retorna:
            list: Lista de frecuencias.
        """
        return self.frequencies
