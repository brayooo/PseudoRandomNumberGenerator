import json
import os

from model.LinearCongruentialMethod import LinearCongruentialMethod
from model.MiddleSquareMethod import MiddleSquareMethod
from model.MultiplicativeCongruentialMethod import MultiplicativeCongruentialMethod
from model.NormalInvDistributionMethod import NormalInvDistributionMethod
from model.UniformDistributionMethod import UniformDistributionMethod


class Methods:
    """
    Clase que encapsula la ejecución de diferentes métodos de generación de números pseudoaleatorios.
    """

    def execute_multiplicative_congruential(self, xo, t, g, min_value, max_value, iterations):
        """
        Ejecuta el método multiplicativo congruencial.

        Parámetros:
            xo (int): Valor inicial de la semilla.
            t (int): Variable utilizada para calcular el multiplicador.
            g (int): Variable utilizada para calcular la m.
            min_value (int): Valor mínimo para el rango de los números generados.
            max_value (int): Valor máximo para el rango de los números generados.
            iterations (int): Número de iteraciones o números a generar.

        Retorna:
            MultiplicativeCongruentialMethod: Instancia del método con los números generados.
        """
        mc = MultiplicativeCongruentialMethod(xo, t, g, min_value, max_value, iterations)
        mc.execute()
        return mc

    def execute_middle_square(self, seed, min_value, max_value, iterations):
        """
        Ejecuta el método del cuadrado medio.

        Parámetros:
            seed (int): Semilla inicial para la generación de números.
            min_value (int): Valor mínimo para el rango de los números generados.
            max_value (int): Valor máximo para el rango de los números generados.
            iterations (int): Número de iteraciones o números a generar.

        Retorna:
            MiddleSquareMethod: Instancia del método con los números generados.
        """
        ms = MiddleSquareMethod(seed, min_value, max_value, iterations)
        ms.generate_randoms()
        return ms

    def execute_linear_congruential(self, xo, k, c, g, min_value, max_value, iterations):
        """
        Ejecuta el método lineal congruencial.

        Parámetros:
            xo (int): Valor inicial de la semilla.
            k (int): Variable utilizada para calcular el multiplicador.
            c (int): Incremento.
            g (int): Variable utilizada para calcular la m.
            min_value (int): Valor mínimo para el rango de los números generados.
            max_value (int): Valor máximo para el rango de los números generados.
            iterations (int): Número de iteraciones o números a generar.

        Retorna:
            LinearCongruentialMethod: Instancia del método con los números generados.
        """
        lc = LinearCongruentialMethod(xo, k, c, g, min_value, max_value, iterations)
        lc.generate_numbers_tested()
        return lc

    def execute_normal_inv_distribution_method(self, intervals_amount, mean, standard_deviation, ri_values):
        """
        Ejecuta el método de distribución normal inversa.

        Parámetros:
            intervals_amount (int): Cantidad de intervalos para la distribución.
            mean (float): Media de la distribución.
            standard_deviation (float): Desviación estándar de la distribución.
            ri_values (list): Valores Ri a utilizar para la generación de la distribución.

        Retorna:
            NormalInvDistributionMethod: Instancia del método con los números generados.
        """
        nd = NormalInvDistributionMethod(intervals_amount, mean, standard_deviation, ri_values)
        nd.execute_method()
        return nd

    def execute_uniform_distribution_method(self, min_value, max_value, ri_values):
        """
        Ejecuta el método de distribución uniforme.

        Parámetros:
            min_value (int): Valor mínimo para el rango de los números generados.
            max_value (int): Valor máximo para el rango de los números generados.
            ri_values (list): Valores Ri a utilizar para la generación de la distribución.

        Retorna:
            UniformDistributionMethod: Instancia del método con los números generados.
        """
        ud = UniformDistributionMethod(min_value, max_value, ri_values)
        ud.fill_ni_values()
        return ud

    def write_pseudo_numbers(self, data, file_name):
        """
        Este método escribe los números pseudoaleatorios en un archivo.

        Parámetros:
            data (list): Lista de numeros que se quieren escribir en el archivo.
            file_name (str): Nombre que el archivo tendrá.
        """
        folder_name = "NumbersGenerated"

        # Crear la carpeta si no existe
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Ruta del archivo JSON dentro de la carpeta
        file_path = os.path.join(folder_name, file_name)

        json_data = {"numbers": data}
        with open(file_path, 'w') as file:
            json.dump(json_data, file)
