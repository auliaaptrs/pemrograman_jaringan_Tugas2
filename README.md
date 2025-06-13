# Socket Time Server

A simple Python socket server-client program for sending the current server time. The server responds to TIME commands with the current timestamp and supports clean disconnection using the QUIT command. Multithreaded and designed for network programming practice.


## 🧩 Features

- Server runs on a specified port and listens for multiple client connections.
- Client can send:
  - `TIME` to get the current server time.
  - `QUIT` to disconnect gracefully.
- Server logs connection info and request handling using Python's `logging` module.

## 🏗️ Folder Structure
```
├── Client.py # Client-side script
└── Server.py # Server-side script
```

## 📝 Sample Input
```
Connected to the time server.
Enter Command (TIME / QUIT): TIME
Server: 13 06 2025 15:21:47
Enter Command (TIME / QUIT): QUIT
Server: 
Connection closed.
```

## 📄 Sample Output

```
2025-06-13 15:21:02,132 - Server running on port 45000
2025-06-13 15:21:05,820 - Client connected: ('127.0.0.1', 41940)
2025-06-13 15:21:11,405 - Request Received
2025-06-13 15:21:26,403 - Request Received
2025-06-13 15:21:30,380 - Request Received
2025-06-13 15:21:30,381 - Disconnecting ('127.0.0.1', 41940)
2025-06-13 15:21:44,408 - Client connected: ('127.0.0.1', 52750)
2025-06-13 15:21:47,993 - Request Received
2025-06-13 15:21:52,439 - Client connected: ('127.0.0.1', 45706)
2025-06-13 15:21:55,559 - Request Received
2025-06-13 15:21:59,788 - Request Received
2025-06-13 15:21:59,789 - Disconnecting ('127.0.0.1', 52750)
```

## ✅ Conclusion
This project demonstrates a basic yet effective implementation of a multithreaded socket server-client system in Python. The server is capable of handling multiple clients concurrently using threading, allowing it to maintain responsiveness even under several simultaneous connections.

An important feature included is the use of Python’s built-in logging module to clearly log each connection, disconnection, and request. Specifically, the message Request Received is logged every time the server successfully receives and processes a command (TIME or QUIT) from a client, making it easier to monitor server activity in real time.
