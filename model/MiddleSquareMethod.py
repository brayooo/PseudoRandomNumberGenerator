
class MiddleSquareMethod:
    """
    Implementa el método del cuadrado medio para generar números pseudoaleatorios.
    """
# TODO round ni values to 5 decimals
    def __init__(self, seed, min_val, max_val, num_amount):
        """
        Inicializa una instancia de la clase MiddleSquareMethod.

        Parámetros:
            seed (int): Semilla inicial para la generación de números.
            min_val (float): Valor mínimo para el rango de los números generados.
            max_val (float): Valor máximo para el rango de los números generados.
            num_amount (int): Número de valores a generar.
        """
        self.seed = seed
        self.ni_values = []
        self.ri_values = []
        self.xi_values = []
        self.centers = []
        self.min_val = min_val
        self.max_val = max_val
        self.num_amount = num_amount

    def generate_randoms(self):
        """
        Genera números pseudoaleatorios utilizando el método del cuadrado medio.
        """
        seed = self.seed
        len_seed = len(str(self.seed))
        for _ in range(self.num_amount):
            self.xi_values.append(seed)
            xi2 = seed * seed
            center = self.get_center(str(xi2))
            self.centers.append(center)
            ri = center / (10 ** len_seed)
            self.ri_values.append(ri)
            ni = self.min_val + ((self.max_val - self.min_val) * ri)
            self.ni_values.append(ni)
            seed = center

    def get_center(self, num):
        """
        Obtiene el centro de un número, utilizado en el método del cuadrado medio.

        Parámetros:
            num (str): Número del cual se extraerá el centro.

        Retorna:
            int: Centro del número.
        """
        len_seed = len(str(self.seed))
        padded = num.zfill(len_seed * 2)
        start_index = int(len_seed / 2)
        end_index = start_index + len_seed
        return int(padded[start_index:end_index])

    @property
    def xi_values_array(self):
        """
        Devuelve el arreglo de valores Xi generados.

        Retorna:
            list: Lista de valores Xi.
        """
        return self.xi_values

    @property
    def ri_values_array(self):
        """
        Devuelve el arreglo de valores Ri generados.

        Retorna:
            list: Lista de valores Ri.
        """
        return self.ri_values

    @property
    def ni_values_array(self):
        """
        Devuelve el arreglo de valores Ni generados.

        Retorna:
            list: Lista de valores Ni.
        """
        return self.ni_values
