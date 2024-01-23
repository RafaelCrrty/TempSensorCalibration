import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

class Canvas_grafica(FigureCanvas):
    def __init__(self,sensor,configuration,minutos,escaneos,nom_pruebas, parent=None):
        self.fig, self.ax = plt.subplots(1, dpi=95, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)
        self.sensor = sensor
        self.segundos = minutos
        self.segundos *= 60
        self.segundos -=3
        self.scan = escaneos # escaneos
        self.configuration = configuration # esto es para la configuracion si escaneos o tiempo
        self.tiempox = []
        self.temperaturay = []
        self.count = 0
        self.nom_prue = nom_pruebas
       
    def actualizar_temp(self,arrtemp):
        if self.configuration == "Tiempo":
            if self.count < self.segundos:
                self.count += 1
                self.datos_arduino_grafica(arrtemp)

        elif self.configuration == "Escaneos":
            if self.count <= self.scan:
                self.count += 1
                self.datos_arduino_grafica(arrtemp)

    def datos_arduino_grafica(self,arrtemp):
        temperatura = arrtemp
        self.tiempox.append(self.count)
        self.temperaturay.append(float(temperatura[1]))
        self.ax.plot(self.temperaturay, color='red')
        self.ax.set_xlabel("Tiempo s")
        self.ax.set_ylabel("Temperatura")
        self.ax.set_title(self.sensor, size=9)
        self.draw()
            
        tiempostr= str(self.count)
        tempstr = str(temperatura[1])

        if self.count == 1:
        # Agrega el dato inicial de temperatura (5 grados)
            tiempostr = '1'
            tempstr = self.sensor+"_"+self.nom_prue

        with open('data_sensors/datos'+self.sensor+'_temporales.txt', 'a', encoding='utf-8') as archivo_txt:
            text = tiempostr+","+tempstr + "\n"
            archivo_txt.write(text)

    def obtener_temperatura_desde_arduino(self,partes):
        self.actualizar_temp(partes)

    def close_plt(self):
        plt.close(self.fig)  # Cierra

class Canvas_grafica_promedios(FigureCanvas):
    def __init__(self,sensor, parent=None):
        self.sensor = sensor
        self.ecuacion_recta = ""
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(5, 5), sharey=True, facecolor='white')
        super().__init__(self.fig)

    def datos_arduino_grafica(self):
        # Realizar el ajuste lineal
        self.a, self.b = np.polyfit(self.xprueba, self.yppromedio, 1)
        if self.a >= 0 and self.b >= 0:
           self.ecuacion_recta = f"y = {round(self.a, 4)} * x + {round(self.b, 4)}"
        elif self.a >= 0 and self.b < 0:
            self.ecuacion_recta = f"y = {round(self.a, 4)} * x - {-round(self.b, 4)}"
        elif self.a < 0 and self.b >= 0:
            self.ecuacion_recta = f"y = -{-round(self.a, 4)} * x + {round(self.b, 4)}"
        else:
            self.ecuacion_recta = f"y = -{-round(self.a, 4)} * x - {-round(self.b, 4)}"
            
        # Generar los valores predichos por la recta ajustada
        ejey_pred = []
        for x in self.xprueba:
            y_pred =  self.a * x +  self.b
            ejey_pred.append(y_pred)

        # Graficar los puntos y la recta ajustada
        self.scatter_plotP = self.ax.scatter(self.xprueba,self.yppromedio, marker='D' , color='blue',label='Temperaturas')       
        self.ax.plot(self.xprueba,ejey_pred,linestyle = '--', color='red', label='Ajuste')
        self.ax.set_xlabel("Temperatura de sensor (°C)")
        self.ax.set_ylabel("Temperatura de referencia (°C)")
        self.ax.set_title(self.sensor, size=9)
        self.draw()
        # Agregar leyenda

    def getter_a(self):
        return round(self.a, 4)
    
    def getter_b(self):
        return round(self.b, 4)

    def getter_label_ecuacion(self):
        return self.ecuacion_recta

    def datos_prueba_(self, x_pruebas, y_promedios):
        self.limpiar_grafica()
        self.xprueba = x_pruebas
        self.yppromedio = y_promedios
        self.datos_arduino_grafica()

    def limpiar_grafica(self):
        self.ax.clear()
        self.draw()

    def close_plt(self):
        plt.close(self.fig)
