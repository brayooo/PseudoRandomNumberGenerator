import numpy as np
from scipy.stats import norm
import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QSpinBox, QPushButton, QFrame,
                             QTableWidget, QTableWidgetItem, QHeaderView, QComboBox, QVBoxLayout, QHBoxLayout)


class NormalDistributionTab(QWidget):
    """
        Esta es la clase de contenido de la pestaña Método de distribución normal inversa.
        Hereda de QWidget, una clase base para todos los objetos de la interfaz de usuario en PyQt.
    """
    generate_button_clicked = pyqtSignal()
    tab_selected = pyqtSignal(str)

    def __init__(self, tabs=None):
        """
        Inicializa una instancia de la clase NormalDistributionTab.

        Parámetros:
            tabs (list): Lista de nombres de pestañas disponibles para la selección de la fuente de números Ri.
        """

        super().__init__()
        self.tabs = tabs or []
        self.tab_selector = None
        self.standard_deviation_spinbox = None
        self.mean_spinbox = None
        self.intervals_amount_spinbox = None
        self.graph_data = None
        self.ri_table_data = None
        self.ni_table_data = None
        self.main_layout = QVBoxLayout(self)
        self.input_layout = QHBoxLayout()
        self.init_ui()

    def init_ui(self):
        """
            Este método inicializa la interfaz de usuario de la pestaña.
        """
        self.init_input_layout()
        self.init_table()
        self.init_graph()

    def init_input_layout(self):
        """
            Este método inicializa el layout de entrada con etiquetas, cuadros de giro y botones.
        """
        self.main_layout.addLayout(self.input_layout)

        # Inicializa y agrega la etiqueta y el cuadro de giro para la cantidad de intervalos.
        self.intervals_amount_label = QLabel("Amount of intervals")
        self.intervals_amount_spinbox = QSpinBox()
        self.intervals_amount_spinbox.setRange(0, int(1e+9))
        self.input_layout.addWidget(self.intervals_amount_label)
        self.input_layout.addWidget(self.intervals_amount_spinbox)

        # Inicializa y agrega la etiqueta y el cuadro de giro para la media.
        self.mean_label = QLabel("Mean")
        self.mean_spinbox = QSpinBox()
        self.mean_spinbox.setRange(0, int(1e+9))
        self.input_layout.addWidget(self.mean_label)
        self.input_layout.addWidget(self.mean_spinbox)

        # Inicializa y agrega la etiqueta y el cuadro de giro para la desviación estándar.
        self.standard_deviation_label = QLabel("Standard deviation")
        self.standard_deviation_spinbox = QSpinBox()
        self.standard_deviation_spinbox.setRange(0, int(1e+9))
        self.input_layout.addWidget(self.standard_deviation_label)
        self.input_layout.addWidget(self.standard_deviation_spinbox)

        # Inicializa y agrega el QComboBox para seleccionar la pestaña de origen de los números Ri.
        self.tab_selector = QComboBox(self)
        self.tab_selector.addItem("Seleccione una pestaña", "")
        self.tab_selector.currentIndexChanged.connect(self.on_tab_selected)
        self.input_layout.addWidget(self.tab_selector)

        # Inicializa y agrega el botón de generar.
        self.generate_button = QPushButton("Generate")
        self.input_layout.addWidget(self.generate_button)
        self.generate_button.clicked.connect(self.generate_button_clicked)

        # Inicializa y agrega una línea horizontal como separador.
        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(self.line)

    def init_table(self):
        """
            Este método inicializa el QTableWidget para mostrar los datos.
        """
        self.table = QTableWidget()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        # Establece el estilo de la tabla.
        self.table.setStyleSheet("""
                                             QTableWidget {
                                                 gridline-color: black;
                                                 color: black;
                                             }
                                             QHeaderView::section {
                                                 background-color: #29005f;
                                                 color: white;
                                                 font-weight: bold;
                                                 border: 1px solid black;
                                             }
                                             QScrollBar:vertical {
                                                 border: none;
                                                 background: white;
                                                 width: 14px;
                                                 margin: 15px 0 15px 0;
                                             }
                                             QScrollBar::handle:vertical {        
                                                 background: gray;
                                                 min-height: 30px;
                                             }
                                             QScrollBar::add-line:vertical {
                                                 border: none;
                                                 background: none;
                                             }
                                             QScrollBar::sub-line:vertical {
                                                 border: none;
                                                 background: none;
                                             }
                                         """)
        self.main_layout.addWidget(self.table)

    def init_graph(self):
        """
            Este método inicializa el PlotWidget para mostrar el gráfico.
        """
        self.graphWidget = pg.PlotWidget()
        self.graphWidget.setLabel('left', 'Frequencies')
        self.graphWidget.setLabel('bottom', 'Intervals')
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.setTitle('Gauss Bell', color='k')
        self.main_layout.addWidget(self.graphWidget)

    def on_tab_selected(self, index):
        """
            Este método emite la pestaña seleccionada.
        """
        tab_id = self.tab_selector.itemData(index)
        if tab_id:
            self.tab_selected.emit(tab_id)

    def set_data(self, ri_table_data, ni_table_data):
        """
            Este método establece los datos para la tabla y el gráfico.
        """
        self.ri_table_data = ri_table_data
        self.ni_table_data = ni_table_data
        self.graph_data = ni_table_data

    def update_table(self):
        """
            Este método actualiza la tabla con los datos proporcionados.
        """
        if not self.ri_table_data or not self.ni_table_data:
            return

        iterations = len(self.ri_table_data)
        self.table.setRowCount(iterations)
        self.table.setColumnCount(3)

        # Establece las etiquetas del encabezado de la tabla.
        header_labels = ['Iteration', 'Ri', 'Ni']
        self.table.setHorizontalHeaderLabels(header_labels)

        # Llenar la tabla con datos.
        for i in range(iterations):
            item_i = QTableWidgetItem(str(i + 1))
            item_i.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 0, item_i)

            item_ri = QTableWidgetItem(str(self.ri_table_data[i]))
            item_ri.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 1, item_ri)

            # Añadir los valores Ni a la tabla.
            item_ni = QTableWidgetItem(str(self.ni_table_data[i]))
            item_ni.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 2, item_ni)

        # Establece los encabezados de las columnas en negrita.
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)
        self.create_graph()

    def create_graph(self):
        """
        Este método crea el gráfico con los datos proporcionados.
        """
        if not self.graph_data:
            return

        # Calcular el histograma a partir de los datos de Ni
        counts, bins = np.histogram(self.graph_data, bins=self.get_intervals_spin_box_value(), density=True)

        # Crear puntos para la línea de la campana de Gauss
        curve_bins = np.linspace(min(bins), max(bins), 300)
        curve = norm.pdf(curve_bins, self.get_mean_spin_box_value(), self.get_standard_deviation_spin_box_value())

        # Crear el objeto BarGraphItem para el histograma
        bg1 = pg.BarGraphItem(x=bins[:-1], height=counts, width=0.9 * (bins[1] - bins[0]), brush='b')

        # Limpiar el widget de gráfico antes de añadir nuevos elementos
        self.graphWidget.clear()

        # Añadir el histograma al gráfico
        self.graphWidget.addItem(bg1)

        # Añadir la campana de Gauss al gráfico
        gaussian_curve = pg.PlotDataItem(curve_bins, curve, pen=pg.mkPen('r', width=2))
        self.graphWidget.addItem(gaussian_curve)

        # Ajustar el rango del gráfico para que se muestren todos los datos
        self.graphWidget.getViewBox().autoRange()

    def get_intervals_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro del parámetro intervals.

            Retorna:
                int: Número de intervalos.
        """
        if self.intervals_amount_spinbox is not None:
            return self.intervals_amount_spinbox.value()

    def get_mean_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro del parámetro mean.

            Retorna:
                int: Valor de la media.
        """
        if self.mean_spinbox is not None:
            return self.mean_spinbox.value()

    def get_standard_deviation_spin_box_value(self):
        """
            Este método devuelve el valor del cuadro de giro del parámetro standard deviation.

            Retorna:
                int: Valor de la desviacion estandar.
        """
        if self.standard_deviation_spinbox is not None:
            return self.standard_deviation_spinbox.value()

    def set_tab_options(self, tab_names):
        """
        Configura las opciones del QComboBox con los nombres de las pestañas.
        """
        self.tab_selector.clear()
        self.tab_selector.addItem("Seleccione una pestaña", "")
        for tab_name in tab_names:
            self.tab_selector.addItem(tab_name, tab_name)
