import socket

def telnet_client(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            while True:
                # Read input from the user
                message = input("Enter message (or 'exit' to quit): ")

                if message.lower() == 'exit':
                    print("Closing connection...")
                    break

                # Send the message to the server
                client_socket.sendall(message.encode('ascii'))

                # Receive the response from the server
                response = client_socket.recv(1024).decode('ascii')
                print(f"Server response: {response}")

    except ConnectionRefusedError:
        print("Unable to connect to the server. Please check the host and port.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    HOST = "localhost"  # Replace with the server's IP address
    PORT = 8085         # Replace with the server's port number

    telnet_client(HOST, PORT)
