# TCP File Server 🌐

## Overview 🎯
A robust TCP server implementation that handles file requests via HTTP/1.1 protocol. This server enables clients to retrieve files from a specified directory with support for persistent connections and comprehensive error handling.

## Key Features ⭐
- **HTTP/1.1 File Retrieval** 📂
  - GET request support
  - Binary & text file handling
  - Path flexibility (relative/absolute)
  
- **Smart Connection Management** 🔌
  - Keep-alive support
  - Auto-timeout (1 second) ⏱️
  - Connection state tracking

- **Error Handling** 🚨
  - 404 Not Found responses
  - 301 Redirects with location headers
  - Timeout management

## Quick Start 🚀

### Server Setup 💻
```bash
python3 tcp_server.py [PORT]
```

### Client Usage 🖥️
```bash
python3 tcp_client.py [SERVER_IP] [PORT]
```

## run Methods 🔄

### Clone Poject
```bash
git clone https://github.com/itayalter1/HTTP-TCP-Server-Client.git
```
```bash
cd DNS-Resolver-and-Server
```

### 1. Python Client 🐍
```bash
# Request a file from subdirectory
after tun the client anter this:

a/1.jpg

# The file will be downloaded to your current directory
you can run all files that append in File.
```

### 2. Web Browser 🌐
Enter in your browser's address bar:
```
http://serverHost:serverPort/filename

# Examples:
http://localhost:8080/image.jpg
http://localhost:8080/docs/readme.txt
```

## Example Interactions how it's work 🔄

### 1. Basic File Request 📧
```http
# Request
GET / HTTP/1.1
Connection: close

# Response
HTTP/1.1 200 OK
Connection: close
Content-Length: 11

hello world
```

### 2. Redirect Handling 🔄
```http
# Client Request
GET /a/picture.jpg HTTP/1.1
Host: localhost:8080
Connection: keep-alive

# Server Redirect Response
HTTP/1.1 301 Moved Permanently
Location: /b/picture.jpg
Connection: keep-alive

# Final Response
HTTP/1.1 200 OK
Content-Length: 12345
Content-Type: image/jpeg
Connection: keep-alive

[Image Data...]
```

### 3. Error Cases ❌
- File Not Found: Returns 404 error
- Redirect Needed: Returns 301 with location header

## Technical Features 🛠️

### Connection Handling 🔌
- **Persistent Connections**
  - Keep-alive support
  - Configurable timeouts
  - Auto-cleanup

### File Operations 📁
- Text file serving
- Binary file support (.jpg, .ico)
- Directory traversal protection
- Automatic file type detection

### Network Analysis 🔍
- Wireshark compatibility
- Connection tracking
- Packet inspection

## the file 📂
the file that the code use it is files.
if you want to change this delte the file add append new with name files.

### tree 🖼️
```bash
.
├── a
│   ├── 1.jpg
│   ├── 2.jpg
│   ├── 3.jpg
│   ├── 4.jpg
│   ├── 5.jpg
│   ├── 6.jpg
│   └── b
│       ├── 1.jpg
│       ├── 2.jpg
│       ├── 3.jpg
│       ├── 4.jpg
│       ├── 5.jpg
│       ├── 6.jpg
│       └── ref.html
├── c
│   ├── Footube.html
│   ├── footube.css
│   ├── footube.js
│   └── img
│       ├── 1.jpg
│       ├── 2.jpg
│       ├── 3.jpg
│       ├── 4.jpg
│       ├── 5.jpg
│       └── 6.jpg
├── favicon.ico
├── index.html
└── result.html
```

## Requirements 📋
- Python 3.x
- Basic networking tools
- Wireshark (for debugging)

## Testing 🧪
1. Start server
2. Run client requests
3. Monitor Wireshark output
4. Verify file transfers

## Best Practices 💡
- Keep connections short
- Handle binary files properly
- Monitor timeouts
- Validate paths
- Use appropriate file extensions
- Check server responses for redirects
