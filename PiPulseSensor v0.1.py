#!/usr/bin/env python

# Script inspiré de simpletest.py - https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008
# Adapté pour GPIO Zero v1.2 - http://gpiozero.readthedocs.org/en/v1.2.0/recipes.html

from gpiozero import MCP3008
import time

print('Lecture MCP3008 en cours, pressez Ctrl-C pour quitter...')
# Formattage du tableau de présentation des données lues sur les huit canaux.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Boucle principale.
while True:
    # Lecture des huit canaux dans une liste.
    values = [0]*8
    for i in range(8):
        # Lecture des données d'un canal spécifique (0-7) dont l'initialisation est implicite.
        spi = MCP3008(i)
        # Arrondi des données lues.
        values[i] = int(round(spi.value*100))
    # Affichage des données lues.
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # Pause.
    time.sleep(0.5)
