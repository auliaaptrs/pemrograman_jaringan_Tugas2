import socket

HOST = 'localhost'
PORT = 45000
TERMINATOR = '\r\n'

def send_command(connection, msg):
    connection.sendall((msg + TERMINATOR).encode('utf-8'))
    reply = connection.recv(1024)
    return reply.decode('utf-8')

def run_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((HOST, PORT))
            print("Connected to the time server.")

            while True:
                user_input = input("Enter Command (TIME / QUIT): ").strip().upper()
                if user_input in ['TIME', 'QUIT']:
                    server_reply = send_command(client_socket, user_input)
                    print(f"Server: {server_reply.strip()}")

                    if user_input == 'QUIT':
                        print("Connection closed.")
                        break
                else:
                    print("Please enter either TIME or QUIT.")
    except ConnectionRefusedError:
        print("Connection failed. Make sure the server is running.")
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    run_client()
