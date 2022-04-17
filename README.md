# RasPi_PaP
Pilot a Nema stepper motor with Raspberry Pi and A4988

J’ai une idée qui me trotte dans la tête depuis un moment, c’est de réaliser une « poursuite » de satellite pilotée par un Raspberry Pi. L’idée c’est de faire tourner le programme Gpredict sur le Pi, de récupérer les coordonnées et de piloter un duo de moteurs pas à pas pour diriger une (petite) antenne vers un satellite. La première étape est de piloter un moteur pas à pas à partir du Raspberry Pi.
En direct le 16 avril. Je présente cette application du Raspberry Pi vers 18h30 (H de Paris). Vous pouvez gagner mon livre « Raspberry Pi 4 » offert par les Editions ENI.
Commander un moteur pas à pas avec le Raspberry Pi

Le synoptique du montage est le suivant :

<img width="545" alt="synoptique16" src="https://user-images.githubusercontent.com/5877909/163719797-aa13a5a8-a6f6-441a-8def-273120271fd3.png">

Le Raspberry Pi envoie au driver A4988 une direction (sens horaire CW, ou anti horaire CCW) et sur un autre GPIO on sort des impulsions qui provoqueront chacune une avance d’un pas.

Le nombre de pas par tour est déterminé par les entrées MS1 à MS3. Par d&f&ut le moteur PaP fait un tour en 200 pas (de 1,8°) mais on peut modifier le nombre de micro-pas fournis par le driver pour affiner le déplacement.

![montage_PAP_08](https://user-images.githubusercontent.com/5877909/163719925-b08f7e9b-307a-4a12-9b6e-be425ad017df.png)

Le montage tel qu’il sera réalisé est présenté ici avec Fritzing. Le module supporte une alimentation de puissance pour le moteur comprise entre 8 et 35 volts. Ici j’ai opté pour une alimentation 12 volts, suffisante pour fournir le courant souhaité au moteur.

![test_PAP2](https://user-images.githubusercontent.com/5877909/163719944-b5a93c63-0f2c-4a34-9736-716973f25c93.jpg)

Le câblage une fois réalisé donne ceci. J’ai muni le moteur PaP d’une flèche en impression 3D pour vérifier que ses déplacements sont conformes à ce qui est attendu

![A4988_Stepper_03](https://user-images.githubusercontent.com/5877909/163720018-f6cddb94-05ff-4904-b6aa-3eb13ff36ddd.jpg)

Ici le module A4988 avant la pose du radiateur sur le circuit de commande. La potentiomètre sert à régler le courant qui circule dans les bobines du moteur car le moteur est alimenté en courant, pas en tension. C’est le module qui va limiter le courant envoyé dans les bobines du moteur. Ne pas oublier que tant que le montage est alimenté le moteur est maintenu en position par le courant qui circule dans les bobines… Donc… il chauffe. Vous pouvez consulter la notice du A4988 en cliquant sur ce lien : https://www.framboise314.fr/wp-content/uploads/2022/04/A4988.pdf

Liens :
Article du blog : https://www.framboise314.fr/piloter-un-moteur-pas-a-pas-avec-le-raspberry-pi-et-un-driver-a4988/

Vidéo youtube : https://youtu.be/YyUdxzrAYzA


