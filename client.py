import socket, zlib, sys

HOST, PORT = "127.0.0.1", 1234

def compress(data):
  return zlib.compress(bytes(data, "utf-8"), -1)

data = " ".join(sys.argv[1:])
compressed_data = compress(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect((HOST, PORT))
    soc.sendall(compress(data))

    received = soc.recv(1024).strip()

print("Sent:    {}".format(compressed_data))
print("Received {}".format(received))