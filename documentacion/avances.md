# Bitácora de avances — inferencia distribuida RGB

| Actividad | Estado | Evidencia |
| --- | --- | --- |
| Algoritmo CART con Gini escrito en Python puro | Código disponible | [model2.py](../codigo/model2.py) |
| Conjunto de 15 muestras RGB, 3 clases | Incorporado en código | [algoritmo.md](algoritmo.md) |
| Prueba local del modelo | Ejecutada con el código entregado el 15/10/2026 | [prueba_basica.py](../pruebas/prueba_basica.py) |
| Confirmar inversión del sensor | Pendiente con dispositivo real | Sin evidencia física |
| Código de comunicación distribuida | Pendiente de incorporar | Sin archivo aportado |
| Fotos y capturas de la clase | Pendiente de adjuntar | Sin evidencia subida |
| Métricas con datos independientes | Pendiente de validar | No hay resultados medidos |

## Hallazgo de la prueba local

Con `_INVERTIR_SENSOR = True`, el ejemplo `model2(170, 100, 95)` devuelve **Verde**, no **Rojo** como dice el comentario al final del archivo original. La diferencia se conserva y documenta para su revisión.

## Registro futuro

- **Fecha:**
- **Hardware conectado:**
- **Programa ejecutado:**
- **Datos RGB recibidos:**
- **Clase predicha:**
- **Resultado esperado / observación:**
- **Fotografía o video:**
