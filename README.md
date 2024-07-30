# CLI-based-Chtbot
FIrst project of Uplfalirs Training
Here's a detailed README file for your GitHub repository:

---

# **CLI Chat Application using Python Sockets**

## **Project Overview**

This project is a **Command Line Interface (CLI) Chat Application** that demonstrates real-time communication using **Python's socket programming**. It allows two users to exchange messages over a network. The chat messages are logged with **accurate timestamps**, ensuring data integrity and easy retrieval. This project is an excellent introduction to **network programming** and **real-time communication protocols** for beginners.

## **Project Structure**

The project consists of two main components:
1. **Receiver Side Code**
2. **Sender Side Code**

### **1. Receiver Side Code**

The receiver side script initializes a UDP socket to listen for incoming messages. It logs all received messages with timestamps.

```python
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
```

### **2. Sender Side Code**

The sender side script initializes a UDP socket to send messages to the receiver. It prompts the user to enter a message, sends it to the receiver, and logs the sent messages with timestamps.

```python
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
```

## **How to Run the Project**

### **Prerequisites**

- **Python 3.x** installed on your machine.
- Basic understanding of **Python programming**.

### **Steps to Run**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the URL of your GitHub repository.

2. **Navigate to the Project Directory**:
   ```bash
   cd <project-directory>
   ```

3. **Running the Receiver Side Code**:
   - Open a terminal and navigate to the directory containing the `receiver.py` script.
   - Run the script:
     ```bash
     python receiver.py
     ```
   - The receiver will start listening for incoming messages.

4. **Running the Sender Side Code**:
   - Open another terminal and navigate to the directory containing the `sender.py` script.
   - Run the script:
     ```bash
     python sender.py
     ```
   - You can now send messages to the receiver.

### **How It Works**

- The **Receiver Side** script creates a socket and binds it to the specified IP address and port. It listens for incoming messages and logs them with the sender's address and a timestamp.
- The **Sender Side** script creates a socket and sends user-input messages to the receiver's IP address and port. It logs the sent messages with a timestamp.

## **Result and Output**

- Messages sent from the sender are displayed on the receiver's terminal and logged in the `received_messages.log` file.
- Messages entered by the sender are logged in the `sent_messages.log` file with timestamps.

## **Contributing**

Feel free to fork this repository and contribute by submitting a pull request. Whether it's bug fixes, new features, or documentation improvements, all contributions are welcome!

## **License**
This project is open-source and available under the [MIT License](LICENSE).
