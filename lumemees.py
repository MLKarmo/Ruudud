import pygame
pygame.init()

screen=pygame.display.set_mode([300,300], pygame.RESIZABLE)
pygame.display.set_caption("Lumemees - Maria-Liis Karmo")
screen.fill([100, 150, 255])

#päikese kiired
pygame.draw.polygon(screen, [255, 255, 100], [[300,0],[-40,300],[40,300]], 0)
pygame.draw.polygon(screen, [255, 255, 100], [[300,0],[-60,300],[-140,300]], 0)
pygame.draw.polygon(screen, [255, 255, 100], [[300,0],[60,300],[140,300]], 0)

#päike
pygame.draw.circle(screen, [255,255,0], [280,20], 30,  0)

#pilved
pygame.draw.circle(screen, [200,255,255], [30,50], 20,  0)
pygame.draw.circle(screen, [200,255,255], [50,40], 20,  0)
pygame.draw.circle(screen, [200,255,255], [70,50], 20,  0)

pygame.draw.circle(screen, [200,255,255], [230,60], 25,  0)
pygame.draw.circle(screen, [200,255,255], [255,45], 25,  0)
pygame.draw.circle(screen, [200,255,255], [280,60], 25,  0)

pygame.draw.circle(screen, [200,255,255], [10,150], 30,  0)
pygame.draw.circle(screen, [200,255,255], [30,130], 30,  0)
pygame.draw.circle(screen, [200,255,255], [50,150], 30,  0)


#keha
pygame.draw.circle(screen, [255,255,255], [150,50], 40,  0)
pygame.draw.circle(screen, [255,255,255], [150,120], 50,  0)
pygame.draw.circle(screen, [255,255,255], [150,220], 70,  0)

#käed
pygame.draw.circle(screen, [255,255,255], [210,100], 35,  0)
pygame.draw.circle(screen, [255,255,255], [90,100], 35,  0)
pygame.draw.circle(screen, [255,255,255], [250,110], 27,  0)
pygame.draw.circle(screen, [255,255,255], [50,110], 27,  0)

pygame.draw.line(screen, [100,50,0], [260,100], [280,50], 7)
pygame.draw.line(screen, [100,50,0], [40,100], [20,50], 7)

pygame.draw.line(screen, [100,50,0], [280,50], [285,20], 7)
pygame.draw.line(screen, [100,50,0], [280,50], [270,20], 7)

pygame.draw.line(screen, [100,50,0], [20,50], [15,20], 7)
pygame.draw.line(screen, [100,50,0], [20,50], [30,20], 7)


#nägu #silmad
pygame.draw.circle(screen, [0,0,0], [127,50], 5,  0)
pygame.draw.circle(screen, [0,0,0], [172,50], 5,  0)
pygame.draw.line(screen, [0,0,0], [140,48], [120,44], 6)
pygame.draw.line(screen, [0,0,0], [180,45], [160,48], 6)

      #kulm
pygame.draw.line(screen, [0,0,0], [182,35], [155,45], 4)
pygame.draw.line(screen, [0,0,0], [153,42], [155,45], 4)

      #suu
pygame.draw.line(screen, [0,0,0], [145,68], [155,68], 5)
pygame.draw.line(screen, [0,0,0], [155,68], [175,60], 5)

      #põselohk
pygame.draw.line(screen, [0,0,0], [178,55], [180,65], 4)

      #nina
pygame.draw.polygon(screen, [255, 150, 50], [[145,50],[155,55],[140,70]], 0)

      #nööbid

pygame.draw.circle(screen, [0,0,0], [150,100], 6,  0)
pygame.draw.circle(screen, [0,0,0], [150,120], 7,  0)
pygame.draw.circle(screen, [0,0,0], [150,145], 8,  0)

#müts
pygame.draw.polygon(screen, [255, 100, 200], [[110,30],[190,30],[185,10],[115,10]], 0)
pygame.draw.line(screen, [255,150,200], [190,31], [90,31], 4)

#hari
pygame.draw.line(screen, [200,100,0], [250,30], [230,280], 7)
pygame.draw.polygon(screen, [255, 200, 100], [[220,10],[280,13],[235,90],[255,93]], 0)
pygame.draw.line(screen, [255, 100, 200], [240,70], [250,70], 7)

pygame.display.flip()  

while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()