import math
from datetime import datetime
import pygame

pygame.init()
pygame.mixer.init()
screen_size = (600, 400)
screen = pygame.display.set_mode(screen_size)
screen.fill((0, 0, 0))
clock = pygame.time.Clock()



while True:
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12
    vineboom = pygame.mixer.Sound('vineboom.mp3')
    vergil = pygame.mixer.Sound('vergil.mp3')
    sixseven = pygame.mixer.Sound('sixseven.mp3')
    
    if second == 0 or second == 30:
        if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.play(vineboom)
    elif hour == 2 and minute == 59 and second == 48:
        pygame.mixer.Sound.play(vergil)
    elif hour == 6 and minute == 6 and second == 54:
         pygame.mixer.Sound.play(sixseven)
    

    if second >= 30:
        screen.fill((0, 0, 0))
        lasse = pygame.image.load('lasse.png')
        screen.blit(lasse, (20, 20))
    else:
        screen.fill((0, 0, 0))
        andreas = pygame.image.load('andreas.png')
        screen.blit(andreas, (20, 20))

    for linehour in range(0, 360, 30):
        length = 150
        startpoint = (300,200)
        end_posx = startpoint[0] + length * math.cos(math.radians(linehour))
        end_posy = startpoint[1] + length * math.sin(math.radians(linehour))
        endpointhour = (end_posx, end_posy)
        pygame.draw.line(screen, (200, 200, 200), startpoint, endpointhour, 1)

    for lineminute in range(0, 360, 6):
        length = 125
        startpoint = (300,200)
        end_posx = startpoint[0] + length * math.cos(math.radians(lineminute))
        end_posy = startpoint[1] + length * math.sin(math.radians(lineminute))
        endpointminute = (end_posx, end_posy)
        pygame.draw.line(screen, (200, 200, 200), startpoint, endpointminute, 1)

    pygame.draw.circle(screen, (0, 0, 0), (300, 200), 115)

    sec_len = 110
    min_len = 90
    hr_len = 60

    endpointsecondhandx = startpoint[0] + sec_len * math.cos(math.radians(second * 6 - 90))
    endpointsecondhandy = startpoint[1] + sec_len * math.sin(math.radians(second * 6 - 90))
    
    endpointminutehandx = startpoint[0] + min_len * math.cos(math.radians(minute * 6 - 90))
    endpointminutehandy = startpoint[1] + min_len * math.sin(math.radians(minute * 6 - 90))
    
    endpointhrhandx = startpoint[0] + hr_len * math.cos(math.radians((hour * 30) + (minute * 0.5) - 90))
    endpointhrhandy = startpoint[1] + hr_len * math.sin(math.radians((hour * 30) + (minute * 0.5) - 90))
    
    endpointsecondhand = (endpointsecondhandx, endpointsecondhandy)
    endpointminutehand = (endpointminutehandx, endpointminutehandy)
    endpointhrhand = (endpointhrhandx, endpointhrhandy)

    font = pygame.font.SysFont(None, 36)
    text = font.render(f'{hour}:{minute}', True, (255, 255, 255))
    text0 = font.render(f'{hour}:0{minute}', True, (255, 255, 255))
    
    if minute > 9:
        screen.blit(text, (267,222))
    else:
        screen.blit(text0, (267,222))

    pygame.draw.line(screen, (255, 0, 0), startpoint, endpointsecondhand, 1)
    pygame.draw.line(screen, (255, 255, 255), startpoint, endpointminutehand, 2)
    pygame.draw.line(screen, (255, 0, 255), startpoint, endpointhrhand, 3)

    pygame.display.flip()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()