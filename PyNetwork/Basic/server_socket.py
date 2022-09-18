import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to localhost on port 80
serversocket.bind(('localhost',80))

#become a server socket and listen a maxinum of 10 connections
serversocket.listen(10)
