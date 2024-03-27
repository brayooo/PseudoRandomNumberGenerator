import sys

from PyQt6.QtWidgets import QApplication

from model.Methods import Methods
from presenter.Presenter import Presenter
from view.MainFrame import MainFrame


def main():
    """
    Función principal que inicia la aplicación.
    """
    # Crea la aplicación de PyQt.
    app = QApplication(sys.argv)

    # Crea la vista principal, el modelo y el presentador.
    view = MainFrame()
    model = Methods()
    presenter = Presenter(view, model)

    # Inicia la ejecución de la vista principal.
    presenter.run()

    # Finaliza la aplicación cuando se cierra la ventana principal.
    sys.exit(app.exec())


if __name__ == '__main__':
    # Si este script es ejecutado como principal, llama a la función main.
    main()
