import numpy as np

from view.BaseTab import BaseTab


class MiddleSquareTab(BaseTab):
    """
        Clase para la pestaña del método cuadrado medios en la interfaz de usuario.
        Hereda de BaseTab y agrega campos de entrada específicos para este método.
        """
    def __init__(self):
        """
        Inicializa una instancia de la clase MiddleSquareTab.
        """
        super().__init__()
        self.seed_spinbox = self.add_input_field("Seed:")
        self.min_spinbox = self.add_input_field("Minimum Xi Value:")
        self.max_spinbox = self.add_input_field("Maximum Xi Value:")
        self.iterations_amount_spinbox = self.add_input_field("Number of Iterations:")
        self.set_table_headers(['Iteration', 'Xi', 'Ri', 'Ni'])
        self.set_graph_labels('Iterations', 'Frequencies', 'Scatter Plot of Ri Values')

    def get_seed_spin_box_value(self):
        """
        Devuelve el valor de la semilla inicial (seed) ingresado por el usuario.

        Retorna:
            int: Valor de seed.
        """
        return self.seed_spinbox.value()

    def get_min_spin_box_value(self):
        """
        Devuelve el valor mínimo de Xi ingresado por el usuario.

        Retorna:
            int: Valor mínimo de Xi.
        """
        return self.min_spinbox.value()

    def get_max_spin_box_value(self):
        """
        Devuelve el valor máximo de Xi ingresado por el usuario.

        Retorna:
            int: Valor máximo de Xi.
        """
        return self.max_spinbox.value()

    def get_iterations_spin_box_value(self):
        """
        Devuelve el número de iteraciones ingresado por el usuario.

        Retorna:
            int: Número de iteraciones.
        """
        return self.iterations_amount_spinbox.value()

    def set_data(self, data1, data2, data3):
        """
        Establece los datos para la tabla y el gráfico.

        Parámetros:
            data1 (list): Datos para la primera columna de la tabla.
            data2 (list): Datos para la segunda columna de la tabla y el gráfico.
            data3 (list): Datos para la tercera columna de la tabla.
        """
        super().set_data(data1, data2, data3)

    def generate_table(self, iterations):
        """
        Genera la tabla y el gráfico con los datos establecidos.

        Parámetros:
            iterations (int): Número de iteraciones para mostrar en la tabla y el gráfico.
        """
        super().generate_table(iterations)
