# client.py
import socket
def send_data(target_ip, target_port, data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_ip, target_port))
    # Send integers as a comma-separated string
    data_str = ','.join(map(str, data))
    client.send(data_str.encode('utf-8'))
    client.close()

if __name__ == "__main__":
 print("Enter 4 integers to send to the server:")
 integers_to_send = []
 for i in range(1, 5):
    num = int(input(f"{i}: "))
    integers_to_send.append(num)
 # Simulate sending 4 integers from the client
 send_data('127.0.0.1', 8888, integers_to_send)