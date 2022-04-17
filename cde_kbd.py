#!/usr/bin/python3             
# Pour exécuter le prog. en ligne de commande  
from pynput import keyboard    # Bibliothèque de gestion clavier
from time import sleep         # Bibliothèque de gestion du temps
import RPi.GPIO as GPIO        # Bibliothèque de gestion des GPIO   

STEP = 14                      # La commande d'avance d'un pas est connectée à GPIO14  
DIR = 15                       # La commande du sens de rotation est connectée à GPIO15
vitesse = 0.0005               # Temps d'attente entre les pas : règle la vitesse

GPIO.setmode(GPIO.BCM)         # Utiliser la numérotation BCM pour les GPIO
GPIO.setwarnings(False)        # Ne pas afficher les alertes
GPIO.setup(STEP, GPIO.OUT)     # Paramétrer GPIO14 en sortie
GPIO.setup(DIR, GPIO.OUT)      # Paramétrer GPIO15 en sortie

# Tourner d'un nombre de pas en CW ou CCW à une vitesse donnée
def tourne(pas, sens, vitesse):
    # Sens de rotation
    if (sens == "CW"):
        GPIO.output(DIR, GPIO.HIGH)
    else:
        GPIO.output(DIR, GPIO.LOW)
    # Avancer du nombre de pas
    for x in range(pas):
        GPIO.output(14, GPIO.HIGH)
        sleep(vitesse)
        GPIO.output(14, GPIO.LOW)
        sleep(vitesse)
        
# Fonction appelée quand une touche est appuyée
def appui(key):
    try:
        print('Touche alphanumérique : {0} '.format(
            key.char))
    except AttributeError:
        print('Touche spéciale : {0}'.format(
            key))
        # Touche flèche gauche - Sens inverse des aiguilles d'une montre - 10 pas
        if (key == keyboard.Key.left):
            sens = "CCW"
            tourne(10,sens,vitesse) 
        # Touche flèche droite - Sens des aiguilles d'une montre - 10 pas
        elif (key == keyboard.Key.right):
            sens = "CW"
            tourne(10,sens,vitesse) 
        # Touche flèche haute - Sens inverse des aiguilles d'une montre - 100 pas
        elif (key == keyboard.Key.up):
            sens = "CCW"
            tourne(100,sens,vitesse) 
        # Touche flèche basse - Sens des aiguilles d'une montre - 100 pas
        elif (key == keyboard.Key.down):
            sens = "CW"
            tourne(100,sens,vitesse) 
        # Touche page haute - Sens inverse des aiguilles d'une montre - 800 pas = 1/4 de tour
        elif (key == keyboard.Key.page_up):
            sens = "CCW"
            tourne(800,sens,vitesse/10) 
        # Touche page basse - Sens des aiguilles d'une montre - 800 pas = 1/4 de tour
        elif (key == keyboard.Key.page_down):
            sens = "CW"
            tourne(800,sens,vitesse/10) 
           
# Fonction exécutée quand une touche est relachée
def relache(key):
    print('Key released: {0}'.format(
        key))
    # Si c'est la touche ESC on sort du programme
    if key == keyboard.Key.esc:
        # Stop listener
        print("Sortie du programme")
        GPIO.cleanup()
        return False

# Le listener collecte les événements et appelle les fonctions en callback
with keyboard.Listener(
        on_press = appui,
        on_release = relache) as listener:
    listener.join()
