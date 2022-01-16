import pygame
import os


def registration():
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

    def draw():
        screen.blit(text_1, (50, 125))
        screen.blit(text_2, (50, 25))
        pygame.draw.rect(screen, (0, 0, 0), (50, 75, 500, 50), 5)
        pygame.draw.rect(screen, (0, 0, 0), (50, 175, 500, 50), 5)

    class Line(pygame.sprite.Sprite):
        def __init__(self, y, name):
            super().__init__(lines_sprites)
            self.name = name
            self.image = pygame.Surface((500, 50), pygame.SRCALPHA, 32)
            pygame.draw.rect(self.image, (112, 112, 112), (0, 0, 500, 50), 0)
            self.rect = pygame.Rect(50, y, 500, 50)

        def return_name(self):
            return self.name

        def update(self, *args):
            pass

    pygame.init()
    size = 600, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Регистрация')

    running = True

    font = pygame.font.Font('data/Days.ttf', 40)
    text_1 = font.render(f'пароль:', True, (0, 0, 0))
    text_2 = font.render(f'логин:', True, (0, 0, 0))

    all_write = False

    lines_sprites = pygame.sprite.Group()
    coordinates = [75, 175]
    lines = ['login', 'password']

    for i in range(2):
        y = coordinates[i]
        name = lines[i]
        Line(y, name)
    while running:
        screen.fill((196, 195, 195))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and all_write:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in lines_sprites:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        print(button.return_name())
        draw()
        lines_sprites.draw(screen)
        lines_sprites.update()
        pygame.display.flip()


if __name__ == '__main__':
    registration()
