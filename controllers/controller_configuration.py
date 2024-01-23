from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog,QMessageBox
from views.View_Configuration.view_configuration_prueba_ui import Ui_Dialog

class MainDialog(QDialog):
    data_signal = QtCore.pyqtSignal(int, int, int, str, int,int)
    def __init__(self):
        super(MainDialog, self).__init__()

        # Crear una instancia de la clase Ui_Dialog
        self.ui = Ui_Dialog()
        # Configurar la interfaz de usuario
        self.ui.setupUi(self)

        # Conectar el evento activated del QComboBox a un método específico
        self.ui.comboBox_configuration.activated.connect(self.on_combobox_activated)
        # Conectar la señal del botón a un método
        self.ui.btn_aceptar.clicked.connect(self.onclick_configuration)
        self.ui.btn_cancelar.clicked.connect(self.onclick_salir)

    def onclick_salir (self):
        # Cerrar la ventana
        self.accept()

    def on_combobox_activated(self, index):
        selected_option = self.ui.comboBox_configuration.itemText(index)

        # Realiza las acciones deseadas según la opción seleccionada
        if selected_option == "Tiempo":
           self.ui.stackedWidget.setCurrentIndex(0)
        elif selected_option == "Escaneos":
           self.ui.stackedWidget.setCurrentIndex(1)
        else:
            # Acción para otras opciones
            print("Opción seleccionada:", selected_option)

    def onclick_configuration(self):
       #Inicio
       rangoa = self.ui.spinBox_rangoa.value()
       #Final
       rangob = self.ui.spinBox_rangob.value()
       intervalos = self.ui.spinBox_rintervalos.value()

       if rangoa > rangob or intervalos <= 0:
            msj = ""
            if rangoa ==0 and rangob == 0:
               msj = "El rango inicial y final no pueden ser 0\n"
            if rangoa > rangob:
               msj = "El rango inicial no debe ser mayor que el rango final\n"
            if intervalos <= 0:
               msj += "El intervalo no puede ser 0"    
            self.alerta_warning(msj)
       else:
           fragmentos = (rangob - rangoa) // intervalos + 1
           print("Número de fragmentos:", fragmentos)
           self.value_rangos(fragmentos,rangoa,rangob,intervalos)
           # Cerrar la ventana
           
    def value_rangos(self,fragmentos,rangoa,rangob,intervalos):
        escaneos = self.ui.spinBox_numescaneos.value() # escaneos
        temp = self.ui.spinBox_minutos.value() # minutos
        configuration = self.ui.comboBox_configuration.currentText()
        if fragmentos > 12:
            # Crear el mensaje con el límite de pruebas y el número de fragmentos
            limit = 12
            mess = "El límite de pruebas es: {}\nNúmero de pruebas: {}".format(limit, fragmentos)
            self.alerta_warning(mess)
        elif fragmentos > 0  and fragmentos <= 12:
            # Se indica si es por tiempo o si es por escaneos
            if configuration == "Tiempo" and temp != 0:
                self.data_signal.emit(rangoa, rangob, intervalos,configuration, temp,fragmentos)
                self.accept()
            elif configuration == "Escaneos" and escaneos != 0:
                self.data_signal.emit(rangoa, rangob, intervalos,configuration, escaneos,fragmentos)
                self.accept()
        
        print(str(configuration) +" "+str(escaneos))
        if configuration == "Escaneos" and escaneos == 0:
            msj = "El número de escaneos no puede ser 0"
            self.alerta_warning(msj)

        elif configuration == "Tiempo" and temp == 0:
            msj = "El tiempo no puede ser 0"
            self.alerta_warning(msj)

    def alerta_warning(self,mess):
        # Crear una instancia de QMessageBox
        alert = QMessageBox()

        # Establecer el ícono y el título de la ventana de diálogo
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle("Exceso de pruebas")

        # Establecer el texto del mensaje
        alert.setText(mess)

        # Mostrar la ventana de diálogo y esperar a que el usuario la cierre
        alert.exec_()
