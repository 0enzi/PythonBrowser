# Hi, Elvis here.
# Here' s a simple web browser in python with HTTP 1.0
import socket
print("Enter the hostname of site you want to visit.")
url = input('https://')
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect((f'{url}', 80))
cmd = f'GET http://{url} HTTP/1.0\r\n\r\n'.encode()
my_socket.send(cmd)

while True:
    data = my_socket.recv(2048) #nice
    if len(data) < 1:
        break
    print(data.decode(), end="")

print("\n😂Copy and paste the html you receive and load it up to see the site \n\n")
my_socket.close()