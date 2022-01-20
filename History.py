import pygame


def history():
    pygame.init()
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('История игры')

    font = pygame.font.Font('data/Rex Bold.ttf', 50)
    font_1 = pygame.font.Font('data/Rex Bold.ttf', 35)
    text = font.render(f'ИСТОРИЯ ИГРЫ', True, (196, 30, 58))
    text_1 = font_1.render(f'В 70-х компания Nintendo выпустила', True, (0, 0, 0))
    text_2 = font_1.render(f'серию гаджетов Game & Watch, на которых', True, (0, 0, 0))
    text_3 = font_1.render(f'можно было сыграть в несложные игры.', True, (0, 0, 0))
    text_6 = font_1.render(f'В 1981 г. вышел первый прототип "Ну, погоди!",', True, (0, 0, 0))
    text_7 = font_1.render(f'в котором яйца ловил обычный волк.', True, (0, 0, 0))
    text_9 = font_1.render(f'Затем модельный ряд пополнили игры', True, (0, 0, 0))
    text_10 = font_1.render(f'Octopus, Mickey Mouse и Master Chief', True, (0, 0, 0))
    text_11 = font_1.render(f'которые геймплейно они почти не отличались.', True, (0, 0, 0))
    text_12 = font_1.render(f'Разработка приглянулась Министерству', True, (0, 0, 0))
    text_13 = font_1.render(f'электронной промышленности СССР, которое', True, (0, 0, 0))
    text_14 = font_1.render(f'под маркой "Электроника" выпускало', True, (0, 0, 0))
    text_15 = font_1.render(f'различные бытовые электроприборы.', True, (0, 0, 0))
    text_16 = font_1.render(f'В 1984 г. "Электроника ИМ-02" добралась', True, (0, 0, 0))
    text_17 = font_1.render(f'до советских магазинов. Аббревиатура "ИМ"', True, (0, 0, 0))
    text_18 = font_1.render(f'означала "игра микропроцессорная", а', True, (0, 0, 0))
    text_19 = font_1.render(f'геймплей был похож разработки Nintendo,', True, (0, 0, 0))
    text_20 = font_1.render(f'но с поправкой на визуальный стиль', True, (0, 0, 0))
    text_21 = font.render(f'"Ну, погоди!"', True, (196, 30, 58))
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

        screen.blit(text_1, (140, 85))
        screen.blit(text_2, (80, 120))
        screen.blit(text_3, (80, 160))
        screen.blit(text_6, (80, 190))
        screen.blit(text_7, (80, 230))
        screen.blit(text_9, (140, 270))
        screen.blit(text_10, (80, 310))
        screen.blit(text_11, (80, 340))
        screen.blit(text_12, (140, 380))
        screen.blit(text_13, (80, 410))
        screen.blit(text_14, (80, 450))
        screen.blit(text_15, (80, 490))
        screen.blit(text_16, (140, 530))
        screen.blit(text_17, (80, 570))
        screen.blit(text_18, (100, 610))
        screen.blit(text_19, (85, 640))
        screen.blit(text_20, (120, 680))

        screen.blit(text_21, (260, 730))

        pygame.display.flip()


if __name__ == '__main__':
    history()