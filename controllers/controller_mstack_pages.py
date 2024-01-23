from views.View_MStack_pages.view_mstack_pages_ui import Ui_MainWindow
from PyQt5 import QtWidgets
from controllers.controller_calibration import MyApplication


class Controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear instancia de la interfaz generada por PyQt5
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.view_calibration = MyApplication()
        self.ui.stackedWidget.addWidget(self.view_calibration)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show()
    sys.exit(app.exec_())