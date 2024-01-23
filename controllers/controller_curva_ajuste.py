from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from views.View_Curva_ajuste.view_curva_ajuste_ui import Ui_Dialog as calibration
from models.Grafica import Canvas_grafica_promedios
from models.Mediador import Mediator,Component
import pandas as pd
import re 
import csv


class MainCalibration(QDialog):
    data_signal = QtCore.pyqtSignal(bool)
    def __init__(self):
        
        super(MainCalibration, self).__init__()
        # Crear una instancia de la clase Ui_Dialog
        self.ui = calibration()
        # Configurar la interfaz de usuario
        self.ui.setupUi(self)
        self.ui.btn_regresar.clicked.connect(self.regresar_view_principal)
        self.ui.btn_exportar_datos.clicked.connect(self.exp_data)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        #self.drag_start_position = None
        self.canca1 = Canvas_grafica_promedios("Sensor1")
        self.canca2 = Canvas_grafica_promedios("Sensor2")
        self.canca3 = Canvas_grafica_promedios("Sensor3")
        self.canca4 = Canvas_grafica_promedios("Sensor4")

        self.temperatura_clmn_1 = []
        self.termpar_1_clmn_2 = []
        self.termpar_2_clmn_3 = []
        self.termpar_3_clmn_4 = []
        self.termpar_4_clmn_5 = []

        self.mediator = Mediator()
        self.component = Component(self.mediator,"Controller_curva_ajuste")
        self.mediator.add(self.component)

    def exp_data(self):
        """"""
        # Ejemplo de uso
        df_temporal = 'pruebas_sensores.csv'
        df_temp = 'promedios_sensores.csv'
        df_archivo_exel = 'data_calibration.xlsx'

        sensores = ["sensor1", "sensor2", "sensor3", "sensor4"]
        ruta_relativa = "data_sensors/"
        archivos_csv = [ruta_relativa + 'datos' + sensor + '_temperatura.csv' for sensor in sensores]

        data = {"Prueba": [], "sensor1": [], "sensor2": [], "sensor3": [], "sensor4": []}
        # Leer los archivos CSV y guardar los datos en el diccionario
        max_length = 0  # Variable para almacenar la longitud máxima de las listas
        # Leer los archivos CSV y guardar los datos en el diccionario
        for archivo, sensor in zip(archivos_csv, sensores):
            with open(archivo, 'r') as archivo_csv:
                # Crear un lector CSV
                lector = csv.reader(archivo_csv)
                for linea in lector:
                    valor_data = linea[1]
                    if not re.match(r'^\d+(\.\d+)?$', valor_data):
                        numero = int(re.search(r'sensor\d+_Pruebade(\d+)C', valor_data).group(1))
                    elif re.match(r'^\d+(\.\d+)?$', valor_data):
                        data["Prueba"].append(numero)
                        max_length = max(max_length, len(data["Prueba"]))
                        data[sensor].append(valor_data)
                        max_length = max(max_length, len(data[sensor]))

        # Asegurar que todas las listas tengan la misma longitud
        for columna in data:
            diff = max_length - len(data[columna])
            data[columna] += ['-'] * diff

        # Crear el DataFrame
        df = pd.DataFrame(data)

        # Encontrar el índice de la primera fila que contiene "-"
        indice_inicio = df[df == "-"].any(axis=1).idxmax()

        # Eliminar todas las filas a partir del índice de inicio
        df = df.iloc[:indice_inicio]

        # Reiniciar los índices del DataFrame
        df.reset_index(drop=True, inplace=True)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv(df_temporal, index=False)
        # Aplicar permisos de solo lectura al archivo generado
        #os.chmod(df_temporal, 0o444)

        data_list = [
            [valor1, valor2, valor3, valor4, valor5]  # Supongamos que estos son tus datos
            for valor1, valor2, valor3, valor4, valor5 in zip(
                self.temperatura_clmn_1,
                self.termpar_1_clmn_2,
                self.termpar_2_clmn_3,
                self.termpar_3_clmn_4,
                self.termpar_4_clmn_5
            )
        ]

        # Crear el DataFrame con los datos
        dfq = pd.DataFrame(data_list, columns=['Pruebas', 'Promedio S1', 'Promedio S2', 'Promedio S3', 'Promedio S4'])
        dfq.to_csv(df_temp,index = False)

                # Cargar los archivos CSV en pandas
        df1 = pd.read_csv(df_temporal)
        df2 = pd.read_csv(df_temp)

        # Crear un objeto ExcelWriter
        writer = pd.ExcelWriter(df_archivo_exel, engine='xlsxwriter')

        # Escribir los DataFrames en hojas separadas
        df1.to_excel(writer, sheet_name='Data prueba Sensores', index=False)
        df2.to_excel(writer, sheet_name='Promedios', index=False)

        # Guardar el archivo Excel
        writer.close()

        # Abrir el cuadro de diálogo de guardado de archivos
        dialogo = QFileDialog()
        dialogo.setDefaultSuffix('.xlsx')
        dialogo.setAcceptMode(QFileDialog.AcceptSave)
        dialogo.setFileMode(QFileDialog.AnyFile)
        dialogo.setNameFilters(["Excel Files (*.xlsx)"])
        if dialogo.exec_():
            # Obtener la ruta y el nombre de archivo seleccionados
            ruta_guardado = dialogo.selectedFiles()[0]
            
            # Guardar el archivo Excel en la ruta seleccionada
            if ruta_guardado:
                writer = pd.ExcelWriter(ruta_guardado, engine='xlsxwriter')
                df1.to_excel(writer, sheet_name='Data prueba Sensores', index=False)
                df2.to_excel(writer, sheet_name='Promedios', index=False)
                writer.close()

    def user_action(self):
        msj = self.mediator.get_message(self.component)
        if msj is not None:
           self.list_temp = msj
           self.add_tableview()
           data_list = self.recuperation_elemens_table()  # Obtener la lista de datos

            # Acceder a los elementos de la columna 1
            # Acceder a los elementos de la columna 1 y convertirlos a float
           self.temperatura_clmn_1 = [float(fila[0]) for fila in data_list]
           self.termpar_1_clmn_2 = [float(fila[1]) for fila in data_list]
           self.termpar_2_clmn_3 = [float(fila[2]) for fila in data_list]
           self.termpar_3_clmn_4 = [float(fila[3]) for fila in data_list]
           self.termpar_4_clmn_5 = [float(fila[4]) for fila in data_list]

           self.canca1.datos_prueba_(self.termpar_1_clmn_2,self.temperatura_clmn_1)
           self.canca2.datos_prueba_(self.termpar_2_clmn_3,self.temperatura_clmn_1)
           self.canca3.datos_prueba_(self.termpar_3_clmn_4,self.temperatura_clmn_1)
           self.canca4.datos_prueba_(self.termpar_4_clmn_5,self.temperatura_clmn_1)

           self.ui.lbl_constantea_grafica1.setText("a = "+ str(self.canca1.getter_a()))
           self.ui.lbl_constanteb_grafica1.setText("b = "+ str(self.canca1.getter_b()))
           self.ui.lbl_ecuacion_grafica1.setText(str(self.canca1.getter_label_ecuacion()))
           
           self.ui.lbl_constantea_grafica2.setText("a = "+ str(self.canca2.getter_a()))
           self.ui.lbl_constanteb_grafica2.setText("b = "+ str(self.canca2.getter_b()))
           self.ui.lbl_ecuacion_grafica2.setText(str(self.canca2.getter_label_ecuacion()))
           

           self.ui.lbl_constantea_grafica3.setText("a = "+ str(self.canca3.getter_a()))
           self.ui.lbl_constanteb_grafica3.setText("b = "+ str(self.canca3.getter_b()))
           self.ui.lbl_ecuacion_grafica3.setText(str(self.canca3.getter_label_ecuacion()))
           

           self.ui.lbl_constantea_grafica4.setText("a = "+ str(self.canca4.getter_a()))
           self.ui.lbl_constanteb_grafica4.setText("b = "+ str(self.canca4.getter_b()))
           self.ui.lbl_ecuacion_grafica4.setText(str(self.canca4.getter_label_ecuacion()))
           
           self.ui.grafica_layout1.addWidget(self.canca1)
           self.ui.grafica_layout2.addWidget(self.canca2)
           self.ui.grafica_layout3.addWidget(self.canca3)
           self.ui.grafica_layout4.addWidget(self.canca4)
    
    def add_tableview(self):
        # Limpiar el layout actual
        # Obtener el QTableView actual
        table_view = self.ui.tableview_promedios

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
        

    def recuperation_elemens_table(self):
        table_view = self.ui.tableview_promedios  # Obtén una referencia al QTableView
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
        return data_list

    def regresar_view_principal(self):
        self.data_signal.emit(True)
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

