import socket
import time
import sys

# Function for TCP client streaming
def tcp_client_streaming(server_ip, port, data_size, buffer_size=1024):
    # Create the TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    total_bytes_sent = 0
    total_messages_sent = 0
    data = b'A' * buffer_size  # Simulate data block to send

    start_time = time.time()

    # Send data continuously (streaming)
    while total_bytes_sent < data_size:
        client_socket.send(data)
        total_bytes_sent += len(data)
        total_messages_sent += 1

    end_time = time.time()
    client_socket.close()

    # Output transmission statistics
    transmission_time = end_time - start_time
    print(f"TCP Client (Streaming): {transmission_time:.2f} seconds")
    print(f"TCP Client (Streaming): {total_messages_sent} messages sent.")
    print(f"TCP Client (Streaming): {total_bytes_sent} bytes sent.")


# Function for TCP client Stop-and-Wait (for comparison)
def tcp_client_stop_and_wait(server_ip, port, data_size, buffer_size=1024):
    # Create the TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    total_bytes_sent = 0
    total_messages_sent = 0
    data = b'A' * buffer_size  # Simulate data block to send

    start_time = time.time()

    # Send data and wait for acknowledgment after each packet (stop-and-wait)
    while total_bytes_sent < data_size:
        client_socket.send(data)
        total_bytes_sent += len(data)
        total_messages_sent += 1

        # Wait for acknowledgment
        client_socket.recv(buffer_size)

    end_time = time.time()
    client_socket.close()

    # Output transmission statistics
    transmission_time = end_time - start_time
    print(f"TCP Client (Stop-and-Wait): {transmission_time:.2f} seconds")
    print(f"TCP Client (Stop-and-Wait): {total_messages_sent} messages sent.")
    print(f"TCP Client (Stop-and-Wait): {total_bytes_sent} bytes sent.")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python tcp_client.py <server_ip> <port> <data_size>")
        sys.exit(1)

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    data_size = int(sys.argv[3])  # In bytes, either 500 MB or 1 GB

    # Choose between streaming or stop-and-wait
    mode = sys.argv[4] if len(sys.argv) > 4 else "streaming"
    if mode == "streaming":
        tcp_client_streaming(server_ip, port, data_size)
    elif mode == "stop_and_wait":
        tcp_client_stop_and_wait(server_ip, port, data_size)
    else:
        print("Invalid mode. Use 'streaming' or 'stop_and_wait'.")
