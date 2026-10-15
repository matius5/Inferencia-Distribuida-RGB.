################################################################(################
# model2 - Árbol de decisión (Grupo de Mateo, Jesus R y Daniel) (sin scikit-learn porque daba error)
# Árbol CART con índice Gini. Python puro: no requiere instalar nada.


_INVERTIR_SENSOR = True
 
# Datos de entrenamiento (muestras RGB en rango 0 a 255)
_X_TRAIN = [
    # ROJO (clase 1)
    [255, 0, 0], [200, 30, 20], [180, 50, 10], [220, 15, 15], [170, 100, 95],
    # VERDE (clase 2)
    [0, 255, 0], [20, 200, 30], [50, 180, 10], [15, 220, 15], [80, 190, 70],
    # AZUL (clase 3)
    [0, 0, 255], [30, 20, 200], [10, 50, 180], [15, 15, 220], [70, 80, 200]
]
 
# Etiquetas: 1 = Rojo, 2 = Verde, 3 = Azul
_Y_TRAIN = [1]*5 + [2]*5 + [3]*5
 
_CLASES_NOMBRES = {1: "Rojo", 2: "Verde", 3: "Azul"}
 
 
def _gini(etiquetas):
    n = len(etiquetas)
    return 1.0 - sum((etiquetas.count(c) / n) ** 2 for c in set(etiquetas))
 
 
def _construir(X, y):
    # Hoja: todas las muestras son de la misma clase
    if len(set(y)) == 1:
        return y[0]
 
    mejor = None  # (gini ponderado, característica, umbral)
    for f in range(3):
        valores = sorted(set(fila[f] for fila in X))
        for a, b in zip(valores, valores[1:]):
            umbral = (a + b) / 2
            izq = [y[i] for i in range(len(X)) if X[i][f] <= umbral]
            der = [y[i] for i in range(len(X)) if X[i][f] > umbral]
            g = (len(izq) * _gini(izq) + len(der) * _gini(der)) / len(y)
            if mejor is None or g < mejor[0]:
                mejor = (g, f, umbral)
 
    # Sin división posible: devolver la clase más común
    if mejor is None:
        return max(set(y), key=y.count)
 
    _, f, umbral = mejor
    idx_izq = [i for i in range(len(X)) if X[i][f] <= umbral]
    idx_der = [i for i in range(len(X)) if X[i][f] > umbral]
    return {
        "f": f,
        "umbral": umbral,
        "izq": _construir([X[i] for i in idx_izq], [y[i] for i in idx_izq]),
        "der": _construir([X[i] for i in idx_der], [y[i] for i in idx_der]),
    }
 
 
# Se entrena UNA sola vez, cuando se importa este archivo (al iniciar Flask)
_ARBOL = _construir(_X_TRAIN, _Y_TRAIN)
 
 
def model2(R, G, B):
    """Recibe R, G, B (0-255) y retorna 'Rojo', 'Verde' o 'Azul'."""
    entrada = [float(R), float(G), float(B)]
    if _INVERTIR_SENSOR:
        entrada = [255 - max(0, min(255, v)) for v in entrada]
    nodo = _ARBOL
    while isinstance(nodo, dict):
        nodo = nodo["izq"] if entrada[nodo["f"]] <= nodo["umbral"] else nodo["der"]
    return _CLASES_NOMBRES.get(nodo, "Indefinido")
 
 
if __name__ == "__main__":
    # Prueba rápida solo si se ejecuta este archivo directamente
    print(model2(170, 100, 95))  # Rojo
