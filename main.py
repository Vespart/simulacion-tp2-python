import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QStackedWidget
from paginas.PaginaInicio import PaginaInicio
from paginas.PaginaElegirDist import PaginaElegirDist
from paginas.PaginaValsExp import PaginaValsExp
from paginas.PaginaValsNorm import PaginaValsNorm
from paginas.PaginaValsUnif import PaginaValsUnif
from paginas.PaginaResultados import PaginaResultados
from core.generadores import generar_numeros_pseudoaleatorios, darDistExp, darDistNorm, darDistUnifAB


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generador de Variables Aleatorias")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)
        self.setLayout(layout)

        self.pagina_inicio = PaginaInicio(
            self.elegir_dist, self.volver, self.cerrar_aplicacion)
        self.stack.addWidget(self.pagina_inicio)

    def elegir_dist(self):
        pagina_elegir = PaginaElegirDist(
            self.ir_a_parametros, self.volver, self.cerrar_aplicacion)
        self.stack.addWidget(pagina_elegir)
        self.stack.setCurrentWidget(pagina_elegir)

    def ir_a_parametros(self, distribucion, cantidad):
        self.distribucion = distribucion
        self.cantidad = cantidad

        if distribucion == "Normal":
            pagina = PaginaValsNorm(
                cantidad, self.ir_a_resultados, self.volver, self.cerrar_aplicacion)
        elif distribucion == "Exponencial Negativa":
            pagina = PaginaValsExp(
                cantidad, self.ir_a_resultados, self.volver, self.cerrar_aplicacion)
        elif distribucion == "Uniforme":
            pagina = PaginaValsUnif(
                cantidad, self.ir_a_resultados, self.volver, self.cerrar_aplicacion)

        self.stack.addWidget(pagina)
        self.stack.setCurrentWidget(pagina)

    def ir_a_resultados(self, tipo, cantidad, *parametros):
        datos = generar_numeros_pseudoaleatorios(cantidad)
        if tipo == "Normal":
            datos = darDistNorm(datos, *parametros)
        elif tipo == "Exponencial Negativa":
            datos = darDistExp(datos, *parametros)
        elif tipo == "Uniforme":
            datos = darDistUnifAB(datos, *parametros)

        pagina_resultados = PaginaResultados(
            self.volver, self.cerrar_aplicacion, datos, tipo)
        self.stack.addWidget(pagina_resultados)
        self.stack.setCurrentWidget(pagina_resultados)

    def volver(self, pagina_actual):
        self.stack.removeWidget(pagina_actual)
        self.stack.setCurrentIndex(self.stack.count() - 1)

    @staticmethod
    def cerrar_aplicacion(self):
        QApplication.quit()


def aplicar_estilo(qapp, ruta="./recursos/estilos.qss"):
    with open(ruta, "r") as f:
        estilo = f.read()
        qapp.setStyleSheet(estilo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplicar_estilo(app)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
