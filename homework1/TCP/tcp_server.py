import socket
import sys


def tcp_server(port, buffer_size=1024, mode="streaming"):
    # Create the TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)

    print("TCP Server is listening on port", port, "in", mode, "mode")

    # Wait for a client connection
    connection, client_address = server_socket.accept()
    print("Connection established with", client_address)

    total_bytes_received = 0
    total_messages_received = 0

    # Receive data from the client
    while True:
        data = connection.recv(buffer_size)
        if not data:
            break
        total_bytes_received += len(data)
        total_messages_received += 1

        # If in stop-and-wait mode, send an acknowledgment after each message.
        if mode == "stop_and_wait":
            connection.send(b'ACK')

    # Close the connection
    connection.close()

    # Output received data statistics
    print(f"TCP Server: {total_messages_received} messages received.")
    print(f"TCP Server: {total_bytes_received} bytes received.")


if __name__ == "__main__":
    port = 5000  # default port
    mode = "streaming"  # default mode
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    if len(sys.argv) >= 3:
        mode = sys.argv[2]
    tcp_server(port, mode=mode)
