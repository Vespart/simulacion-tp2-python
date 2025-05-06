from PyQt5.QtWidgets import QDoubleSpinBox, QLabel
from .PaginaBase import PaginaBase


class PaginaValsExp(PaginaBase):
    def __init__(self, cantidad, intervalos, callback_generado, callback_volver, callback_cerrar):
        super().__init__("Parametros para Exponencial Negativa",
                         callback_volver, callback_cerrar)
        self.cantidad = cantidad
        self.callback = callback_generado
        self.intervalos = intervalos

        self.entrada_lmd = QDoubleSpinBox()
        self.entrada_lmd.setDecimals(4)
        self.entrada_lmd.setSingleStep(0.0001)
        self.entrada_lmd.setValue(0)
        self.entrada_lmd.setRange(0.0001, 1e6)

        self.set_boton_extra_texto("Generar")
        self.conectar_boton_extra(self.generar)

        self.agregar_widget(QLabel("Ingrese el valor de Lambda : "))
        self.agregar_widget(self.entrada_lmd)

    def generar(self):
        lmd = self.entrada_lmd.value()
        self.callback("Exponencial Negativa", self.cantidad, self.intervalos, lmd)
