from socket import socket, AF_INET, SOCK_STREAM

socket_client = socket(AF_INET, SOCK_STREAM)

client_info = ("127.0.0.1", 1212)

socket_client.bind(client_info)

# # 链接服务器
# socket_client.connect(("127.0.0.1", 1213))
# # 向服务器发起数据
# socket_client.send("xxx".encode("utf-8"))
# # 接收服务器返回的数据
# socket_client.recv(2048).decode("utf-8")

# 让套接字开启监听模式，设置成服务器
socket_client.listen(128)

while True:
    new_receive_socket, origin_addr = socket_client.accept()

    # 新套接字服务完成以后，关闭
    new_receive_socket.close()
socket_client.close()
