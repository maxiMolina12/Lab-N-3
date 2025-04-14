import socket

ip = input("Ingrese la dirección IP a escanear: ")
for puerto in range (1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock. settimeout (1)
    result = sock. connect_ex((ip, puerto))
    if result == 0:
        print("Puerto Abierto: " + str(puerto))
        sock. close()
    else:
        print("Puerto Cerrado: " + str(puerto) )