# SpyTank

Ressources destinées à création d'un robot dans le cadre d'une formation liée à la programmation, l'électronique, les réseaux, l'impression 3D et le Web.

## Exercice de controle à distance via une interface web

1. Flashez le code arduino si ce n'est pas déjà fait. 
2. Dans le dossier **remote_robot_control** vous trouverez le fichier **browser_stream_setup.sh** donnez lui la permission d'execution et executez le pour lancer l'installation des dépendances.

    >   chmod u+x browser_stream_setup.sh

    >   sudo ./browser_stream_setup.sh

3. Ouvrez ensuite le fichier **robot_controller.py** qui permet de controler le robot depuis un joystick
3. A la ligne 72, tapez le code nécessaire pour faire avancer le robot en utilisant la position du joystick sur l'axe des x et y (*joystickX*,*joystickY*)
4. Pour tester, executez le fichier **robot_web_server.py** apres lui avoir donné les droits d'execution.

    >   chmod u+x robot_web_server.py

    >   sudo ./robot_web_server.py

    Tapez ensuite **l'adresse du raspberryPi** dans le navigateur (ou 127.0.0.1 si c'est en local) suivit du **port 98**.
    Exemple : 

    >   127.0.0.1:98

**NOTE :** le rayon du joystick est de 1, vous aurez donc des valeurs entre -1 et 1. Faites attention à laisser une zone "morte" pour le joystick afin d'éviter un comportement non voulu.
