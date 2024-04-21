import socket
import threading
def handle_client(client_socket):
   data = client_socket.recv(1024)
   if not data:
      return
   # Split the received string into individual integers
   received_data = list(map(int, data.decode('utf-8').split(',')))
   print(f"Received integers: {received_data}")
   print(f"Sum of integers: {sum(received_data)}")
   client_socket.close()
   
   
   
def start_server():
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind(('0.0.0.0', 8888))
   server.listen(5)
   print("[*] Listening on 0.0.0.0:8888")
   while True:
      client_socket, addr = server.accept()
      print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
      client_handler = threading.Thread(target=handle_client,
      args=(client_socket,))
      client_handler.start()

if __name__ == "__main__":
 server_thread = threading.Thread(target=start_server)
 server_thread.start()