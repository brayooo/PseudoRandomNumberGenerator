import numpy as np
import pyqtgraph as pg
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (QWidget, QLabel, QSpinBox, QPushButton, QFrame,
                             QTableWidget, QTableWidgetItem, QHeaderView, QVBoxLayout,
                             QHBoxLayout)
from PyQt6.QtGui import QFont


class BaseTab(QWidget):
    """
    Clase base para las pestañas de la interfaz de usuario, proporciona funcionalidades comunes.
    """
    generate_button_clicked = pyqtSignal()

    def __init__(self):
        """
        Inicializa una instancia de la clase BaseTab.
        """
        super().__init__()
        self.graph_type = None
        self.main_layout = QVBoxLayout(self)
        self.input_layout = QHBoxLayout()
        self.main_layout.addLayout(self.input_layout)

        self.generate_button = QPushButton("Generate", self)
        self.generate_button.clicked.connect(self.generate_button_clicked)
        self.main_layout.addWidget(self.generate_button)

        self.line = QFrame(self)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.main_layout.addWidget(self.line)

        self.table = QTableWidget(self)
        self.configure_table()
        self.main_layout.addWidget(self.table)

        self.graphWidget = pg.PlotWidget(self)
        self.configure_graph()
        self.main_layout.addWidget(self.graphWidget)

        self.data1 = None
        self.data2 = None
        self.data3 = None

    def configure_table(self):
        """
        Configura las propiedades de la tabla de datos.
        """
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
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
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)

    def configure_graph(self):
        """
        Configura las propiedades del gráfico.
        """
        self.graphWidget.setBackground('w')
        self.graphWidget.getAxis('bottom').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('bottom').setTextPen(pg.mkPen(color='k', width=1))
        self.graphWidget.getAxis('left').setTextPen(pg.mkPen(color='k', width=1))

    def add_input_field(self, label_text, spinbox_range=(-1e9, 1e9)):
        """
        Agrega un campo de entrada con una etiqueta y un cuadro de giro.

        Parámetros:
            label_text (str): Texto de la etiqueta.
            spinbox_range (tuple): Rango del cuadro de giro.

        Retorna:
            QSpinBox: El cuadro de giro creado.
        """
        label = QLabel(label_text, self)
        spinbox = QSpinBox(self)
        spinbox.setRange(int(spinbox_range[0]), int(spinbox_range[1]))
        self.input_layout.addWidget(label)
        self.input_layout.addWidget(spinbox)
        return spinbox

    def set_table_headers(self, headers):
        """
        Establece los encabezados de la tabla de datos.

        Parámetros:
            headers (list): Lista de encabezados de la tabla.
        """
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

    def set_graph_labels(self, x_label, y_label, title):
        """
        Establece las etiquetas y el título del gráfico.

        Parámetros:
            x_label (str): Etiqueta del eje X.
            y_label (str): Etiqueta del eje Y.
            title (str): Título del gráfico.
        """
        self.graphWidget.setLabel('bottom', x_label)
        self.graphWidget.setLabel('left', y_label)
        self.graphWidget.setTitle(title, color='k')

    def clear_graph(self):
        """
        Limpia el gráfico, eliminando todos los elementos.
        """
        self.graphWidget.clear()

    def add_bar_graph(self, x_data, y_data):
        """
        Agrega un gráfico de barras al widget de gráfico.

        Parámetros:
            x_data (list): Datos del eje X.
            y_data (list): Datos del eje Y.
        """
        bar_graph = pg.BarGraphItem(x=x_data, height=y_data, width=0.6)
        self.graphWidget.addItem(bar_graph)
        self.graphWidget.getViewBox().autoRange()

    def clear_table(self):
        """
        Limpia el contenido de la tabla de datos.
        """
        self.table.clearContents()

    def set_table_data(self, iterations):
        """
        Establece los datos de la tabla de datos.

        Parámetros:
            iterations (int): Número de iteraciones para mostrar en la tabla.
        """
        max_rows = min(iterations, 1000)  # Limitar a 1000 filas como máximo
        self.table.setRowCount(max_rows)
        self.table.setColumnCount(4)

        # Llenar la tabla con datos.
        for i in range(iterations):
            item_i = QTableWidgetItem(str(i + 1))
            item_i.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 0, item_i)

            item1 = QTableWidgetItem(str(self.data1[i]))
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 1, item1)

            item2 = QTableWidgetItem(str(self.data2[i]))
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 2, item2)

            item3 = QTableWidgetItem(str(self.data3[i]))
            item3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(i, 3, item3)
        font = QFont()
        font.setBold(True)
        self.table.horizontalHeader().setFont(font)

    def set_graph_type(self, graph_type):
        """
        Establece el tipo de gráfico a mostrar.

        Parámetros:
            graph_type (str): Tipo de gráfico ('scatter', 'bar', etc.).
        """
        self.graph_type = graph_type

    def add_graph(self, iterations):
        """
        Agrega un gráfico al widget de gráfico, según el tipo seleccionado.

        Parámetros:
            iterations (int): Número de iteraciones para mostrar en el gráfico.
        """
        self.clear_graph()
        if self.graph_type == 'scatter':
            self.create_scatter_graph(min(iterations, 500))
        self.graphWidget.getViewBox().autoRange()

    def create_scatter_graph(self, iterations):
        """
        Crea un gráfico de dispersión con los datos.

        Parámetros:
            iterations (int): Número de iteraciones para mostrar en el gráfico.
        """
        scatter = pg.ScatterPlotItem(size=10)
        scatter.setBrush(pg.mkBrush('r'))

        for i in range(1, iterations + 1):
            scatter.addPoints([i], [self.data2[i - 1]])

        # Agregue el diagrama de dispersión al widget de gráfico.
        self.graphWidget.addItem(scatter)

        # Ajustar el rango del gráfico para que se ajuste a los datos.
        self.graphWidget.getViewBox().autoRange()

    def set_data(self, data1, data2, data3):
        """
        Establece los datos para la tabla y el gráfico.

        Parámetros:
            data1 (list): Datos para la primera columna de la tabla.
            data2 (list): Datos para la segunda columna de la tabla y el gráfico.
            data3 (list): Datos para la tercera columna de la tabla.
        """
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3

    def generate_table(self, iterations):
        """
        Genera la tabla y el gráfico con los datos establecidos.

        Parámetros:
            iterations (int): Número de iteraciones para mostrar en la tabla y el gráfico.
        """

        if self.data1 is None or self.data2 is None or self.data3 is None:
            return
        self.clear_table()
        self.clear_graph()
        self.set_table_data(iterations)
        counts, bins = np.histogram(self.data2[:500], bins=121)
        self.add_bar_graph(np.arange(len(counts)), counts)
        self.set_graph_type('scatter')
        self.add_graph(iterations)
