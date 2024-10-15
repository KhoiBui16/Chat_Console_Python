import socket

def start_server():
    """Start UDP server"""
    server_ip = input("Enter server IP (for example, 0.0.0.0 for all interfaces): ")
    server_port = int(input("Enter server PORT: "))

    # Create UDP socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the IP address and port
    server_socket.bind((server_ip, server_port))

    print(f"Server started at {server_ip}:{server_port}")

    while True:
        try:
            # Receive data from the client
            message, client_address = server_socket.recvfrom(1024)
            decoded_message = message.decode('utf-8')
            print(f"Received from {client_address}: {decoded_message}")

            # If the client sends '!q', the server will disconnect and exit
            if decoded_message == '!q':
                print(f"Client {client_address} requested to disconnect. Server will shut down.")
                break

            # Send a response back to the client
            response = f"{decoded_message}"
            server_socket.sendto(response.encode('utf-8'), client_address)

        except KeyboardInterrupt:
            print("\nServer is shutting down...")
            break

    # Close the socket when the server shuts down
    server_socket.close()

if __name__ == "__main__":
    start_server()
    

