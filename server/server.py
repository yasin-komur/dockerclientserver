import socket

HOST = '127.0.0.1'
PORT = 65432

print("server.py working")


def operations(n1, n2, operation):
    n1, n2 = int(n1), int(n2)

    if operation == "add":
        return n1 + n2
    elif operation == "subtract":
        return n1 - n2
    elif operation == "multiply":
        return n1 * n2
    elif operation == "divide":
        return n1 / n2
    else:
        return "We are not that good!"


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                op = ""
                while True:
                    data = conn.recv(16)
                    op += data.decode() + " "
                    if not data:
                        break
                    conn.sendall(data)
                print(operations(op.split()[1], op.split()[2], op.split()[0]))
except socket.error as err:
    print("Socket creating error: ", err)
except IndexError:
    print("Index problem occured.")
except KeyboardInterrupt:
    print(end="")

