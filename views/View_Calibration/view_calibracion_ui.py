# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\rafae\OneDrive\Escritorio\Proyecto_Calibration_termopar\views\View_Calibration\view_calibracion.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1920, 1042)
        Form.setStyleSheet("QWidget{\n"
"                    border-radius: 10px;\n"
"    }")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(570, 170, 1341, 871))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #ccc;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 50, 651, 381))
        self.frame_2.setStyleSheet("#frame_2 {\n"
"border: 1px solid red;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 631, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.grafica1 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.grafica1.setContentsMargins(0, 0, 0, 0)
        self.grafica1.setObjectName("grafica1")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(670, 50, 661, 381))
        self.frame_3.setStyleSheet("#frame_3 {\n"
"border: 1px solid red;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.frame_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 10, 641, 361))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.grafica2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.grafica2.setContentsMargins(0, 0, 0, 0)
        self.grafica2.setObjectName("grafica2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 440, 651, 381))
        self.frame_4.setStyleSheet("#frame_4 {\n"
"border: 1px solid red;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame_4)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(9, 10, 631, 361))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.grafica3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.grafica3.setContentsMargins(0, 0, 0, 0)
        self.grafica3.setObjectName("grafica3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(670, 440, 661, 381))
        self.frame_5.setStyleSheet("#frame_5 {\n"
"border: 1px solid red;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.frame_5)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(9, 10, 641, 361))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.grafica4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.grafica4.setContentsMargins(0, 0, 0, 0)
        self.grafica4.setObjectName("grafica4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(600, 830, 131, 31))
        self.pushButton.setStyleSheet("background-color: rgb(107, 167, 46);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.btn_cancelar = QtWidgets.QPushButton(self.frame)
        self.btn_cancelar.setGeometry(QtCore.QRect(600, 830, 131, 31))
        self.btn_cancelar.setStyleSheet("background-color: rgb(255, 138, 74);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.btn_cancelar.setObjectName("btn_cancelar")
        self.btn_puerto_arduino = QtWidgets.QPushButton(self.frame)
        self.btn_puerto_arduino.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.btn_puerto_arduino.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/images/iconos/calibre.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_puerto_arduino.setIcon(icon)
        self.btn_puerto_arduino.setIconSize(QtCore.QSize(35, 35))
        self.btn_puerto_arduino.setObjectName("btn_puerto_arduino")
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.btn_cancelar.raise_()
        self.pushButton.raise_()
        self.btn_puerto_arduino.raise_()
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(10, 40, 551, 121))
        self.frame_6.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #ccc;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.lbl_prueba_grados = QtWidgets.QLabel(self.frame_6)
        self.lbl_prueba_grados.setGeometry(QtCore.QRect(10, 15, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_prueba_grados.setFont(font)
        self.lbl_prueba_grados.setStyleSheet("QLabel{\n"
"border: none\n"
"}")
        self.lbl_prueba_grados.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_prueba_grados.setObjectName("lbl_prueba_grados")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_6)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 531, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.barra_tiempo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.barra_tiempo.setContentsMargins(0, 0, 0, 0)
        self.barra_tiempo.setObjectName("barra_tiempo")
        self.btn_configuracion_prueba = QtWidgets.QPushButton(self.frame_6)
        self.btn_configuracion_prueba.setGeometry(QtCore.QRect(500, 10, 41, 41))
        self.btn_configuracion_prueba.setStyleSheet("")
        self.btn_configuracion_prueba.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/images/iconos/configuraciones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_configuracion_prueba.setIcon(icon1)
        self.btn_configuracion_prueba.setIconSize(QtCore.QSize(30, 30))
        self.btn_configuracion_prueba.setObjectName("btn_configuracion_prueba")
        self.btn_clear_barra = QtWidgets.QPushButton(self.frame_6)
        self.btn_clear_barra.setGeometry(QtCore.QRect(450, 10, 41, 41))
        self.btn_clear_barra.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/images/iconos/borrar_.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear_barra.setIcon(icon2)
        self.btn_clear_barra.setIconSize(QtCore.QSize(30, 30))
        self.btn_clear_barra.setObjectName("btn_clear_barra")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(10, 170, 551, 871))
        self.frame_7.setStyleSheet("QFrame {\n"
"    background-color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #ccc;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.3);\n"
"}\n"
"")
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.lbl_detalles_pruebas = QtWidgets.QLabel(self.frame_7)
        self.lbl_detalles_pruebas.setGeometry(QtCore.QRect(10, 10, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detalles_pruebas.setFont(font)
        self.lbl_detalles_pruebas.setStyleSheet("QLabel{\n"
"border: none\n"
"}\n"
"")
        self.lbl_detalles_pruebas.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_detalles_pruebas.setObjectName("lbl_detalles_pruebas")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 531, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.barra_bao_termico1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.barra_bao_termico1.setContentsMargins(0, 0, 0, 0)
        self.barra_bao_termico1.setObjectName("barra_bao_termico1")
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 81, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 170, 531, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.barra_bao_termico2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.barra_bao_termico2.setContentsMargins(0, 0, 0, 0)
        self.barra_bao_termico2.setObjectName("barra_bao_termico2")
        self.label_5 = QtWidgets.QLabel(self.frame_7)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(10, 260, 531, 61))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.barra_bao_termico3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.barra_bao_termico3.setContentsMargins(0, 0, 0, 0)
        self.barra_bao_termico3.setObjectName("barra_bao_termico3")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        self.label_6.setGeometry(QtCore.QRect(10, 340, 81, 16))
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame_7)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(10, 360, 531, 61))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.barra_bao_termico4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.barra_bao_termico4.setContentsMargins(0, 0, 0, 0)
        self.barra_bao_termico4.setObjectName("barra_bao_termico4")
        self.tableView_promedios = QtWidgets.QTableView(self.frame_7)
        self.tableView_promedios.setGeometry(QtCore.QRect(20, 470, 501, 351))
        self.tableView_promedios.setStyleSheet("")
        self.tableView_promedios.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableView_promedios.setObjectName("tableView_promedios")
        self.lbl_detalles_pruebas_2 = QtWidgets.QLabel(self.frame_7)
        self.lbl_detalles_pruebas_2.setGeometry(QtCore.QRect(10, 440, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_detalles_pruebas_2.setFont(font)
        self.lbl_detalles_pruebas_2.setStyleSheet("QLabel{\n"
"border: none\n"
"}\n"
"")
        self.lbl_detalles_pruebas_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_detalles_pruebas_2.setObjectName("lbl_detalles_pruebas_2")
        self.btn_curva_ajuste = QtWidgets.QPushButton(self.frame_7)
        self.btn_curva_ajuste.setGeometry(QtCore.QRect(210, 830, 131, 31))
        self.btn_curva_ajuste.setStyleSheet("background-color: rgb(107, 167, 46);\n"
"\n"
"color: rgb(255, 255, 255);")
        self.btn_curva_ajuste.setObjectName("btn_curva_ajuste")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(860, 60, 721, 71))
        self.label_20.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.frame_20 = QtWidgets.QFrame(Form)
        self.frame_20.setGeometry(QtCore.QRect(-10, 0, 1991, 31))
        self.frame_20.setStyleSheet("background-color:#97775b")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.lbl_temporizador = QtWidgets.QLabel(Form)
        self.lbl_temporizador.setGeometry(QtCore.QRect(1680, 100, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_temporizador.setFont(font)
        self.lbl_temporizador.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_temporizador.setObjectName("lbl_temporizador")
        self.lbl_nomconfiguration = QtWidgets.QLabel(Form)
        self.lbl_nomconfiguration.setGeometry(QtCore.QRect(1670, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_nomconfiguration.setFont(font)
        self.lbl_nomconfiguration.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_nomconfiguration.setObjectName("lbl_nomconfiguration")
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(570, 40, 191, 131))
        self.frame_8.setStyleSheet("background-image: url(:/images/logo_uni_unam.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, -1, 1921, 1041))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.stackedWidget.addWidget(self.page_6)
        self.stackedWidget.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.label_20.raise_()
        self.frame_20.raise_()
        self.lbl_temporizador.raise_()
        self.lbl_nomconfiguration.raise_()
        self.frame_8.raise_()
        self.frame.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Iniciar"))
        self.btn_cancelar.setText(_translate("Form", "Cancelar"))
        self.btn_puerto_arduino.setToolTip(_translate("Form", "<html><head/><body><p>Configuración de Arduino</p></body></html>"))
        self.lbl_prueba_grados.setText(_translate("Form", "Prueba de # °C"))
        self.btn_configuracion_prueba.setToolTip(_translate("Form", "<html><head/><body><p>Configurar pruebas</p></body></html>"))
        self.btn_clear_barra.setToolTip(_translate("Form", "<html><head/><body><p>Borrar Configuraciones</p></body></html>"))
        self.lbl_detalles_pruebas.setText(_translate("Form", "Detalles de Medición con el Baño Térmico"))
        self.label_2.setText(_translate("Form", "Sensor 1"))
        self.label_4.setText(_translate("Form", "Sensor 2"))
        self.label_5.setText(_translate("Form", "Sensor 3"))
        self.label_6.setText(_translate("Form", "Sensor 4"))
        self.lbl_detalles_pruebas_2.setText(_translate("Form", "Promedios de cada sensor "))
        self.btn_curva_ajuste.setText(_translate("Form", "Curva ajuste"))
        self.label_20.setText(_translate("Form", "Calibración de sensores baño térmico"))
        self.lbl_temporizador.setText(_translate("Form", "..."))
        self.lbl_nomconfiguration.setText(_translate("Form", "Temporizador"))

import resources.images.iconos.images_rc