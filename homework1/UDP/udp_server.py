import socket
import sys

def udp_server(port, buffer_size=1024, mode="streaming"):
    # Create the UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', port))

    print("UDP Server is listening on port", port, "in", mode, "mode")

    total_bytes_received = 0
    total_messages_received = 0

    while True:
        data, client_address = server_socket.recvfrom(buffer_size)
        if not data:
            break
        total_bytes_received += len(data)
        total_messages_received += 1

        # If in stop-and-wait mode, send an acknowledgment after each message.
        if mode == "stop_and_wait":
            server_socket.sendto(b'ACK', client_address)
        print(f"UDP Server: {total_messages_received} messages received.")
        print(f"UDP Server: {total_bytes_received} bytes received.")

if __name__ == "__main__":
    port = 5000  # default port
    mode = "streaming"  # default mode
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    if len(sys.argv) >= 3:
        mode = sys.argv[2]
    udp_server(port, mode=mode)
