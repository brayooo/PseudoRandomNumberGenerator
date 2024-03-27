class MathUtils:
    """
    Clase de utilidades matemáticas que proporciona métodos estáticos para operaciones matemáticas comunes.
    """
    @staticmethod
    def truncate(number):
        """
        Trunca un número a 5 decimales.

        Parámetros:
            number (float): El número a truncar.

        Retorna:
            float: El número truncado a 5 decimales.
        """
        return float(f'{number:.5f}')
