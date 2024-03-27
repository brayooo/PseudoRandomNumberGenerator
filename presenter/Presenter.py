class Presenter:
    """
    Esta clase se encarga de conectar la vista (interfaz de usuario) con el modelo (lógica de negocio)
    para la generación de números pseudoaleatorios mediante diferentes métodos.
    """
    def __init__(self, view, model) -> None:
        """
        Inicializa una instancia de la clase Presenter.

        Parámetros:
            view: La vista (interfaz de usuario) asociada a este presentador.
            model: El modelo (lógica de negocio) asociado a este presentador.
        """
        self.ms_method = None
        self.mcm_method = None
        self.lc_method = None
        self.nd_method = None
        self.ud_method = None
        self.selected_ri_values = []
        self.model = model
        self.view = view
        self.connect_signals()

    def presenter_middleSquare_method(self):
        """
        Ejecuta y presenta los resultados del método del cuadrado medio.
        """
        try:
            seed = self.view.ms_tab.get_seed_spin_box_value()
            min_value = self.view.ms_tab.get_min_spin_box_value()
            max_value = self.view.ms_tab.get_max_spin_box_value()
            iterations = self.view.ms_tab.get_iterations_spin_box_value()

            if len(str(seed)) < 3:
                raise ValueError("La longitud de la semilla debe tener más 3 digitos o más")

            if min_value > max_value:
                raise ValueError("El valor de min debe ser menor que max.")

            self.ms_method = self.model.execute_middle_square(seed, min_value, max_value, iterations)
            self.view.ms_tab.set_data(self.ms_method.xi_values_array, self.ms_method.ri_values_array,
                                      self.ms_method.ni_values_array)
            self.view.ms_tab.generate_table(iterations)

            self.model.write_pseudo_numbers(self.ms_method.ri_values_array, "middleSquareNumbers.json")

        except ValueError as e:
            self.view.show_warning(str(e))

    def presenter_linear_congruential_method(self):
        """
        Ejecuta y presenta los resultados del método lineal congruencial.
        """
        try:
            xo = self.view.lc_tab.get_xo_spin_box_value()
            k = self.view.lc_tab.get_k_spin_box_value()
            c = self.view.lc_tab.get_c_spin_box_value()
            g = self.view.lc_tab.get_g_spin_box_value()
            min_value = self.view.lc_tab.get_min_spin_box_value()
            max_value = self.view.lc_tab.get_max_spin_box_value()
            iterations = self.view.lc_tab.get_iterations_spin_box_value()

            # Validar que los valores sean menores que g
            if xo >= g or k >= g or c >= g:
                raise ValueError("Los valores de xo, k, c, deben ser menores que g.")

            if min_value > max_value:
                raise ValueError("El valor de min debe ser menor que max.")

            self.lc_method = self.model.execute_linear_congruential(xo, k, c, g, min_value, max_value, iterations)

            self.view.lc_tab.set_data(self.lc_method.get_xi_values_array(), self.lc_method.get_ri_values_array(),
                                      self.lc_method.get_ni_values_array())
            self.view.lc_tab.generate_table(iterations)

            self.model.write_pseudo_numbers(self.lc_method.get_ri_values_array(), "linearCongruentialNumbers.json")

        except ValueError as e:
            self.view.show_warning(str(e))

    def presenter_multiplicative_congruential_method(self):
        """
        Ejecuta y presenta los resultados del método multiplicativo congruencial.
        """
        try:
            # Recupera los valores de entrada de los cuadros de giro en la pestaña 1
            xo = self.view.mc_tab.get_xo_spin_box_value()
            t = self.view.mc_tab.get_t_spin_box_value()
            g = self.view.mc_tab.get_g_spin_box_value()
            min_value = self.view.mc_tab.get_min_spin_box_value()
            max_value = self.view.mc_tab.get_max_spin_box_value()
            iterations = self.view.mc_tab.get_iterations_spin_box_value()

            # Validar que los valores sean menores que g
            if xo >= g or t >= g:
                raise ValueError("Los valores de xo y t deben ser menores que g.")

            if min_value > max_value:
                raise ValueError("El valor de min debe ser menor que max.")
            # Ejecuta el método multiplicativo congruencial
            self.mcm_method = self.model.execute_multiplicative_congruential(xo, t, g, min_value, max_value, iterations)

            # Establece los datos generados en la pestaña 1
            self.view.mc_tab.set_data(self.mcm_method.get_xi_values_array(), self.mcm_method.get_ri_values_array(),
                                      self.mcm_method.get_ni_values_array())
            # Genera la tabla con los datos generados
            self.view.mc_tab.generate_table(iterations)

            self.model.write_pseudo_numbers(self.ms_method.get_ri_values_array(),
                                            "multiplicativeCongruentialNumbers.json")

        except ValueError as e:
            self.view.show_warning(str(e))

    def presenter_normal_distribution_method(self):
        """
        Ejecuta y presenta los resultados del método de distribución normal inversa.
        """
        intervals = self.view.nd_tab.get_intervals_spin_box_value()
        mean = self.view.nd_tab.get_mean_spin_box_value()
        standard_deviation = self.view.nd_tab.get_standard_deviation_spin_box_value()
        if self.selected_ri_values is not None:
            self.nd_method = self.model.execute_normal_inv_distribution_method(intervals, mean, standard_deviation,
                                                                               self.selected_ri_values)
            self.view.nd_tab.set_data(self.nd_method.get_ri_values_array(), self.nd_method.get_ni_values_array())
            self.view.nd_tab.update_table()

        self.model.write_pseudo_numbers(self.nd_method.get_ni_values_array(),
                                        "pseudoRandomNumbersNormalDistribution.json")

    def presenter_uniform_distribution_method(self):
        """
        Ejecuta y presenta los resultados del método de distribución uniforme.
        """
        try:
            min_value = self.view.ud_tab.get_min_spin_box_value()
            max_value = self.view.ud_tab.get_max_spin_box_value()

            if min_value > max_value:
                raise ValueError("El valor de min debe ser menor que max.")

            if self.selected_ri_values is not None:
                self.ud_method = self.model.execute_uniform_distribution_method(min_value, max_value,
                                                                                self.selected_ri_values)
                self.view.ud_tab.set_data(self.ud_method.get_ri_values_array(), self.ud_method.get_ni_values_array())
                print(self.ud_method.get_ri_values_array())
                self.view.ud_tab.update_table()

            self.model.write_pseudo_numbers(self.ud_method.get_ni_values_array(),
                                            "uniformDistributionNumbers.json")
        except ValueError as e:
            self.view.show_warning(str(e))

    def on_tab_changed(self, tab_id):
        """
        Maneja el cambio de pestaña y actualiza los valores Ri seleccionados según el método correspondiente.
        """
        try:
            if tab_id == "Middle Square Method":
                if not hasattr(self.ms_method, 'ri_values_array') or not self.ms_method.ri_values_array:
                    raise ValueError("Primero debe generar números con el método seleccionado.")
                self.selected_ri_values = self.ms_method.ri_values_array
            elif tab_id == "Linear Congruential Method":
                if not hasattr(self.lc_method, 'ri_values_array') or not self.lc_method.get_ri_values_array():
                    raise ValueError("Primero debe generar números con el método seleccionado.")
                self.selected_ri_values = self.lc_method.get_ri_values_array()
            elif tab_id == "Multiplicative Congruential Method":
                if not hasattr(self.mcm_method, 'ri_values_array') or not self.mcm_method.get_ri_values_array():
                    raise ValueError("Primero debe generar números con el método seleccionado.")
                self.selected_ri_values = self.mcm_method.get_ri_values_array()
        except ValueError as e:
            self.view.show_warning(str(e))

    def connect_signals(self):
        """
        Conecta las señales de la vista con los métodos correspondientes del presentador.
        """
        self.view.ms_tab.generate_button.clicked.connect(self.presenter_middleSquare_method)
        self.view.lc_tab.generate_button.clicked.connect(self.presenter_linear_congruential_method)
        self.view.mc_tab.generate_button.clicked.connect(self.presenter_multiplicative_congruential_method)
        self.view.nd_tab.tab_selected.connect(self.on_tab_changed)
        self.view.ud_tab.tab_selected.connect(self.on_tab_changed)
        self.view.nd_tab.generate_button.clicked.connect(self.presenter_normal_distribution_method)
        self.view.ud_tab.generate_button.clicked.connect(self.presenter_uniform_distribution_method)

    def run(self):
        """
        Muestra la vista principal de la aplicación.
        """
        self.view.show()
