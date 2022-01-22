import pygame


def reg_rules():  # Функция, отвечающая за правил регистрации
    pygame.init()
    size = 800, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Как начать играть')

    # Создание шрифтов и текстов
    font = pygame.font.Font('PyGame1Project/data/Rex Bold.ttf', 50)
    font_1 = pygame.font.Font('PyGame1Project/data/Rex Bold.ttf', 35)
    text = font.render(f'ЗДРАВСТВУЙ, Дорогой Пользователь!', True, (196, 30, 58))
    text_1 = font_1.render(f'Перед тем как вы сможете начать играть в', True, (0, 0, 0))
    text_2 = font_1.render(f'EGG_catcher, вам нужно будет зарегистрироваться,', True, (0, 0, 0))
    text_3 = font_1.render(f'чтобы ваши лучшие результаты сохранялись.', True, (0, 0, 0))
    text_4 = font_1.render(f'Для этого введите логин и пароль маленькими', True, (0, 0, 0))
    text_5 = font_1.render(f'английскими буквами.', True, (0, 0, 0))
    text_6 = font_1.render(f'После регистрации не забудьте нажать', True, (0, 0, 0))
    text_7 = font_1.render(f'SPACE, для перехода на начальный экран', True, (0, 0, 0))
    text_8 = font_1.render(f'УДАЧНОЙ ИГРЫ!', True, (196, 30, 58))
    text_9 = font_1.render(f'НАЖМИТЕ SPACE, ЧТОБЫ ПРОДОЛЖИТЬ', True, (0, 0, 0))

    running = True

    while running:
        screen.fill((196, 195, 195))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # Закрытие окна при нажатии ESCAPE
                if event.key == pygame.K_SPACE:
                    running = False
        # Вывод текста
        screen.blit(text, (35, 20))
        screen.blit(text_1, (100, 80))
        screen.blit(text_2, (35, 125))
        screen.blit(text_3, (70, 170))
        screen.blit(text_4, (60, 215))
        screen.blit(text_5, (240, 255))
        screen.blit(text_6, (120, 305))
        screen.blit(text_7, (110, 345))
        screen.blit(text_8, (280, 390))
        screen.blit(text_9, (152, 550))

        pygame.display.flip()


if __name__ == '__main__':
    reg_rules()
