def aplicar_estilo(qapp, modo="claro"):
    ruta = "./recursos/estilo_claro.qss" if modo == "claro" else "./recursos/estilo_oscuro.qss"
    with open(ruta, "r") as f:
        estilo = f.read()
        qapp.setStyleSheet(estilo)