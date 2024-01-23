import sys
import threading
import csv,os,re
import serial
import time
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFrame, QLabel,QHBoxLayout,QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.View_Calibration.view_calibracion_ui import Ui_Form
from controllers.controller_curva_ajuste import MainCalibration
from controllers.controller_configuration import MainDialog
from controllers.controller_config_arduino import ArduinoSettingDialog
from models.Grafica import Canvas_grafica
from models.Mediador import Mediator,Component
import pygame
import random

class MyApplication(QMainWindow):
    def __init__(self):
        super(MyApplication, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
       # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.sensores = ["sensor1", "sensor2", "sensor3", "sensor4"]

        self.frac = 0 # total de fracmnetos
        self.parra = 0
        self.rows = -1
        self.count_button = 0 # es un contador para saber cuantas pulsadas tiene el boton

        self.push = 0
        self.boolcancel = False

        self.ui.pushButton.clicked.connect(self.graficar)
        self.ui.btn_cancelar.clicked.connect(self.cancelar_getdatos)
        self.ui.btn_clear_barra.clicked.connect(self.smj_clear_items)
       
        self.ui.btn_configuracion_prueba.clicked.connect(self.configuration)
        self.ui.btn_puerto_arduino.clicked.connect(self.settigns_arduino)

        self.ui.btn_curva_ajuste.clicked.connect(self.curva_ajuste_emergent)
        self.ui.btn_curva_ajuste.setDisabled(True)
        tooltip_text = "Rango inicial: 0\nRango final: 0\nIntervalos: 0\nConfiguración: None \n0 minutos"
        self.ui.btn_configuracion_prueba.setToolTip(tooltip_text)
        self.mediator = Mediator()
        self.component = Component(self.mediator,"Controller_calibrartion")


        self.viewconfig_ardino = ArduinoSettingDialog()

        self.emergent_configuration_pruebabar = MainDialog()
        self.emergent_curva_ajuste = MainCalibration()
        self.emergent_curva_ajuste.data_signal.connect(self.actualizar_stackpane)
        
        self.ui.stackedWidget.addWidget(self.emergent_curva_ajuste)
        self.ui.stackedWidget.lower()
        
        self.minutos = 0
        self.timer = QTimer()
        self.booltemp = False
        self.timer.timeout.connect(self.actualizar_temporizador)
        self.timers = QTimer()
        self.boolscan = False
        self.timers.timeout.connect(self.actualizar_escaneos)
        self.minutos_totales = 0
        self.minutos_restantes = 0
        self.segundos_restantes = 0
 
        self.boolean_view = False
        self.boodatesensor = False

        # Inicializar Pygame
        pygame.init()
        # Variables para almacenar las coordenadas del ratón al presionar
        #self.drag_start_position = None

        self.puertooo = None

    def smj_clear_items(self):
        # Crear el cuadro de diálogo de advertencia
        if self.ui.barra_tiempo.count()>0:
            """"""
            bol_data = False
            if self.boodatesensor:
                bol_data = True

            print(str(bol_data) + "NOOOOOOOOOO")
            if bol_data:    
               alert = QMessageBox()
               alert.setIcon(QMessageBox.Information)
               alert.setWindowTitle("Information")
               alert.setText("Por favor, espera que termine la lectura.")
               alert.exec_()
               return
            
            self.clear_barra_Frac()
            
        else:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Information")
            alert.setText("Por favor, indica las pruebas.")
            alert.exec_()

    def clear_barra_Frac(self):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Warning)
        alert.setWindowTitle("Alerta")
        alert.setText("¿Estás seguro de que quieres borrar los elementos?")
        alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            
        # Obtener la respuesta del usuario
        respuesta = alert.exec_()
            
            # Procesar la respuesta
        if respuesta == QMessageBox.Yes:
            self.count_button = 0 
            # Limpiar el QHBoxLayout existente
            self.clear_layout(self.ui.barra_tiempo)
            self.clear_layout(self.ui.barra_bao_termico1) 
            self.clear_layout(self.ui.barra_bao_termico2) 
            self.clear_layout(self.ui.barra_bao_termico3) 
            self.clear_layout(self.ui.barra_bao_termico4)
            self.clear_layout(self.ui.grafica1)
            self.clear_layout(self.ui.grafica2)
            self.clear_layout(self.ui.grafica3)
            self.clear_layout(self.ui.grafica4)
            self.add_tableview()
        else:
            """"""

    def cancelar_getdatos(self):
        self.ui.pushButton.setVisible(True)
        self.ui.btn_cancelar.setVisible(False)
        self.count_button -= 1 
        self.boolcancel = True
    
    #Checar este metodo
    def curva_ajuste_emergent(self):
        if self.push >= self.ui.barra_tiempo.count()-1:
            datos = self.recuperation_elemens_table()
            if datos:
                self.component.notify(datos)
                self.emergent_curva_ajuste.user_action()
            if self.boolean_view == False:
                self.ui.stackedWidget.setCurrentWidget(self.emergent_curva_ajuste)
                self.boolean_view = True
            
            self.actualizar_stackpane(False)
            self.ui.btn_curva_ajuste.setDisabled(False)
        
        else:
            self.ui.btn_curva_ajuste.setDisabled(True)
            print("na")
            
    def recuperation_elemens_table(self):
        table_view = self.ui.tableView_promedios  # Obtén una referencia al QTableView
        model = table_view.model()  # Obtén el modelo asociado al QTableView

        if model is None or model.rowCount() == 0 or model.columnCount() == 0:
            return []

        data_list = []
        num_columns = model.columnCount()
        for row in range(model.rowCount()):
            sublist = []
            for column in range(num_columns):
                index = model.index(row, column)
                data = index.data(QtCore.Qt.DisplayRole)
                sublist.append(str(data) if data is not None else "")
            data_list.append(sublist)
        print(data_list)
        return data_list

    def actualizar_stackpane(self, valor_booleano):
        if valor_booleano:
            self.ui.stackedWidget.hide()
        else:
            self.ui.stackedWidget.raise_()
            self.ui.stackedWidget.show()

    """
     def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.drag_start_position is not None:
            delta = event.globalPos() - self.drag_start_position
            self.move(self.pos() + delta)
            self.drag_start_position = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = None
    
    """
    def configuration(self):
        self.emergent_configuration_pruebabar.setWindowTitle("Ventana emergente")
        self.emergent_configuration_pruebabar.setGeometry(100,100,237, 384)
        self.emergent_configuration_pruebabar.data_signal.connect(self.receive_data)
        self.emergent_configuration_pruebabar.exec_()

    def settigns_arduino(self):
        self.viewconfig_ardino.setWindowTitle("Ventana emergente")
        self.viewconfig_ardino.setGeometry(110,100,263, 476)
        self.viewconfig_ardino.data_signal.connect(self.puerto_arduino)
        self.viewconfig_ardino.exec_()

    def puerto_arduino(self,obj_puerto):
        """"""
        print("El puerto a conectarse es, ", obj_puerto)
        self.puertooo = obj_puerto

    def clear_layout(self, layout):
        print(layout.count())
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def receive_data(self, rangoa, rangob, intervalos, configuration, value,fragmentos):
        # Aquí recibes los datos y puedes hacer lo que necesites con ellos en la ventana principal
        # Por ejemplo, imprimirlos en la consola
        print("Datos recibidos:", rangoa, rangob, intervalos, configuration, value)
        #con esto ya puedes orientar la configuracion que ya se tiene 
       # Establecer el tooltip del botón con los valores recibidos
        tooltip_text = f"Rango inicial: {rangoa}\nRango final: {rangob}\nIntervalos: {intervalos}\nConfiguración: {configuration}\n{value} minutos"
        self.ui.btn_configuracion_prueba.setToolTip(tooltip_text)
        try:
            bools = False
            # Verificar si los valores de rangoa, rangob e intervalos son válidos
            if rangoa > rangob or intervalos <= 0:
                raise ValueError("Valores de rango o intervalo no válidos")
                bools = True
            if bools != True:
                # Limpiar el QHBoxLayout existente
                self.clear_layout(self.ui.barra_tiempo)
                self.clear_layout(self.ui.barra_bao_termico1) 
                self.clear_layout(self.ui.barra_bao_termico2) 
                self.clear_layout(self.ui.barra_bao_termico3) 
                self.clear_layout(self.ui.barra_bao_termico4) 

            # Iterar desde rangoa hasta rangob con el intervalo especificado
            #Inicializar de nuevo las variables
            self.count_button = 0
            self.rows = -1 # para las filas del tableview
            self.parra = 0
            self.frac = fragmentos
            self.config = configuration
            self.escaneos = 0 # numero de escaneo
            self.escaneos_count = 0
            self.boolscan = False
            self.booltemp = False
            self.boolcancel = False
            self.ui.btn_curva_ajuste.setDisabled(True)
            self.boodatesensor = False
            
            ruta_relativa = "data_sensors/"
            archivos_csv = [ruta_relativa+'datos'+self.sensores[0]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[1]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[2]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[3]+'_temperatura.csv']
            self.borrar_archivos_csv(archivos_csv)

            if configuration == "Tiempo": 
                self.minutos = value
                self.timer.stop()
                self.ui.lbl_nomconfiguration.setText("Temporizador")
                self.ui.lbl_temporizador.setText(str(value)+":00")
                self.barras_fracmento(rangoa,rangob,intervalos)

                self.add_tableview()
            
            elif configuration == "Escaneos":
                self.escaneos = value
                self.timers.stop()
                self.ui.lbl_nomconfiguration.setText("Escaneos")
                self.ui.lbl_temporizador.setText("0/"+str(value))
                self.barras_fracmento(rangoa,rangob,intervalos)
                self.add_tableview()
                
        except ValueError as e:
            # Manejar la excepción de valores no válidos
            print("Error:", str(e))

    def barras_fracmento(self,rangoa,rangob,intervalos):
        self.list_temp = []
        for i in range(rangoa, rangob + 1, intervalos):
        # Crear un nuevo widget
            frame = QFrame()
            frame.setFixedSize(36, 59)

            # Establecer el color de fondo del QFrame
            frame.setStyleSheet("background-color: rgb(215, 243, 254);")

            label = QLabel()
            label.setStyleSheet("border: none;")
            label.setAlignment(QtCore.Qt.AlignCenter)
            temp = str(i)
            label.setText(temp)

            # Agregar el label al layout del frame
            frame_layout = QHBoxLayout()
            frame_layout.addWidget(label)
            frame.setLayout(frame_layout)
                   
            # Agregar el frame al QHBoxLayout existente
            self.ui.barra_tiempo.addWidget(frame)
            self.add_frame_to_barra_bao_termico(frame)
                    
            print(i)
            # Agregar datos a la lista de temperaturas
            self.list_temp.append([temp, "0", "0", "0", "0"])

    def add_tableview(self):
        # Limpiar el layout actual
        # Obtener el QTableView actual
        table_view = self.ui.tableView_promedios

        # Eliminar cualquier layout existente
        if table_view.layout() is not None:
            # Eliminar todos los elementos hijos del layout actual
            while table_view.layout().count():
                item = table_view.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

        # Crear el modelo de datos
        model = QStandardItemModel()
        model.setColumnCount(5)
        model.setHeaderData(0, QtCore.Qt.Horizontal, "Temperaturas")
        model.setHeaderData(1, QtCore.Qt.Horizontal, "Sensor 1")
        model.setHeaderData(2, QtCore.Qt.Horizontal, "Sensor 2")
        model.setHeaderData(3, QtCore.Qt.Horizontal, "Sensor 3")
        model.setHeaderData(4, QtCore.Qt.Horizontal, "Sensor 4")

        datos = self.list_temp
       

        for row, data in enumerate(datos):
            for col, value in enumerate(data):
                item = QStandardItem(value)
                model.setItem(row, col, item)
        # Ocultar la columna numeradora
        table_view.setModel(model)
        table_view.verticalHeader().hide()

        # Ajustar automáticamente el ancho de las columnas
        #table_view.resizeColumnsToContents()
       
    def update_table_value(self, row, column, new_value):
        # Obtener el modelo de datos del QTableView
        model = self.ui.tableView_promedios.model()

        # Actualizar el valor en la celda específica
        model.setData(model.index(row, column), new_value)

        # Ajustar automáticamente el ancho de las columnas
        #self.ui.tableView_promedios.resizeColumnsToContents()

    def add_frame_to_barra_bao_termico(self,frame ):
        barra_bao_termico_widgets = [
                    self.ui.barra_bao_termico1,
                    self.ui.barra_bao_termico2,
                    self.ui.barra_bao_termico3,
                    self.ui.barra_bao_termico4
        ]
        for barra in barra_bao_termico_widgets:
            new_frame = QFrame()
            new_frame.setFixedSize(36, 59)
            new_frame.setStyleSheet("background-color: rgb(215, 243, 254);")
            new_label = QLabel()
            new_label.setStyleSheet("border: none;")
            new_label.setAlignment(QtCore.Qt.AlignCenter)
            new_label.setText(frame.findChild(QLabel).text())

            new_frame_layout = QHBoxLayout()
            new_frame_layout.addWidget(new_label)
            new_frame.setLayout(new_frame_layout)

            barra.addWidget(new_frame)

    def iniciar_temp(self):
        self.minutos_totales = self.minutos  # Coloca aquí el valor deseado para los minutos totales
        self.minutos_restantes = self.minutos_totales
        self.segundos_restantes = 0
        tiempo = "{:02d}:{:02d}".format(self.minutos_restantes, self.segundos_restantes)
        self.ui.lbl_temporizador.setText(tiempo)

        self.timer.start(1000)  # 1000 milisegundos = 1 segundo

    def actualizar_temporizador(self):
        if self.booltemp == True:
            self.segundos_restantes -= 1
            if self.segundos_restantes < 0:
                self.minutos_restantes -= 1
                self.segundos_restantes = 59

            if self.minutos_restantes < 0:
                self.ui.lbl_temporizador.setText("00:00")
                self.timer.stop()
                # Reproducir el sonido al llegar a cero el temporizador
                file_path = "resources/music/alarm.mp3"

                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                # optiene un arreglo
                self.parra = 1
                self.rows += 1
                valuepromerr =self.escribir_csv_de_txt()
                self.element_color(self.count_button,"#b0f2c2",True,valuepromerr)
                self.booltemp = False
                self.ui.pushButton.setVisible(True)
                self.ui.btn_cancelar.setVisible(False)
                if self.push >= self.ui.barra_tiempo.count()-1:
                   self.ui.btn_curva_ajuste.setDisabled(False)
                self.boolcancel = False
            
            if self.minutos_restantes >= 0:
                tiempo = "{:02d}:{:02d}".format(self.minutos_restantes, self.segundos_restantes)
                self.ui.lbl_temporizador.setText(tiempo)

            if self.boolcancel == True:
                 valuepromerr =self.escribir_csv_de_txt(True)
                 self.timers.stop()
                 self.boolcancel = False
                 self.element_color(self.count_button+1,"#ffb4b0",False,0)
                
    def iniciar_escaneos(self):
        self.escaneos_count = 0
        self.timers.start(1500)  # 1000 milisegundos = 1 segundo
    
    def actualizar_escaneos(self):
        if  self.boolscan == True:
            if self.escaneos_count < self.escaneos:
                self.escaneos_count += 1
                self.ui.lbl_temporizador.setText(str(self.escaneos_count)+"/"+str(self.escaneos))

            elif self.escaneos_count == self.escaneos:
                self.timers.stop()
                print(str(self.escaneos_count)+" - "+str( self.escaneos))
                # Construye la ruta relativa al archivo "alarm.mp3"
                file_path = "resources/music/alarm.mp3"

                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                self.parra = 1
                self.rows += 1
                valuepromerr =self.escribir_csv_de_txt(False)
                self.element_color(self.count_button,"#b0f2c2",True,valuepromerr)
                self.boolscan = False
                self.ui.pushButton.setVisible(True)
                self.ui.btn_cancelar.setVisible(False)
                if self.push >= self.ui.barra_tiempo.count()-1:
                   self.ui.btn_curva_ajuste.setDisabled(False)
                self.boolcancel = False

            if self.boolcancel == True:
                 valuepromerr =self.escribir_csv_de_txt(True)
                 print("Cumpli con mi objetivo")
                 self.timers.stop()
                 self.boolcancel = False
                 self.element_color(self.count_button+1,"#ffb4b0",False,0)
                 
    def escribir_csv_de_txt(self, boools):
        # arreglo
        promerror = []
        # Definir los nombres de los archivos de texto y CSV
        ruta_relativa = "data_sensors/"
        archivos_txt = [ruta_relativa+'datos'+self.sensores[0]+'_temporales.txt',
                        ruta_relativa+'datos'+self.sensores[1]+'_temporales.txt',
                        ruta_relativa+'datos'+self.sensores[2]+'_temporales.txt',
                        ruta_relativa+'datos'+self.sensores[3]+'_temporales.txt']
        archivos_csv = [ruta_relativa+'datos'+self.sensores[0]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[1]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[2]+'_temperatura.csv',
                        ruta_relativa+'datos'+self.sensores[3]+'_temperatura.csv']
        counclum = 0
        for txt_dato, csv_dato in zip(archivos_txt, archivos_csv):
            if boools != True:
                # Leer los datos del archivo de texto
                with open(txt_dato, 'r') as archivo_txt:
                    lineas = archivo_txt.readlines()
                counclum +=1 
                # Convertir los datos en una lista de tuplas
                datos = []
                suma = 0
                count = 0
                grados = 0
                for linea in lineas:
                    tiempo, temperatura = linea.strip().split(',')
                    datos.append((tiempo, temperatura))
                    if re.match(r'^\d+(\.\d+)?$', temperatura):  # Verifica si la temperatura contiene solo números
                        suma += float(temperatura)
                        count += 1

                Temperatura_prueba = self.ui.lbl_prueba_grados.text()
                # extrayendo del label -- Prueba de 15 °C
                temperatura_grados = re.search(r'(\d+)\s*°C', Temperatura_prueba)
                if temperatura_grados:
                    grados = float(temperatura_grados.group(1))
                else:
                    grados = 0.0

                promedio = suma / count if count > 0 else 0
                if grados != 0:
                    error = float(((grados - promedio) / grados) * 100)
                else:
                    error = 0.0
                promedion = round(promedio, 2)
                promerror.append(promedion)
                promerror.append(round(error,2))

                # Guardar los datos en un archivo CSV
                with open(csv_dato, 'a', newline='') as archivo_csv:
                    escritor_csv = csv.writer(archivo_csv)
                    escritor_csv.writerows(datos)

                self.update_table_value(self.rows, counclum, str(promedion))
                print("Si voy a escribir")

            print("Se cancelo borrare todo")
            os.remove(txt_dato)

        return promerror

    def borrar_archivos_csv(self,directorio):
        for archivo in directorio:
            if archivo.endswith(".csv"):
                if os.path.exists(archivo):
                    os.remove(archivo)

    def graficar(self):
        if self.puertooo == None:
           alert = QMessageBox()
           alert.setIcon(QMessageBox.Information)
           alert.setWindowTitle("Information")
           alert.setText("Configura el puerto de arduino.")
           alert.exec_()
           return
        
        self.count_button+=1
        self.push=self.count_button - 1
        layout = self.ui.barra_tiempo  # Suponiendo que self.ui.barra_tiempo es el QVBoxLayout
        print(str(self.push)+" < "+str(layout.count()))
        if self.push < layout.count():
            self.ui.pushButton.setVisible(False)
            self.ui.btn_cancelar.setVisible(True)
            if self.config == "Tiempo":
               self.booltemp = True
               self.iniciar_temp()
               self.element_color(self.count_button,"#d8f8e1",False,0)
               self.iniciar_grafica_arduino()
            elif self.config == "Escaneos":
               self.boolscan = True
               self.iniciar_escaneos()
               self.element_color(self.count_button,"#d8f8e1",False,0)
               self.iniciar_grafica_arduino()
        elif self.push > layout.count():
            """"""
            self.msj("Las pruebas han terminado")
        elif layout.count()==0:
            self.msj("Configura los parametros")

    def msj(self, msj):
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Information)
        alert.setWindowTitle("Information")
        alert.setText(msj)
        alert.exec_()
        self.ui.btn_curva_ajuste.setDisabled(False)            

    def iniciar_grafica_arduino(self):
        
        self.ser = serial.Serial(self.puertooo, baudrate=9600)
        nom_prueba = self.ui.lbl_prueba_grados.text().replace(" ", "")
        nom_prueba = nom_prueba.replace("°", "")
        self.parra = 0

        # Eliminar los elementos existentes en los widgets de gráfica
        self.clear_layout(self.ui.grafica1)
        self.clear_layout(self.ui.grafica2)
        self.clear_layout(self.ui.grafica3)
        self.clear_layout(self.ui.grafica4)
    
        self.grafica1 = Canvas_grafica(self.sensores[0],self.config ,self.minutos,self.escaneos,nom_prueba)
        self.ui.grafica1.addWidget(self.grafica1)
        self.grafica2 = Canvas_grafica(self.sensores[1],self.config ,self.minutos,self.escaneos,nom_prueba)
        self.ui.grafica2.addWidget(self.grafica2)
        self.grafica3 = Canvas_grafica(self.sensores[2],self.config ,self.minutos,self.escaneos,nom_prueba)
        self.ui.grafica3.addWidget(self.grafica3)
        self.grafica4 = Canvas_grafica(self.sensores[3],self.config ,self.minutos,self.escaneos,nom_prueba)
        self.ui.grafica4.addWidget(self.grafica4)
    
        self.iniciar_hilo()

    def leer_datos_arduino(self):
        """
            while True:
            rawString = self.ser.readline().strip()
            partes = [item.decode() for item in rawString.split()]  # ['sensor1', '-127.00']
            print(str(partes) +"Nose_"+ str(self.parra)+" NONONO: "+ str(self.escaneos_count)+" NNINE: "+ str(self.escaneos))
            if self.parra == 1:
                break
            if partes[0] == self.sensores[0]:
                self.grafica1.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[1]:
                self.grafica2.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[2]:
                self.grafica3.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[3]:
                self.grafica4.obtener_temperatura_desde_arduino(partes)
        self.ser.close()

        self.grafica1.close_plt()
        self.grafica2.close_plt()
        self.grafica3.close_plt()
        self.grafica4.close_plt()
        
        """
        self.boodatesensor = False
        while True:
            rawString = self.ser.readline().strip()
            partes = [item.decode() for item in rawString.split()]  # ['sensor1', '-127.00']
            self.boodatesensor = True
            # Lógica de procesamiento de datos
            if self.parra == 1:
                break
            if self.boolcancel == True:
                break
            if partes[0] == self.sensores[0]:
                self.grafica1.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[1]:
                self.grafica2.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[2]:
                self.grafica3.obtener_temperatura_desde_arduino(partes)
            if partes[0] == self.sensores[3]:
                self.grafica4.obtener_temperatura_desde_arduino(partes)

            time.sleep(0.15)  # Esperar 1 segundo
    
        self.ser.close()
        self.boodatesensor = False
        # Cerrar conexiones o realizar otras tareas finales
        self.grafica1.close_plt()
        self.grafica2.close_plt()
        self.grafica3.close_plt()
        self.grafica4.close_plt()

    def iniciar_hilo(self):
        # Crear un hilo para ejecutar el bucle en segundo plano
        thread = threading.Thread(target=self.leer_datos_arduino)
        thread.start()

    def element_color(self,push, color,boopro,value):
        push-=1
        # Suponiendo que self.ui.barra_tiempo es el QVBoxLayout
        barra_bao_termico_widgets = [
                    self.ui.barra_tiempo,
                    self.ui.barra_bao_termico1,
                    self.ui.barra_bao_termico2,
                    self.ui.barra_bao_termico3,
                    self.ui.barra_bao_termico4
        ]
        count = 0
        count1 = 1
        bar = 0
        for barra in barra_bao_termico_widgets:
            layout = barra
            if push < layout.count():
                for i in range(layout.count()):
                    item = layout.itemAt(i)
                    if item.widget():
                        if i == push:
                            self.ui.lbl_prueba_grados.setText("Prueba de "+item.widget().findChild(QLabel).text()+" °C")
                            widget = item.widget()
                            widget.setStyleSheet("background-color: "+color)
                            
                            if boopro and bar > 0:
                              # Obtiene un arreglo donde 0 es el promedio y 1 el factor de error
                                promedio = value[count] #6
                                error = value[count1] #7
                                stringtolp = "Promedio: "+str(promedio) +"\nError: "+ str(error)
                                item.widget().setToolTip(stringtolp)
                                count += 2
                                count1 += 2
                                print(str(count) +"arreglo")

                            print(i)
                            break
            bar +=1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())

# no olvidar cuando importas actualizas las interfaces
# import resources.images.iconos.images_rc