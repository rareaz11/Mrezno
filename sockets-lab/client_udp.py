import socket

HOST = '127.0.0.1'  
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        print("[CLIENT] Pokrenut UDP klijent.")
        while True:
            message = input("Unesi poruku (ili 'exit'): ")
            if message.lower() == 'exit':
                print("[CLIENT] Izlazak iz klijenta.")
                break

            # Slanje poruke serveru
            print(f"[CLIENT] Šaljem poruku: {message}")
            s.sendto(message.encode(), (HOST, PORT))

            # Primanje odgovora
            data, server = s.recvfrom(1024)
            print(f"[CLIENT] Primljeno od servera: {data.decode()}")

except Exception as e:
    print(f"[CLIENT ERROR] Došlo je do greške: {e}")
