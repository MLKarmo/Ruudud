import pygame
import sys

laius = 640
pikkus = 480

ruut = int(input("Ruudu suurus?: "))
vahe = int(input("Vahede suurus?: "))

roosa = (250, 180, 180)
kollane = [255, 255, 150]

pygame.init()

screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")

screen.fill(kollane)


ruudud_x = laius // (ruut + vahe)
ruudud_y = pikkus // (ruut + vahe)

# Calculate actual vahe (remaining space after squares)
laiuse_vahe = (laius - (ruudud_x * ruut)) // (ruudud_x - 1)
pikkuse_vahe = (pikkus - (ruudud_y * ruut)) // (ruudud_y - 1)

for i in range(ruudud_x):
    for j in range(ruudud_y):
        x = i * (ruut + laiuse_vahe)
        y = j * (ruut + pikkuse_vahe)
        pygame.draw.rect(screen, roosa, (x, y, ruut, ruut))

pygame.display.flip()
    
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()
