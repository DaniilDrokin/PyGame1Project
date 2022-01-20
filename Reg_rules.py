import pygame


def reg_rules():
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Как начать играть')

    font = pygame.font.Font('data/Rex Bold.ttf', 50)
    font_1 = pygame.font.Font('data/Rex Bold.ttf', 35)
    text = font.render(f'ЗДРАВСТВУЙ, Дорогой Пользователь!', True, (196, 30, 58))
    text_1 = font_1.render(f'Перед тем как вы сможете начать играть в', True, (0, 0, 0))
    text_2 = font_1.render(f'EGG_catcher, вам нужно будет зарегистрироваться,', True, (0, 0, 0))
    text_3 = font_1.render(f'чтобы ваши лучшие результаты сохранялись.', True, (0, 0, 0))
    text_6 = font_1.render(f'Для этого введите логин и пароль маленькими', True, (0, 0, 0))
    text_7 = font_1.render(f'английскими буквами.', True, (0, 0, 0))
    text_9 = font_1.render(f'После регистрации не забудьте нажать', True, (0, 0, 0))
    text_10 = font_1.render(f'SPACE, для перехода на начальный экран', True, (0, 0, 0))
    text_11 = font_1.render(f'УДАЧНОЙ ИГРЫ!', True, (196, 30, 58))
    text_12 = font_1.render(f'НАЖМИТЕ SPACE, ЧТОБЫ ПРОДОЛЖИТЬ', True, (0, 0, 0))

    running = True

    while running:
        screen.fill((196, 195, 195))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
        screen.blit(text, (35, 20))

        screen.blit(text_1, (100, 80))
        screen.blit(text_2, (35, 125))
        screen.blit(text_3, (70, 170))
        screen.blit(text_6, (60, 215))
        screen.blit(text_7, (240, 255))
        screen.blit(text_9, (120, 305))
        screen.blit(text_10, (110, 345))
        screen.blit(text_11, (280, 390))
        screen.blit(text_12, (152, 550))

        pygame.display.flip()


if __name__ == '__main__':
    reg_rules()

