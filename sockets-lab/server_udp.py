import socket

HOST = '0.0.0.0'
PORT = 65432

try:
    
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[SERVER] Listening on {HOST}:{PORT} (UDP)")

        while True:
            try:
                # Primanje podataka od klijenta
                data, addr = s.recvfrom(1024)  # Očekujemo da klijent šalje podatke
                print(f"[SERVER] Received from {addr}: {data.decode()}")
                
                # Slanje odgovora nazad klijentu s fiksnom porukom
                response = "Primio sam poruku"
                s.sendto(response.encode(), addr)
                #print(f"[SERVER] Sent to {addr}: {response}")
               
            except Exception as e:
                print(f"[SERVER ERROR] An error occurred while receiving/sending data: {e}")
except Exception as e:
    print(f"[SERVER ERROR] Could not start the server: {e}")
