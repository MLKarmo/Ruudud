import pygame
pygame.init()

#Ekraani suurus ja programmi nimi
screen=pygame.display.set_mode([640,480], pygame.RESIZABLE)
pygame.display.set_caption("༼;´༎ຶ ۝ ༎ຶ༽")

# Tausta pilt
bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])

# mõõk ja mõõga asukoht
mook = pygame.image.load("Mõõk.png")
mook = pygame.transform.scale(mook, [180, 180])
screen.blit(mook,[450,50])
# kook
cake = pygame.image.load("cake.png")
cake = pygame.transform.scale(cake, [180, 100])
screen.blit(cake,[350,200])

# Mingi mees ja ta asukoht ekraanil
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [290, 350])
screen.blit(seller,[100,100])

# Chati pilt
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [230, 160])
screen.blit(chat,[300,100])

# Minu nimi, font ja kirja suurus
font = pygame.font.Font(None, 25)
text = font.render("Tere, olen Maria-Liis", True, [255,255,255])
screen.blit(text, [330,150])

#Viki logo
vikk = pygame.image.load("VIKK.png")
vikk = pygame.transform.scale(vikk, [200, 40])
screen.blit(vikk,[10,10])

# Uuendab programmi ekraani   
pygame.display.flip()  

# Paneb mängu koheselt kinni peale risti vajutamist
while True:
    if pygame.event.wait().type == pygame.QUIT:
        break
pygame.quit()