import time
import threading

def consulta(nombre, tiempo):
    print("Iniciando", nombre)
    time.sleep(tiempo)
    print("Finalizó", nombre)

hilos = []
inicio = time.time()

for i in range(3):
    t = threading.Thread(target=consulta, args=(f"Consulta {i+1}", i+2))
    t.start()
    hilos.append(t)

for h in hilos:
    h.join()

print("Tiempo total:", time.time() - inicio)

