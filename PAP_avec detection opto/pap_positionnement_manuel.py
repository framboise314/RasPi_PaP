#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Pour exécuter le prog. en ligne de commande
# Programme de démo prise de zéro moteur Pas à pas
# Puis saisie d'une valeur qui positionne le moteur PAP
# La valeur saisie n'est pas vérifiée

from time import sleep         # Importer la bibliothèque de gestion du temps 
import RPi.GPIO as GPIO        # Importer la bibliothèque de gestion des GPIO
import random                  # Importer la bibliothèque pour générer un nombre aléatoire

STEP = 14                      # La commande de pas est reliée au GPIO 14
DIR = 15                       # La commande de direction est reliée au GPIO 15
ZERO = 4
vitesse = 0.0005

# GPIO.LOW = CCW
# GPIO.HIGH = CW

GPIO.setmode(GPIO.BCM)         # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(False)        # Ne pas tenir comte des alertes
GPIO.setup(STEP, GPIO.OUT)     # GPIO STEP configuré en sortie
GPIO.setup(DIR, GPIO.OUT)      # GPIO DIR configuré en sortie

GPIO.setup(ZERO, GPIO.IN)

# Tourner d'un nombre de pas en CW ou CCW
def tourne(pas, sens, vitesse):
    # Sens de rotation
    if (sens == "CW"):
        GPIO.output(DIR, GPIO.HIGH)
    else:
        GPIO.output(DIR, GPIO.LOW)
    # Avancer du nombre de pas
    for x in range(pas):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)
        
while 1:        
       
    # Si le Zéro est détecté le moteur est en position
    # On va le décaler car pas sur que le zero soit exact
    # Si l'entrée est à 1 : palette détectée
    if GPIO.input(ZERO)== 1:
        print("Zero détecté entrée à 1")
        sleep(0.5)

    if GPIO.input(ZERO)== 1:
        print("Zéro détecté - Décaler la position CW")
        GPIO.output(DIR, GPIO.HIGH)
        for i in range(100):
            print("oups")
            GPIO.output(STEP, GPIO.HIGH)
            sleep(vitesse*5)
            GPIO.output(STEP, GPIO.LOW)
            sleep(vitesse*5)
            
    # Ramener le moteur vers le zéro
    # vitesse rapide - Arrêt sur le zéro
    GPIO.output(DIR, GPIO.LOW)
    while GPIO.input(ZERO) == 0:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)
    print("Ramené à Zéro")
    sleep(0.5)

    # Faire avancer un peu le moteur pour libérer le capteur
    GPIO.output(DIR, GPIO.HIGH)
    for i in range(50):
        #print("Avance doucement")
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse*5)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse*5)


    # Revenir vers la capteur à petite vitesse
    GPIO.output(DIR, GPIO.LOW)
    while GPIO.input(ZERO) == 0:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse*50)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse*50)
    print("Ramené à Zéro - Final")
    sleep(1)

    ### LE pointeur est sur ZERO ###

    # Saisir la destination

    azimut = input("Entrez l'azimut à atteindre : ")
    # Sens horaire
    GPIO.output(DIR, GPIO.HIGH)
    for x in range(round(float(azimut) * 8.888888)):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse*5)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse*5)
    sleep(5)    


