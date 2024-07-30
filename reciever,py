import socket
from datetime import datetime

# Initialize the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the IP and port to listen on
ip_address = "127.0.0.1"
port_no = 2525
complete_address = (ip_address, port_no)
s.bind(complete_address)

# File to store received messages
log_file = "received_messages.log"

print("Hey, I am listening ....")
while True:   # Infinite loop
    Data = s.recvfrom(100)
    message = Data[0].decode('ascii')
    sender_address = Data[1]
    
    print(message)
    
    # Log the received message with timestamp
    with open(log_file, "a") as file:
        file.write(f"{datetime.now()} - Received from {sender_address[0]}: {message}\n")