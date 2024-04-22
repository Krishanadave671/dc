import socket
import threading
def receive_messages(client_socket):
 while True:
    try:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"\nReceived broadcast: {message}")
    except:
         break



def send_message(client_socket):
    while True:
        message = input("Enter message to broadcast (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.send(message.encode('utf-8'))
        
        
if __name__ == "__main__":
 client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 client1.connect(('127.0.0.1', 8888))
 receive_thread1 = threading.Thread(target=receive_messages,args=(client1,))
 receive_thread1.start()
 send_thread1 = threading.Thread(target=send_message, args=(client1,))
 send_thread1.start()
 receive_thread1.join()
 send_thread1.join()
 client1.close() 
