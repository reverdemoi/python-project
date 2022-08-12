import socketserver, socket, zlib, sys

##### USING SOCKET #####

# HOST, PORT = "127.0.0.1", 1234

# def decompress(data):
#   return zlib.decompress(data)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
#   try:
#     soc.bind((HOST, PORT))
#     soc.listen()
#     conn, addr = soc.accept()

#     with conn:
#       while True:
#         print("----- NEW CONNECTION -----")

#         session_id = addr[1]
#         print(f"Connected to {addr}, current session ID: {session_id}")

#         data = conn.recv(1024) # Data is compressed
#         print(data)
#         conn.sendall(decompress(data)) # Sending back decompressed data
#         conn.close()

#         conn, addr = soc.accept()
  
#   except socket.error as message:
#     print(f"Error error {message}")
#     sys.exit()

##### USING SOCKETSERVER #####

class MyTCPHandler(socketserver.BaseRequestHandler):
  def handle(self):
    self.data = self.request.recv(1024).strip()

    # Logs what's received from client
    print("{} wrote:".format(self.client_address[0]))
    print(self.data)

    # Decompressing the data
    decompressed = zlib.decompress(self.data)

    # Logs reply to client from server
    print("Replied: {}".format(decompressed))

    # Sends actual reply
    self.request.sendall(decompressed)

if __name__ == "__main__":
  HOST, PORT = "127.0.0.1", 1234

  with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
    server.serve_forever()