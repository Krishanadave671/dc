import socket
import threading
def broadcast(message, clients):
 for client in clients:
    try:
       client.send(message.encode('utf-8'))
    except:
    # Handle exceptions if a client connection is no longer valid
        clients.remove(client)
def handle_client(client_socket, clients):
 while True:
    try:
      data = client_socket.recv(1024)
      if not data:
         break
      message = data.decode('utf-8')
      print(f"Received message: {message}")
      broadcast(message, clients)
    except:
    # Handle exceptions if a client connection is no longer valid
      clients.remove(client_socket)
      break

def start_server():
 server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 server.bind(('0.0.0.0', 8888))
 server.listen(5)
 print("[*] Listening on 0.0.0.0:8888")
 clients = []
 while True:
   client_socket, addr = server.accept()
   print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
   clients.append(client_socket)
   client_handler = threading.Thread(target=handle_client,
   args=(client_socket, clients))
   client_handler.start()
if __name__ == "__main__":
 start_server() 