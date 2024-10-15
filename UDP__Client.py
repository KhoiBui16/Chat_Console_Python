import socket

def start_client():
    """Start UDP client and connect to the server"""
    server_ip = input("Enter server IP: ")
    server_port = int(input("Enter server PORT: "))

    # Create UDP socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (server_ip, server_port)

    try:
        while True:
            # Input message from user
            message = input("Enter your message (press '!q' to exit): ")

            if message.lower() == '!q':
                print("Disconnected")
                client_socket.sendto(message.encode('utf-8'), server_address)
                break

            # Send the message to the server
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Receive response from the server
            response, _ = client_socket.recvfrom(1024)
            print(f"From server: {response.decode('utf-8')}")

    finally:
        # Close socket when the client exits
        client_socket.close()

if __name__ == "__main__":
    start_client()
