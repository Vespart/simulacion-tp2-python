from PyQt5.QtWidgets import QLabel, QSpinBox, QPushButton
from .PaginaBase import PaginaBase


class PaginaValsUnif(PaginaBase):
    def __init__(self, cantidad, callback_generado, callback_volver, callback_cerrar):
        super().__init__("Parametros de Uniforme entre A y B",
                         callback_volver, callback_cerrar)
        self.cantidad = cantidad
        self.callback = callback_generado

        self.entrada_a = QSpinBox()
        self.entrada_a.setValue(0)
        self.entrada_a.valueChanged.connect(self.actualizar_min_b)

        self.entrada_b = QSpinBox()
        self.entrada_b.setValue(1)

        # Hay que decidir si es que queremos que los valores de A y B sean enteros o que tambien puedan ser flotantes

        self.set_boton_extra_texto("Generar")
        self.conectar_boton_extra(self.generar)

        self.agregar_widget(QLabel("Ingrese el valor de A: "))
        self.agregar_widget(self.entrada_a)
        self.agregar_widget(QLabel("Ingrese el valor de B: "))
        self.agregar_widget(self.entrada_b)

    def generar(self):
        a = self.entrada_a.value()
        b = self.entrada_b.value()

        self.callback("Uniforme", self.cantidad, a, b)

    def actualizar_min_b(self):
        nuevo_min = self.entrada_a.value() + 1
        self.entrada_b.setMinimum(nuevo_min)
        if self.entrada_b.value() <= self.entrada_a.value():
            self.entrada_b.setValue(nuevo_min)
