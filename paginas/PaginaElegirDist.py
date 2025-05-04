from PyQt5.QtWidgets import QLabel, QSpinBox, QComboBox, QPushButton
from .PaginaBase import PaginaBase


class PaginaElegirDist(PaginaBase):
    def __init__(self, callback_seleccion, callback_volver, callback_cerrar):
        super().__init__("Elija una distribucion", callback_volver, callback_cerrar)

        self.callback = callback_seleccion

        self.combo = QComboBox()
        self.combo.addItems(["Normal", "Uniforme", "Exponencial Negativa"])

        self.spin = QSpinBox()
        self.spin.setMinimum(1)
        self.spin.setMaximum(1000000)
        self.spin.setValue(100)

        self.set_boton_extra_texto("Continuar")
        self.conectar_boton_extra(self.enviar_datos)

        self.agregar_widget(
            QLabel("Seleccione una distribucion con la que quiera generar los valores: "))
        self.agregar_widget(self.combo)
        self.agregar_widget(
            QLabel("Ingrese la cantidad de valores que desea generar:"))
        self.agregar_widget(self.spin)
        self.agregar_widget(QLabel(
            "(Para la distribucion Normal elija un numero par o sera elegido el proximo numero par a su valor ingresado)"))

    def enviar_datos(self):
        dist = self.combo.currentText()
        cantidad = self.spin.value()
        self.callback(dist, cantidad)
