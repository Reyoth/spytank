#!/usr/bin/env python
                                                          
# Exemple simple pour controler le SpyTank
# Controls:
# 	z:	Avancer
#	q:	Tourner à gauche
#	d:	Tourner à droite
#	s:	Reculer
#	x:	Stop
#	t:	Augmenter la vitesse	(si implémenté)
#	g:	Diminuer la vitesse		(si implémenté)
#	w: 	Sortir du programme


from gopigo import *	#Contient les fonctions de base pour controler le SpyTank
import sys				#Contient la fonction exit pour sortir du programme

print "Press:\n\tz: Pour avancer\n\tq: Pour Tourner à gauche\n\td: Pour Tourner à droite\n\ts: Pour Reculer\n\tx: Pour Stopper\n\tw: Pour sortir du programme\n"
while True:
	print "Entrez une commande:",
	a=raw_input()	# Lire l'entrée clavier ( équivaut à input() en python3 )
	if a=='z':
		fwd()	# Avancer (forward)
	elif a=='q':
		left()	# Tourner à gauche
	elif a=='d':
		right()	# Tourner à droite
	elif a=='s':
		bwd()	# Reculer (backward)
	elif a=='x':
		stop()	# Stop
	#elif a=='t':			
		#increase_speed()	# Augmenter la vitesse
	#elif a=='g':
		#decrease_speed()	# Diminuer la vitesse
	elif a=='w':
		print "Arret du programme"		# Exit
		sys.exit()
	else:
		print "Mauvaise commande, réessayez"
	time.sleep(.1)
