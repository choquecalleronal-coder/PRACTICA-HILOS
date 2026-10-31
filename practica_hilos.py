
import threading
import queue
import time
import random

trabajos = queue.Queue()
resultados = {}
lock = threading.Lock()

# CESTO CARGA LOS 24 dDOCUMENTOS DE LA COLA XD
for doc_id in range(1, 25):
    tamaño = random.randint(1, 5)
    trabajos.put((doc_id, tamaño))

#  DE ACA PARA ABAJO SE EJECUTA PARA CADA TRABAJADOR 
def trabajador(nombre):
    cantidad = 0

    while True:
        try:
            # ACA OBTENDRA UN DOCUMENTO 
            doc_id, tamaño = trabajos.get_nowait()

        except queue.Empty:
            # TERMINA CUANDO YA NO HAY DOCUMENTOS 
            break

        # ESTO ES O ASE QUE SIMULA LOS DOCUMENTOS 
        print(f"{nombre} procesando documento {doc_id}")
        time.sleep(tamaño * 0.1)

        cantidad += 1

        #  MARCA  CUANDO EL  DOCUMENTO ESTA BIEN 
        trabajos.task_done()

    # ESTO PROTEJE A CADA REGISTRO QUE PASA 

    with lock:
        resultados[nombre] = cantidad

    print(f"{nombre} ha terminado.")

# CRAEAMOS LOS 4 HILOS ACA 
hilos = []

for i in range(1, 5):
    nombre = f"Trabajador-{i}"

    hilo = threading.Thread(
        target=trabajador,
        args=(nombre,)
    )

    hilos.append(hilo)
    hilo.start()
# ESTO TERMINA QUE CUANDO TERMINA TODOS LOS HILOS 
for hilo in hilos:
    hilo.join()

# MOSTRARE LOS SULTADOS
print("\n==FINAL XD==")

total = 0

for nombre, cantidad in sorted(resultados.items()):
    print(f"{nombre}: {cantidad} documentos")
    total += cantidad

print(f"\nTotal de documentos procesados: {total}")

if total == 24:
    print("VERIFICACION CORRECTA: 24 documentos procesados")
else:
    print("ERROR: cantidad de documentos incorrecta")
