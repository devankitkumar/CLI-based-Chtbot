import socket
from datetime import datetime

# Initialize the socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the target IP and port
target_ip = "127.0.0.1"  # localhost 
target_port = 2525
target_address = (target_ip, target_port)

# File to store sent messages
log_file = "sent_messages.log"

condition = True
while condition:
    message = input("Please enter your message: ")
    message_encrypted = message.encode('ascii')
    
    # Send the message
    s.sendto(message_encrypted, target_address)
    print("Your message is sent .....")
    
    # Log the message with timestamp
    with open(log_file, "a") as file:
        file.write(f"{datetime.now()} - Sent: {message}\n")
    
    permission = input("Do you want to send another message? (Y/N): ")

    if permission.lower() == "n":
        condition = False