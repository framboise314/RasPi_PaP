#!/usr/bin/python3             
# Pour exécuter le prog. en ligne de commande
from time import sleep         # Importer la bibliothèque de gestion du temps 
import RPi.GPIO as GPIO        # Importer la bibliothèque de gestion des GPIO

STEP = 14                      # La commande de pas est reliée au GPIO 14
DIR = 15                       # La commande de direction est reliée au GPIO 15
vitesse = 0.0005

GPIO.setmode(GPIO.BCM)         # Paramétrage de la numérotation des GPIO en mode BCM
GPIO.setwarnings(False)        # Ne pas tenir comte des alertes
GPIO.setup(STEP, GPIO.OUT)     # GPIO STEP configuré en sortie
GPIO.setup(DIR, GPIO.OUT)      # GPIO DIR configuré en sortie

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



while True:
    # On travaille en 1/16 de pas soit 3200 micropas par tour
    for x in range(3200):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)

    sleep(1)

    GPIO.output(DIR, GPIO.LOW)
    for x in range(3200):
        GPIO.output(STEP, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(STEP, GPIO.LOW)
        sleep(vitesse)
        
    sleep(1)	
    tourne(1600, "CW", vitesse)
    sleep(0.5)
    tourne(1600, "CCW", vitesse)
    sleep(1)	
    tourne(800, "CW", vitesse)
    sleep(0.5)
    tourne(800, "CW", vitesse)
    sleep(0.5)
    tourne(800, "CW", vitesse)
    sleep(0.5)
    tourne(800, "CW", vitesse)
    
    sleep(1)
