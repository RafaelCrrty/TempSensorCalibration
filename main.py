import sys
from PyQt5.QtWidgets import QApplication
from controllers.controller_mstack_pages import Controller

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Controller()
    window.show()
    sys.exit(app.exec_())