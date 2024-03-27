from PyQt6.QtWidgets import QMainWindow, QTabWidget, QMessageBox
from view.LCTab import LinerCongruentialTab
from view.MCTab import MultiplicativeCongruentialTab
from view.MStab import MiddleSquareTab
from view.NDTab import NormalDistributionTab
from view.UDTab import UniformDistributionTab


class MainFrame(QMainWindow):
    """
    La clase MainFrame es la ventana principal de la aplicación.
    Hereda de QMainWindow, una clase base para las ventanas principales en PyQt.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase MainFrame.
        """
        super().__init__()
        self.mc_tab = MultiplicativeCongruentialTab()
        self.ms_tab = MiddleSquareTab()
        self.lc_tab = LinerCongruentialTab()
        self.nd_tab = NormalDistributionTab()
        self.ud_tab = UniformDistributionTab()
        self.tab_widget = None
        self.init_ui()
        self.init_tabs()
        self.center()

    def init_ui(self):
        """
        Inicializa la interfaz de usuario de la ventana principal.
        """
        self.setWindowTitle("Main Frame")
        self.tab_widget = QTabWidget(self)
        self.setCentralWidget(self.tab_widget)  # Establece el widget de pestañas como el central
        self.resize(800, 600)  # Establece un tamaño inicial para la ventana principal

    def init_tabs(self):
        """
        Inicializa las pestañas y las agrega al widget de pestañas.
        """
        self.tab_widget.addTab(self.ms_tab, "Middle Square Method")
        self.tab_widget.addTab(self.lc_tab, "Linear congruential Method")
        self.tab_widget.addTab(self.mc_tab, "Multiplicative Congruential Method")
        self.tab_widget.addTab(self.nd_tab, "Normal inv distribution Method")
        self.tab_widget.addTab(self.ud_tab, "Uniform distribution Method")

        # Configura las opciones del QComboBox en la pestaña de distribución normal
        tab_names = ["Middle Square Method", "Linear Congruential Method", "Multiplicative Congruential Method"]
        self.nd_tab.set_tab_options(tab_names)
        self.ud_tab.set_tab_options(tab_names)

    def show_warning(self, message):
        """
        Muestra un mensaje de advertencia al usuario.

        Parámetros:
            message (str): El mensaje de advertencia a mostrar.
        """
        QMessageBox.warning(self, "Advertencia", message)

    def center(self):
        """
        Centra la ventana en la pantalla.
        """
        center_point = self.screen().availableGeometry().center()
        frame_geom = self.frameGeometry()
        frame_geom.moveCenter(center_point)
        self.move(frame_geom.topLeft())
