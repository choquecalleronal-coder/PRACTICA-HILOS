# Práctica de Hilos en Python

## ¿Qué hace el programa?
El programa procesa 24 documentos utilizando 4 hilos. Cada trabajador retira documentos de una cola compartida y registra cuántos procesó. Se utiliza `Lock` para proteger los resultados.

## Captura 1
![Captura 1](CAPTURAS/captura_1.png)

**Resultado:** 6, 5, 7 y 6 documentos.

**Interpretación:** Los cuatro trabajadores procesaron los 24 documentos correctamente.

## Captura 2
![Captura 2](CAPTURAS/captura_2.png)

**Resultado:** 6, 6, 6 y 6 documentos.

**Interpretación:** Los documentos se distribuyeron de manera equilibrada entre los cuatro hilos.

## Captura 3
![Captura 3](CAPTURAS/captura_3.png)

**Resultado:** 6, 6, 4 y 8 documentos.

**Interpretación:** La cantidad procesada varió según la disponibilidad de cada trabajador.

## Captura 4
![Captura 4](CAPTURAS/captura_4.png)

**Resultado:** 5, 5, 7 y 7 documentos.

**Interpretación:** La distribución cambió nuevamente, pero se completaron los 24 documentos.

## Preguntas

**1. ¿Por qué usar queue.Queue?**

Porque permite distribuir documentos de forma segura entre varios hilos.

**2. ¿Qué protege Lock?**

Protege los resultados compartidos y evita posibles condiciones de carrera.

**3. ¿Qué cambiaría para guardar archivos reales?**

Agregaría funciones para guardar archivos, controlar errores y evitar sobrescribir documentos.

## Conclusión
En las cuatro ejecuciones comprobé que los hilos trabajan de forma concurrente y procesan correctamente los 24 documentos.