import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

print("client.py working")
try:
    print("entered try block")
    while True:
        print("Entered while loop")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            operation = s.send(input("Please enter your operation:\n").encode())
            n1 = s.send(input("Please enter the first number:\n").encode())
            n2 = s.send(input("Please enter the second number:\n").encode())
            data = s.recv(16)
            # ask_user = input("You want to quit or continue? Press 'q' or 'c'")
except socket.error as err:
    print("Creating socket error: ", err)
except KeyboardInterrupt:
    print(end="")

# use while loop
# get by 16 byte
# server and client files should be runned as separated two containers.
