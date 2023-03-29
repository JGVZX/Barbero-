import threading

MAX_Cant_SILLAS = 5


clientes_en_sala = threading.Semaphore(0)

cliente_atendido = threading.Semaphore(0)

sillas_disponibles = threading.Semaphore(MAX_Cant_SILLAS)


def barbero():
    while True:

        clientes_en_sala.acquire()
        
        sillas_disponibles.release()
        
        print("El barbero está cortando un cliente Ahora...")
        cliente_atendido.release()


def cliente(id_cliente):
    while True:

        sillas_disponibles.acquire()
        
        print(f"El cliente {id_cliente} se ha sentado en una silla de la sala de espera")
        clientes_en_sala.release()
        
        cliente_atendido.acquire()
        
        print(f"El cliente {id_cliente} ha sido recortado por el barbero")

threading.Thread(target=barbero).start()

for i in range(10):
    threading.Thread(target=cliente, args=(i+1,)).start()