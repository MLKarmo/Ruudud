import pygame
import sys

# ekraani suurus
laius = 640
pikkus = 480

# Ruutude ja vahede suurus
ruut = 20
vahe = 10

#Värvid
roosa = (250, 180, 180)
kollane = [255, 255, 150]

#Käivitab mängu
pygame.init()

# Ekraani suurus ja programmi nimi
screen = pygame.display.set_mode([laius, pikkus])
pygame.display.set_caption("Harjutamine")

# Ekraani värv
screen.fill(kollane)

# Arvutab kui palju ruute mahub ekraanile
ruudud_x = laius // (ruut + vahe)
ruudud_y = pikkus // (ruut + vahe)

# Näitab kui palju üle jääb
laiuse_vahe = (laius - (ruudud_x * ruut)) // (ruudud_x - 1)
pikkuse_vahe = (pikkus - (ruudud_y * ruut)) // (ruudud_y - 1)

for i in range(ruudud_x):
    for j in range(ruudud_y):
        x = i * (ruut + laiuse_vahe)
        y = j * (ruut + pikkuse_vahe)
        pygame.draw.rect(screen, roosa, (x, y, ruut, ruut))

pygame.display.flip()

#Suleb ristist vajatuses koheselt
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()

# Github:
# https://github.com/MLKarmo/Ulesanded/blob/main/ruudud.py
