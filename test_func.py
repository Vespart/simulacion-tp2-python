import math
import random
from core.generadores import darDistNorm


def test_darDistNorm(darDistNorm, repeticiones=5):
    print("🧪 Iniciando pruebas para tu versión de darDistNorm...\n")

    for i in range(repeticiones):
        media = 0
        desv = 1
        cantidad = 1000

        # Generar cantidad par de números uniformes
        if cantidad % 2 != 0:
            cantidad += 1
        nums = [random.uniform(1e-10, 1.0) for _ in range(cantidad)]

        try:
            datos = darDistNorm(nums, media, desv)

            assert isinstance(
                datos, list), "La función debe retornar una lista"
            assert len(datos) == cantidad, "La cantidad de datos no coincide"
            assert all(isinstance(x, float)
                       for x in datos), "Todos los valores deben ser float"
            assert all(not math.isnan(x) and not math.isinf(x)
                       for x in datos), "Hay valores inválidos"

            fuera_de_rango = [x for x in datos if x <
                              media - 6*desv or x > media + 6*desv]
            if fuera_de_rango:
                print(f"⚠️ Prueba {i+1}: {len(fuera_de_rango)
                                          } valores fuera de rango esperado")
            else:
                print(f"✅ Prueba {i+1}/{repeticiones} pasada correctamente.")

        except Exception as e:
            print(f"❌ Error en prueba {i+1}: {e}")
            return

    print("\n🎉 Todas las pruebas finalizadas.")


test_darDistNorm(darDistNorm)
