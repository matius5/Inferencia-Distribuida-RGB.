# Explicación del algoritmo CART con índice Gini

## Entradas y etiquetas

El archivo `codigo/model2.py` incluye **15 muestras RGB**: 5 etiquetadas rojo (1), 5 verde (2) y 5 azul (3). Esos datos están definidos directamente en Python; no se carga un conjunto externo.

## Construcción del árbol

La función `_gini(etiquetas)` calcula `1 − suma(p_clase²)`. La función `_construir(X, y)` evalúa cada uno de los tres canales R, G, B y propone umbrales entre valores consecutivos distintos. Elige la división con menor Gini ponderado y repite el procedimiento recursivamente. Cuando las muestras de un nodo pertenecen a una misma clase, devuelve esa clase.

El árbol `_ARBOL` se construye una vez al importar el módulo. `model2(R,G,B)` recorre el árbol según los umbrales almacenados y devuelve el nombre de la clase.

## Particularidad importante del código

El modelo se entrena con los valores RGB originales, pero `model2` **invierte la entrada** porque `_INVERTIR_SENSOR = True`:

```python
entrada = [255 - max(0, min(255, v)) for v in entrada]
```

Esta transformación puede ser necesaria para algún sensor específico, pero **no está justificada por el código aportado**. Debe comprobarse en el montaje físico. Para los valores `(170,100,95)`, el programa original imprime **`Verde`**, aunque su comentario dice `Rojo`. No se alteró el original para ocultar esta discrepancia.

## Limitaciones

No hay separación explícita entre datos de entrenamiento y evaluación. No se puede afirmar una exactitud determinada ni que el modelo esté validado fuera de las muestras seleccionadas.

[Volver al README](../README.md)
