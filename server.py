import socket
import os
import sys

# Initial settings
FILES_DIR = "files"
TIMEOUT = 1
BUFFER_SIZE = 4064

def read_file(file_path):
    """
    Read the content of a file based on its type (text or binary).
    """
    try:
        mode = 'rb' if file_path.endswith(('.jpg', '.jpeg', '.png', '.ico')) else 'r'
        with open(file_path, mode) as f:
            return f.read().encode() if mode == 'r' else f.read()
    except Exception as e:
        # print(f"Error reading file: {e}")
        return None

def handle_request(client_socket):
    """
    Handle a request from the client.
    """
    try:
        connection_alive = True
        buffer = ""

        while connection_alive:
            # Receive data from the client
            data = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            if not data:
                break

            buffer += data
            if '\r\n\r\n' in buffer:
                # Parse the header
                header, _, _ = buffer.partition('\r\n\r\n')
                lines = header.split('\r\n')
                request_line = lines[0]

                # Parse the request
                method, path, _ = request_line.split()
                connection_header = next((line for line in lines if line.lower().startswith("connection:")), "")
                connection_type = connection_header.split(": ")[1].strip().lower() if connection_header else "close"

                # if path not start with '/'
                if not path.startswith('/'):
                    path = '/' + path

                # Redirect
                if path == "/redirect":
                    response = (
                        "HTTP/1.1 301 Moved Permanently\r\n"
                        "Location: /result.html\r\n"
                        "Connection: close\r\n\r\n"
                    )
                    client_socket.sendall(response.encode('utf-8'))
                    connection_alive = False
                    break
                
                # Default to the homepage
                if path == "/":
                    path = "/index.html"

                # Check the file
                file_path = os.path.join(FILES_DIR, path.lstrip('/'))
                if os.path.exists(file_path) and not os.path.isdir(file_path):
                    content = read_file(file_path)
                    if content is None:
                        raise Exception("Error reading file content.")

                    # Send a 200 response
                    response = (
                        f"HTTP/1.1 200 OK\r\n"
                        f"Content-Length: {len(content)}\r\n"
                        f"Connection: {connection_type}\r\n\r\n"
                    )
                    client_socket.sendall(response.encode('utf-8'))
                    client_socket.sendall(content)
                else:
                    # Send a 404 response
                    response = (
                        "HTTP/1.1 404 Not Found\r\n"
                        "Connection: close\r\n"
                        "Content-Length: 0\r\n\r\n"
                    )
                    client_socket.sendall(response.encode('utf-8'))
                    connection_alive = False
                    break

                # Check if the connection should be closed
                if connection_type == "close":
                    connection_alive = False

            buffer = ""

    except Exception as e:
        pass
    finally:
        client_socket.close()


def start_server(port):
    """
    Initialize the server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', port))
    server_socket.listen(5)
    # print(f"Server started on port {port}...")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            # print(f"Connection from {client_address}")
            client_socket.settimeout(TIMEOUT)
            handle_request(client_socket)
    except KeyboardInterrupt:
        pass
        # print("Server is shutting down.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
