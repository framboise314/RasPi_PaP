#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Version de Tom Jones pour Pyhthon  2
# D'après https://adventurist.me/posts/0136
# 2 modifs pour qu'il fonctionne
# Merci Frederic pour l'aide au déverminage

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 4533
BUFFER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr

az = 0.0
el = 0.0

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break

    print("received data:", data)

    if data == "p\n":
        print("pos query at az:{} el: {}", az, el);

        response = "{}\n{}\n".format(az, el)
        print("responing with: \n {}".format(response))
        conn.send(response)
    elif data.startswith("P "):
        # Modif 1 il ne faut qu'un espace dans la chaine data.split
        values = data.split(" ")
        print(values)
        az = float(values[1])
        el = float(values[2])

        print("moving to az:{} el: {}".format( az, el));

        # Modif 2 il faut 4 caractères quelconques suivis d'un Zero
        conn.send("12340")
    elif data == "q\n":
        print("close command, shutting down")
        conn.close()
        exit()
    else:
        print("unknown command, closing socket")
        conn.close()
        exit()
