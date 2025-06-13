import socket
import threading
import time
import logging
from datetime import datetime

SERVER_PORT = 45000
SERVER_HOST = '0.0.0.0'
MAX_BUFFER = 1024
LINE_ENDING = b'\r\n'

class ClientHandler(threading.Thread):
    def __init__(self, conn, addr):
        threading.Thread.__init__(self)
        self.conn = conn
        self.addr = addr
        self.is_active = True

    def run(self):
        logging.warning(f"Client connected: {self.addr}")
        recv_buffer = b''

        try:
            while self.is_active:
                received = self.conn.recv(MAX_BUFFER)
                if not received:
                    break
                recv_buffer += received

                while LINE_ENDING in recv_buffer:
                    command, recv_buffer = recv_buffer.split(LINE_ENDING, 1)
                    command_str = command.decode('utf-8').strip()

                    logging.info("Request Received")

                    if command_str.upper() == 'TIME':
                        timestamp = time.strftime("%d %m %Y %H:%M:%S")
                        reply = f"{timestamp}\r\n"
                        self.conn.sendall(reply.encode('utf-8'))

                    elif command_str.upper() == 'QUIT':
                        self.is_active = False
                        break

        except Exception as error:
            logging.warning(f"Error handling {self.addr}: {error}")
        finally:
            logging.warning(f"Disconnecting {self.addr}")
            self.conn.close()


class TimeServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        self.sock.bind((SERVER_HOST, SERVER_PORT))
        self.sock.listen(5)
        logging.warning(f"Server running on port {SERVER_PORT}")

        try:
            while True:
                new_conn, new_addr = self.sock.accept()
                client_thread = ClientHandler(new_conn, new_addr)
                client_thread.start()
                self.clients.append(client_thread)
        except KeyboardInterrupt:
            logging.warning("Stopping server...")
        finally:
            self.sock.close()


def run_server():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    main_server = TimeServer()
    main_server.start()
    main_server.join()

if __name__ == "__main__":
    run_server()
