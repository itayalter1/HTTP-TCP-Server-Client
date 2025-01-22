import socket
import os
import sys

def send_request(sock, server_ip, server_port, path):
    """
    Sends an HTTP request to the server.
    """
    try:
        request = f"GET {path} HTTP/1.1\r\nHost: {server_ip}:{server_port}\r\nConnection: close\r\n\r\n"
        sock.sendall(request.encode('utf-8'))
    except Exception as e:
        print(f"Error sending request: {e}")
        raise

def receive_response(sock):
    """
    Receives the server's response and returns headers, body, and status.
    """
    try:
        buffer = b""
        while b"\r\n\r\n" not in buffer:
            chunk = sock.recv(1024)
            if not chunk:
                break
            buffer += chunk

        headers, _, body = buffer.partition(b"\r\n\r\n")
        headers = headers.decode('utf-8').split("\r\n")
        status_line = headers[0]
        code = int(status_line.split(" ")[1])
        
        content_length = 0
        location = None
        for header in headers:
            if header.lower().startswith("content-length:"):
                content_length = int(header.split(":")[1].strip())
            elif header.lower().startswith("location:"):
                location = header.split(": ")[1].strip()

        while len(body) < content_length:
            chunk = sock.recv(1024)
            if not chunk:
                break
            body += chunk

        return code, headers, body[:content_length], location
    except Exception as e:
        print(f"Error receiving response: {e}")
        raise

def save_file(path, content):
    """
    Saves the content received from the server to an appropriate file.
    """
    try:
        file_name = os.path.basename(path) if path != "/" else "index.html"
        mode = 'wb' if file_name.endswith(('.png', '.jpg', '.jpeg', '.ico')) else 'w'
        content = content if mode == 'wb' else content.decode('utf-8')

        with open(file_name, mode) as f:
            f.write(content)
    except Exception as e:
        print(f"Error saving file: {e}")

def download_file(server_ip, server_port, path, recursive=False):
    """
    Downloads a file from the server.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_ip, server_port))

        send_request(sock, server_ip, server_port, path)
        code, headers, body, location = receive_response(sock)
        
        # Always print the status line
        print(headers[0])

        if code == 200:
            save_file(path, body)
        elif code == 404:
            pass  
        elif code == 301 and location:
            if not recursive:  # Prevent infinite redirection loops
                # Reconnect and perform the new request
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((server_ip, server_port))
                download_file(server_ip, server_port, location, True)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])

    while True:
        try:
            path = input()
            if path == "":
                path = '/'
            if not path:
                break
            
            download_file(server_ip, server_port, path)
        except EOFError:
            break