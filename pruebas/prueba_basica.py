"""Diagnóstico reproducible del modelo original, sin modificarlo."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "codigo"))
import model2 as modelo

def main():
    print("Inversión de sensor activa:", modelo._INVERTIR_SENSOR)
    casos = [
        (170, 100, 95),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]
    for rgb in casos:
        print(f"RGB {rgb} -> {modelo.model2(*rgb)}")
    assert modelo.model2(170, 100, 95) == "Verde", (
        "El ejemplo original debe devolver Verde mientras la inversión esté activa"
    )
    print("Diagnóstico básico completado; esto NO demuestra precisión ni inferencia distribuida.")

if __name__ == "__main__":
    main()
