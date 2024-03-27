from model.Utils.MathUtils import MathUtils


class UniformDistributionMethod:
    """
        Esta clase implementa el método de distribución uniforme para generar números pseudoaleatorios.
    """

    def __init__(self, min_value, max_value, ri_values):
        """
        Inicializa una instancia de la clase UniformDistributionMethod.

        Parámetros:
            min_value (float): Valor mínimo para el rango de los números generados.
            max_value (float): Valor máximo para el rango de los números generados.
            ri_values (list): Lista de valores Ri utilizados para generar los números pseudoaleatorios.
        """
        self.min_value = min_value
        self.max_value = max_value
        self.ri_values = ri_values  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni

    def fill_ni_values(self):
        """
        Calcula y almacena los valores de Ni en función de los valores de Ri utilizando la distribución uniforme.
        """
        for i in range(len(self.ri_values)):
            value = self.min_value + (self.max_value - self.min_value) * self.ri_values[i]
            self.ni_values.append(MathUtils.truncate(value))

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
