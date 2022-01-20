import pygame


def rules():
    pygame.init()
    size = 800, 450
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Как начать играть')

    font = pygame.font.Font('data/Rex Bold.ttf', 50)
    font_1 = pygame.font.Font('data/Rex Bold.ttf', 35)
    text = font.render(f'ПРАВИЛА ИГРЫ', True, (196, 30, 58))
    text_1 = font_1.render(f'Четыре курицы, сидящие на насестах,', True, (0, 0, 0))
    text_2 = font_1.render(f'несут яйца, скатывающиеся вниз по четырём лоткам.', True, (0, 0, 0))
    text_3 = font_1.render(f'Управляя волком, требуется наловить как можно', True, (0, 0, 0))
    text_6 = font_1.render(f'больше яиц в корзину.', True, (0, 0, 0))
    text_7 = font_1.render(f'Темп игры постепенно ускоряется.', True, (0, 0, 0))
    text_9 = font_1.render(f'В случае падения яйца на землю у игрока', True, (0, 0, 0))
    text_10 = font_1.render(f'уменьшается запас жизней (всего есть 3 жизни).', True, (0, 0, 0))
    text_11 = font_1.render(f'При потере всех жизней игра прекращается.', True, (0, 0, 0))

    running = True

    while running:
        screen.fill((196, 195, 195))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        screen.blit(text, (240, 25))

        screen.blit(text_1, (100, 85))
        screen.blit(text_2, (15, 120))
        screen.blit(text_3, (50, 160))
        screen.blit(text_6, (230, 200))
        screen.blit(text_7, (150, 240))
        screen.blit(text_9, (80, 270))
        screen.blit(text_10, (50, 310))
        screen.blit(text_11, (80, 350))

        pygame.display.flip()


if __name__ == '__main__':
    rules()