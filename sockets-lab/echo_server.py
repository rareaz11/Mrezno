import socket
import datetime 
from local_machine_info import print_machine_info 


HOST = '0.0.0.0'  # Slušaj na svim dostupnim mrežnim interfejsima
PORT = 65432

try:
    # Kreiraj UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[SERVER] Listening on {HOST}:{PORT} (UDP)")

        while True:
            try:
                # Primanje podataka od klijenta
                data, addr = s.recvfrom(1024)  # Očekujemo da klijent šalje podatke
                message = data.decode()
                print(f"[SERVER] Received from {addr}: {message}")
                print(datetime.datetime.now())
                print_machine_info()

               
                if "antonio_zelic" in message.lower():
                    response = "Unos nije podržan"
                else:
                    response = "Primio sam poruku"

                # Slanje odgovora nazad klijentu
                s.sendto(response.encode(), addr)
                print(f"[SERVER] Sent to {addr}: {response}")
               
            except Exception as e:
                print(f"[SERVER ERROR] An error occurred while receiving/sending data: {e}")
except Exception as e:
    print(f"[SERVER ERROR] Could not start the server: {e}")
