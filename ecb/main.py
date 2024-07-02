import socket
import threading

import rsa


public_key,private_key=rsa.newkeys(1024)
public_partner= None

choice = input("do you want to send(1)or do you want to receive(2)")



if choice == "1":
    senders=input("enter your ip address")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.252.162", 9999))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_partner=rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    receivers=input("enter your ip address")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((receivers,9999))


    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))

else:
    exit()

def receiving_messages(c):
    while True:
       message=input("")
       c.send(rsa.encrypt(message.encode(), public_partner))
       print("you:"+message)

def sending_messages(c):
    while True:
        print("partner:"+ rsa.decrypt(c.recv(1024),private_key).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()