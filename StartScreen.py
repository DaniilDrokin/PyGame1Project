import pygame


def start_screen():
    pygame.init()
    size = 1360, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Начальный экран')

    pygame.font.init()
    font_1 = pygame.font.Font('data/Molot.ttf', 40)
    font_2 = pygame.font.Font('data/Days.ttf', 40)
    font_3 = pygame.font.Font('data/Rex Bold.ttf', 70)
    text_1 = font_1.render(f'НУ, ПОГОДИ!', True, (196, 30, 58))
    text_2 = font_2.render(f'электроника', True, (0, 0, 0))
    text_3 = font_3.render(f'А|Д', True, (0, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((196, 195, 195))
        pygame.draw.rect(screen, (112, 112, 112), (0, 0, 1360, 800), 10)
        pygame.draw.rect(screen, (218, 236, 253), (340, 120, 680, 550), 0)
        pygame.draw.rect(screen, (112, 112, 112), (340, 120, 680, 550), 5)

        pygame.draw.ellipse(screen, (196, 30, 58), (130, 450, 80, 80), 0)
        pygame.draw.ellipse(screen, (112, 112, 112), (130, 450, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(145, 450), (125, 470), (90, 420)], 0)

        pygame.draw.ellipse(screen, (196, 30, 58), (130, 650, 80, 80), 0)
        pygame.draw.ellipse(screen, (112, 112, 112), (130, 650, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(145, 730), (125, 710), (90, 760)], 0)

        pygame.draw.ellipse(screen, (196, 30, 58), (1150, 450, 80, 80), 0)
        pygame.draw.ellipse(screen, (112, 112, 112), (1150, 450, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(1215, 450), (1235, 470), (1270, 420)], 0)

        pygame.draw.ellipse(screen, (196, 30, 58), (1150, 650, 80, 80), 0)
        pygame.draw.ellipse(screen, (112, 112, 112), (1150, 650, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(1215, 730), (1235, 710), (1270, 760)], 0)

        pygame.draw.ellipse(screen, (0, 0, 0), (90, 50, 120, 120), 5)
        pygame.draw.circle(screen, (0, 0, 0), (92, 110), 10, 0)
        pygame.draw.circle(screen, (196, 195, 195), (92, 110), 15, 5)

        screen.blit(text_1, (560, 75))
        screen.blit(text_2, (545, 656))
        screen.blit(text_3, (110, 80))
        image = pygame.image.load('data/wolf.png')
        screen.blit(image, (1050 ,20))

        pygame.draw.lines(screen, (0, 0, 0), False, [(555, 105), (325, 105), (325, 685), (540, 685)], 5)
        pygame.draw.lines(screen, (0, 0, 0), False, [(795, 105), (1035, 105), (1035, 685), (825, 685)], 5)

        pygame.display.flip()


if __name__ == '__main__':
    start_screen()