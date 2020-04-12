import pygame, sys, random

pygame.init()

window_size = (1000, 600)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Cure Corona")

pygame.mixer.music.load(r'C:\Users\Asus\Desktop\Cure Corona\sound\invincible-ncs.mp3')
pygame.mixer.music.play(-1)

doc_image = (pygame.transform.scale(pygame.image.load(r'C:\Users\Asus\Desktop\Cure Corona\img\doc.png').convert_alpha(), (50, 50)))
in_image = (pygame.transform.scale(pygame.image.load(r'C:\Users\Asus\Desktop\Cure Corona\img\infected.png').convert_alpha(), (50, 50)))

bg = (pygame.transform.scale(pygame.image.load(r'C:\Users\Asus\Desktop\Cure Corona\img\city.jpg').convert_alpha(), (1000, 600)))

screen = pygame.display.get_surface()
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (153, 51, 51)
blue = (0, 0, 255)

doc_x = 600
doc_y = 400

powerup_x = random.randint(1, 600)
powerup_y = random.randint(1, 400)

infected1_x = random.randint(1, 600)
infected1_y = random.randint(1, 400)

score = 0
infected = 10
infected_nochange = 10
infected_toadd = 2
saved = 0
wave = 1
x1 = 50

myfont = pygame.font.SysFont("Cosmic Sans MS", 30)

screen.blit(bg, (0, 0))
pygame.display.update()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        doc_x -= 5
        
    if pressed[pygame.K_RIGHT]:
        doc_x += 5
        
    if pressed[pygame.K_UP]:
        doc_y -= 5
        
    if pressed[pygame.K_DOWN]:
        doc_y += 5
        

    screen.blit(bg, (0, 0))

    if doc_x > 1000 or doc_y > 600 or doc_x <0 or doc_y <0:
        screen.fill(white)
        screen.blit(textsurface5, (400, 250))
        pygame.quit()
        sys.exit()

    if doc_x in range(infected1_x-50, infected1_x+50) and doc_y in range(infected1_y-50, infected1_y+50):
        infected1_x = random.randint(1, 600)
        infected1_y = random.randint(1, 400)
        saved += 1
        infected -=1
    
    pygame.draw.rect(screen, black, [infected1_x, infected1_y, 50, 50])
    pygame.draw.rect(screen, black, [doc_x, doc_y, 50, 50])
    textsurface = myfont.render("Saved : " + str(saved),False, green)
    textsurface2 = myfont.render("Infected : " + str(infected),False, green)
    textsurface3 = myfont.render("Wave " + str(wave), False, blue)
    textsurface4 = myfont.render("Press X for Boost", False, red)
    textsurface5 = myfont.render("Game Over", False, red)
    textsurface6 = myfont.render("Score : " + str(score),False, black)
    if infected == (infected_nochange/2)-3:
        x1 = 50
    if infected == infected_nochange/2:
        screen.blit(textsurface4, (400, 250))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_x]:
            x1 = 100
            
    if infected == 0:
        saved = 0
        infected = 10*infected_toadd
        infected_toadd += 1
        wave += 1
        score += 10
        infected_nochange = infected
    screen.blit(textsurface, (5, 10))
    screen.blit(textsurface2, (115, 10))
    screen.blit(textsurface3, (450, 10))
    screen.blit(textsurface6, (900, 10))
    window.blit(doc_image, (doc_x, doc_y))
    window.blit(in_image, (infected1_x, infected1_y))
    pygame.display.update()
    clock.tick(x1*wave)
        
