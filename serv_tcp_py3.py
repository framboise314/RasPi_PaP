#!/usr/bin/env python3

# Serveur TCP pour python 3
# Récupère Azimut et Elevation depuis le programme Gpredict sur Raspberry Pi

# Source : https://adventurist.me/posts/0136
# © Tom Jones 2012
# Merci Frédéric Audon pour le déverminage et la solution au plantage !



import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 4533
BUFFER_SIZE = 100

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ("Connexion à l'adresse : ", addr)

az = 0.0
el = 0.0

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data:
        break

    print("Données reçues : ", data)

    if data == b'p\n':
        print("Position reçue az:{} el:{}", az, el);

        response = "{}\n{}\n".format(az, el)
        print("Répondre avec : \n {}".format(response))
        conn.send(str.encode(response))
    elif data.startswith(b'P '):
        values = data.split(b' ')
        print(values)
        az = float(values[1])
        el = float(values[2])

        print("Déplacement vers az:{} el: {}".format( az, el));

        conn.send(b'12340')
    elif data ==b'q\n':
        print("Commande d'arrêt, fermeture du programme")
        conn.close()
        exit()
    else:
        print("Commande inconnue, fermeture du socket")
        conn.close()
        exit()

