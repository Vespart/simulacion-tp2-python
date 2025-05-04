from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt


class PaginaBase(QWidget):
    def __init__(self, titulo=None, callback_volver=None, callback_cerrar=None):
        super().__init__()
        self.callback_volver = callback_volver
        self.callback_cerrar = callback_cerrar

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.boton_cerrar = QPushButton("✖")
        self.boton_cerrar.setFixedSize(32, 32)
        self.boton_cerrar.setStyleSheet(
            "background-color: #e57373; color: white;")
        self.boton_cerrar.clicked.connect(self.cerrar)

        header_layout = QHBoxLayout()
        header_layout.addStretch()
        header_layout.addWidget(self.boton_cerrar)

        self.layout.addLayout(header_layout)

        self.contenedor = QVBoxLayout()
        self.layout.addLayout(self.contenedor)
        self.layout.addStretch()

        if titulo:
            self.contenedor.addWidget(QLabel(f"<h1>{titulo}</h1>"))

        self.boton_volver = QPushButton("← Volver")
        self.boton_volver.setFixedHeight(30)
        self.boton_volver.clicked.connect(self.volver)

        self.boton_extra = QPushButton("")
        self.boton_extra.setFixedHeight(30)

        footer_layout = QHBoxLayout()
        footer_layout.addWidget(self.boton_volver)
        footer_layout.addStretch()
        footer_layout.addWidget(self.boton_extra)

        self.layout.addLayout(footer_layout)

    def agregar_widget(self, widget):
        self.contenedor.addWidget(widget)

    def volver(self):
        if self.callback_volver:
            self.callback_volver(self)

    def cerrar(self):
        if self.callback_cerrar:
            self.callback_cerrar(self)

    def set_boton_extra_texto(self, texto):
        self.boton_extra.setText(texto)

    def conectar_boton_extra(self, funcion):
        self.boton_extra.clicked.connect(funcion)
