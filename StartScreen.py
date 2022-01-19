import pygame
import os
from Game import game
from Records import records


def start_screen():
    def load_image(name, colorkey=None):
        fullname = os.path.join("data", name)
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    class Button(pygame.sprite.Sprite):
        def __init__(self, x, y, radius, name):
            super().__init__(button_sprites)
            self.name = name
            self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
            pygame.draw.circle(self.image, (196, 30, 58), (radius, radius), radius)
            self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and args[0].button == 1\
                    and self.tip(args[0].pos):
                button_sound.play()
                return self.name

        def give_name(self):
            return self.name

        def tip(self, pos):
            return self.rect.collidepoint(pos)

    def draw():
        pygame.draw.rect(screen, (112, 112, 112), (0, 0, 1360, 800), 10)
        pygame.draw.rect(screen, (218, 236, 253), (340, 120, 680, 550), 0)
        pygame.draw.rect(screen, (112, 112, 112), (340, 120, 680, 550), 5)

        pygame.draw.ellipse(screen, (112, 112, 112), (130, 450, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(145, 450), (125, 470), (90, 420)], 0)

        pygame.draw.ellipse(screen, (112, 112, 112), (130, 650, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(145, 730), (125, 710), (90, 760)], 0)

        pygame.draw.ellipse(screen, (112, 112, 112), (1150, 450, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(1215, 450), (1235, 470), (1270, 420)], 0)

        pygame.draw.ellipse(screen, (112, 112, 112), (1150, 650, 80, 80), 8)
        pygame.draw.polygon(screen, (0, 0, 0), [(1215, 730), (1235, 710), (1270, 760)], 0)

        pygame.draw.ellipse(screen, (0, 0, 0), (90, 50, 120, 120), 5)
        pygame.draw.circle(screen, (0, 0, 0), (92, 110), 10, 0)
        pygame.draw.circle(screen, (196, 195, 195), (92, 110), 15, 5)

        pygame.draw.lines(screen, (0, 0, 0), False, [(555, 105), (325, 105), (325, 685), (540, 685)], 5)
        pygame.draw.lines(screen, (0, 0, 0), False, [(795, 105), (1035, 105), (1035, 685), (825, 685)], 5)

        screen.blit(text_1, (560, 75))
        screen.blit(text_2, (545, 656))
        screen.blit(text_3, (110, 80))
        screen.blit(load_image('wolf.png'), (1050, 20))

    pygame.init()
    size = 1360, 800
    button_sprites = pygame.sprite.Group()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Начальный экран')

    font_1 = pygame.font.Font('data/Molot.ttf', 40)
    font_2 = pygame.font.Font('data/Days.ttf', 40)
    font_3 = pygame.font.Font('data/Rex Bold.ttf', 70)
    font_4 = pygame.font.Font('data/Rex Bold.ttf', 50)
    text_1 = font_1.render(f'НУ, ПОГОДИ!', True, (196, 30, 58))
    text_2 = font_2.render(f'электроника', True, (0, 0, 0))
    text_3 = font_3.render(f'А|Д', True, (0, 0, 0))

    button_sound = pygame.mixer.Sound("data/button.wav")

    running = True
    radius = 40
    buttons = ['Settings', 'Play', 'Records', 'History']
    coordinates = [(130, 450), (130, 650), (1150, 450), (1150, 650)]
    for i in range(4):
        x, y = coordinates[i]
        name = buttons[i]
        Button(x, y, radius, name)
    while running:
        screen.fill((196, 195, 195))

        for button in button_sprites:
            if button.tip(pygame.mouse.get_pos()):
                if button.give_name() == 'Play':
                    text_4 = font_4.render(f'Play', True, (0, 0, 0))
                    screen.blit(text_4, (button.rect.x, button.rect.y - 45))
                elif button.give_name() == 'History':
                    text_4 = font_4.render(f'History', True, (0, 0, 0))
                    screen.blit(text_4, (button.rect.x - 30, button.rect.y - 45))
                elif button.give_name() == 'Settings':
                    text_4 = font_4.render(f'Settings', True, (0, 0, 0))
                    screen.blit(text_4, (button.rect.x - 40, button.rect.y + 85))
                elif button.give_name() == 'Records':
                    text_4 = font_4.render(f'Records', True, (0, 0, 0))
                    screen.blit(text_4, (button.rect.x - 40, button.rect.y + 85))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in button_sprites:
                    but = button.update(event)
                    if but == 'Play':
                        game()
                    elif but == 'Records':
                        records()
                    elif but == 'History':
                        pass
                    elif but == 'Settings':
                        pass
        button_sprites.draw(screen)
        draw()
        pygame.display.flip()


if __name__ == '__main__':
    start_screen()
