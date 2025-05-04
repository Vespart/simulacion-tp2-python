from PyQt5.QtWidgets import QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget, QTableWidget, QTableWidgetItem, QPlainTextEdit, QHeaderView
from PyQt5.QtCore import Qt
from .PaginaBase import PaginaBase
from sympy import nextprime
from math import sqrt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PaginaResultados(PaginaBase):
    def __init__(self, callback_volver, callback_cerrar, datos: list[float], nombre: str = ""):
        super().__init__("Resultados de la Generación", callback_volver, callback_cerrar, )
        self.datos = datos
        self.distribucion = nombre

        self.agregar_widget(
            QLabel(f"<h2>Resultados para distribución: {self.distribucion}</h2>"))

        self.stack = QStackedWidget()
        self.stack.addWidget(self.crear_tabla())
        self.stack.addWidget(self.crear_histograma())
        self.stack.addWidget(self.crear_serie())

        botones_layout = QHBoxLayout()
        self.btnTabla = QPushButton("Mostrar Tabla de Frecuencias")
        self.btnHist = QPushButton("Mostrar Histograma")
        self.btnSerie = QPushButton("Mostrar Serie de Numeros")

        self.btnTabla.clicked.connect(lambda: self.stack.setCurrentIndex(0))
        self.btnHist.clicked.connect(lambda: self.stack.setCurrentIndex(1))
        self.btnSerie.clicked.connect(lambda: self.stack.setCurrentIndex(2))

        botones_layout.addWidget(self.btnTabla)
        botones_layout.addWidget(self.btnHist)
        botones_layout.addWidget(self.btnSerie)

        self.contenedor.addLayout(botones_layout)
        self.boton_extra.hide()
        self.agregar_widget(self.stack)

    def crear_tabla(self):
        intervalos = nextprime(self.redondear(sqrt(len(self.datos))))
        tabla = QTableWidget(intervalos, 4)
        tabla.setHorizontalHeaderLabels(
            ["Intervalo N°", "Límite Inferior", "Límite Superior", "Frecuencia Observada"])
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        minim = min(self.datos)
        maxim = max(self.datos)
        alcance = maxim - minim
        rango = alcance / intervalos
        li = minim

        n_intervalo = 1

        while n_intervalo <= intervalos:
            ls = round(li + rango - (0.0001 / 10), 4)
            fo = sum(1 for x in self.datos if li <= x < ls)
            # Crear cada celda como no editable
            celda_intervalo = QTableWidgetItem(str(n_intervalo))
            celda_intervalo.setFlags(
                celda_intervalo.flags() & ~Qt.ItemIsEditable)

            celda_li = QTableWidgetItem(str(li))
            celda_li.setFlags(celda_li.flags() & ~Qt.ItemIsEditable)

            celda_ls = QTableWidgetItem(str(ls))
            celda_ls.setFlags(celda_ls.flags() & ~Qt.ItemIsEditable)

            celda_fo = QTableWidgetItem(str(fo))
            celda_fo.setFlags(celda_fo.flags() & ~Qt.ItemIsEditable)

            # Insertar en la tabla
            tabla.setItem(n_intervalo - 1, 0, celda_intervalo)
            tabla.setItem(n_intervalo - 1, 1, celda_li)
            tabla.setItem(n_intervalo - 1, 2, celda_ls)
            tabla.setItem(n_intervalo - 1, 3, celda_fo)

            li = ls
            n_intervalo += 1
        return tabla

    def crear_histograma(self):
        fig = Figure(figsize=(6, 4), facecolor='#f9f9f9')  # fondo claro
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)

        # Estilo de barras
        n, bins, patches = ax.hist(
            self.datos,
            bins=nextprime(self.redondear(sqrt(len(self.datos)))),
            edgecolor='white',
            linewidth=1.2,
            color='#5c7cfa',   # azul violeta suave
            alpha=0.9
        )

        # Títulos con estilo
        ax.set_title(f"Histograma de Frecuencias de Distribucion {self.distribucion}", fontsize=14,
                     fontweight='bold', color='#343a40')
        ax.set_xlabel("Valores", fontsize=12)
        ax.set_ylabel("Frecuencia Observada", fontsize=12)

        # Ejes con estilo
        ax.tick_params(axis='both', labelsize=10)
        ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
        ax.set_facecolor('#ffffff')  # fondo del gráfico
        return canvas

    def crear_serie(self):
        texto = QPlainTextEdit()
        texto.setReadOnly(True)
        linea = ', '.join(f"{x:.4f}" for x in self.datos)
        texto.setPlainText(linea)
        return texto

    @staticmethod
    def redondear(x):
        if x >= 0:
            return int(x + 0.5)
        else:
            return int(x - 0.5)

    def frecuencia_en_intervalo(datos, li, ls):
        return sum(1 for x in datos if li <= x < ls)
