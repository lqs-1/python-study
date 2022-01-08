from socket import socket, AF_INET, SOCK_DGRAM

socket_client = socket(AF_INET, SOCK_DGRAM)
socket_client.bind(("127.0.0.1", 1212))

socket_client.sendto("xxxx".encode("utf-8"), ("127.0.0.1", 1213))

receive_list = socket_client.recvfrom(2048)
data = receive_list[0]
send_addr = receive_list[1]

socket_client.close()