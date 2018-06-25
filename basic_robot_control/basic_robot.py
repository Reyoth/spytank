#!/usr/bin/env python3
                                                          
# Exemple simple pour controler le SpyTank
# Controls:
# 	z:	Avancer
#	q:	Tourner a gauche
#	d:	Tourner a droite
#	s:	Reculer
#	x:	Stop
#	t:	Augmenter la vitesse	(si implemente)
#	g:	Diminuer la vitesse		(si implemente)
#	w: 	Sortir du programme


from gopigo import *	#Contient les fonctions de base pour controler le SpyTank
import sys				#Contient la fonction exit pour sortir du programme

print ("Press:\n\tz: Pour avancer\n\tq: Pour Tourner a gauche\n\td: Pour Tourner a droite\n\ts: Pour Reculer\n\tx: Pour Stopper\n\tw: Pour sortir du programme\n")
while True:
	print ("Entrez une commande:")
	a=input()	# Lire l'entree clavier ( equivaut a input() en python3 )
	if a=='z':
		fwd()	# Avancer (forward)
	elif a=='q':
		left()	# Tourner a gauche
	elif a=='d':
		right()	# Tourner a droite
	elif a=='s':
		bwd()	# Reculer (backward)
	elif a=='x':
		stop()	# Stop
	elif a=='t':			
		increase_speed()	# Augmenter la vitesse
	elif a=='g':
		decrease_speed()	# Diminuer la vitesse
	elif a=='w':
		print ("Arret du programme")		# Exit
		sys.exit()
	else:
		print ("Mauvaise commande, reessayez")
	time.sleep(.1)
