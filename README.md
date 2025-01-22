כמובן, הנה הגרסה המעודכנת של ה-README:

---

# **HTTP-TCP-Server-Client**

## **Overview**
This project implements an HTTP server and client using the TCP protocol in Python. The server is capable of handling HTTP GET requests for static files (e.g., HTML, images) and supports features like redirects and error handling. The client component is designed to interact with the server, demonstrating persistent connections, request handling, and automatic reconnections.

The project serves as a demonstration of fundamental networking concepts, such as socket programming, HTTP request parsing, response generation, and managing TCP connections.

---

## **Components**

### **1. Server**
The server component listens for incoming HTTP GET requests and serves static files from a designated directory. It handles file requests, 404 errors for non-existent files, and 301 redirects. It also logs the request and response headers for debugging.

#### **Features:**
- **Listen on TCP port:** The server listens for incoming requests on a specific port, configurable via command line.
- **Serve static files:** The server serves various static files like HTML and images from a specified directory.
- **Handle HTTP GET requests:** It processes HTTP GET requests and serves the corresponding files.
- **Error handling:** Returns HTTP status codes such as:
  - `200 OK` for successful requests
  - `404 Not Found` for missing files
  - `301 Moved Permanently` for redirects
- **Logging:** The server logs both request and response headers to the console to help with debugging.

#### **How it works:**
The server waits for HTTP GET requests from clients, fetches the corresponding file from the filesystem, and sends back an appropriate HTTP response. It also handles edge cases like non-existent files by sending an HTTP 404 response or handling redirects via 301.

---

### **2. Client**
The client component is designed to communicate with the server by sending HTTP GET requests. It demonstrates persistent connection handling (via `Connection: keep-alive`) and the ability to automatically reconnect in case of a lost connection.

#### **Features:**
- **Send HTTP GET requests:** The client sends requests to a server at a specified IP address and port.
- **Persistent connections:** It supports the `Connection: keep-alive` header to maintain the connection for multiple requests, improving efficiency.
- **Automatic reconnection:** If the connection is unexpectedly closed, the client automatically attempts to reconnect and resend the last request.
- **Error handling:** The client can handle situations such as connection errors and unexpected disconnects, ensuring a robust interaction with the server.

## **How to Clone the Project from GitHub**

To clone the project from GitHub, follow these steps:

1. Make sure you have `git` installed on your machine. You can check by running the following command in your terminal:

    ```bash
    git --version
    ```

    If you don’t have `git` installed, install it following [this guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

2. Clone the repository by running the following command:

    ```bash
    git clone https://github.com/itayalter1/HTTP-TCP-Server-Client.git
    ```

3. Navigate to the project directory:

    ```bash
    cd HTTP-TCP-Server-Client
    ```

You now have the project on your local machine and can run it as described above.

---
---

## **How to Run the Project**

### **1. Server**

To run the server, execute the following command in your terminal:

```bash
python3 server.py <server-port>
```

This starts the HTTP server on the specified TCP port. The server will begin listening for incoming requests and will respond with static files or error codes as defined.

- Replace `<server-port>` with the desired port number (e.g., `8080`).

### **2. Client**

To start the client and connect to the server, use the following command:

```bash
python3 client.py <server-ip> <server-port>
```

This command allows the client to connect to the server using the provided IP and port, sending HTTP GET requests to fetch static files.

- Replace `<server-ip>` with the server's IP address (e.g., `127.0.0.1` for localhost).
- Replace `<server-port>` with the server's port (e.g., `8080`).

---



## **File Structure**

- `server.py`: Implements the HTTP server that listens for incoming requests and serves static files.
- `client.py`: Implements the client that sends HTTP GET requests and handles server responses.
- `files/`: A folder containing sample files (HTML, images) served by the server.

---

## **Technologies Used**

- **Language:** Python
- **Protocols:** HTTP (using TCP sockets)
- **Networking:** Socket programming, TCP connections, persistent connections

---

## **Future Improvements**

- **HTTPS Support:** Adding support for secure connections (TLS/SSL).
- **Request Parsing:** Improve parsing of complex HTTP requests.
- **Client Enhancements:** Implement the ability to send POST requests and handle other HTTP methods.
- **Logging:** Enhance logging to capture request/response details in log files.

---

## **Contact**

For questions or suggestions, feel free to reach out:

- **Email:** itayalter1@gmail.com  
- **GitHub:** [itayalter1](https://github.com/itayalter1)

---

