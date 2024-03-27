class MultiplicativeCongruentialMethod:
    """
        Esta clase implementa el método multiplicativo congruencial para generar números pseudoaleatorios.
    """

    def __init__(self, xo, t, g, min_value, max_value, iterations):
        """
        Inicializa una instancia de la clase MultiplicativeCongruentialMethod.

        Parámetros:
            xo (int): Valor inicial semilla.
            t (int): Parámetro multiplicador.
            g (int): Parámetro para calcular la m.
            min_value (float): Valor mínimo para el rango de los números generados.
            max_value (float): Valor máximo para el rango de los números generados.
            iterations (int): Número de iteraciones o números a generar.
        """
        self.xi_values = []  # Lista para almacenar los valores de Xi
        self.ri_values = []  # Lista para almacenar los valores de Ri
        self.ni_values = []  # Lista para almacenar los valores de Ni
        self.xo = xo  # Valor inicial semilla
        self.t = t  # Parametro multiplicador
        self.g = g  # Parametro del modulo
        self.min = min_value  # Valor minimo para el rango
        self.max = max_value # Valor maximo para el rango
        self.iterations = iterations  # Numero de iteraciones

    def execute(self):
        """
            Este método ejecuta el método multiplicativo congruencial.
        """
        self.fill_first_xi_value()
        self.fill_xi_values()
        self.fill_ri_and_ni_values()

    def fill_first_xi_value(self):
        """
            Este método calcula y almacena el primer valor Xi.
        """
        a = (8 * self.t) + 3
        amount = 2 ** self.g
        value = (a * self.xo) % amount
        self.xi_values.append(round(value, 5))

    def fill_xi_values(self):
        """
            Este método calcula y almacena todos los valores Xi posteriores.
        """
        a = (8 * self.t) + 3
        amount = 2 ** self.g
        for i in range(self.iterations - 1):
            value = (a * self.xi_values[i]) % amount
            self.xi_values.append(round(value, 5))

    def fill_ri_and_ni_values(self):
        """
            Este método calcula y almacena todos los valores de Ri y Ni.
        """
        num_amount = 2 ** self.g
        for i in range(self.iterations):
            ri_value = float(self.xi_values[i]) / (num_amount - 1)
            self.ri_values.append(round(ri_value, 5))

            ni_value = self.min + (self.max - self.min) * ri_value
            self.ni_values.append(round(ni_value, 5))

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
