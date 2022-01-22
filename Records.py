import sqlite3
import pygame
import os


def records():  # Функция, отвечающая за вывод рекордов
    def load_image(name, colorkey=None):
        fullname = os.path.join("PyGame1Project/data", name)
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def draw(your_record):  # Функция рисования
        # Вывод различных кубков и цвета текста при разном рекорде
        if your_record >= 200:
            screen.fill((196, 195, 195))
            screen.blit(load_image("cup_golden.png"), (150, 50))
            text = font.render(f'ВАШ РЕКОРД:', True, (255, 215, 0))
            text_1 = font.render(f'{your_record}', True, (255, 215, 0))
            screen.blit(text_1, (225, 625))
        elif your_record >= 100:
            screen.fill((255, 255, 255))
            screen.blit(load_image("cup_silver.png"), (-200, 50))
            text = font.render(f'ВАШ РЕКОРД:', True, (192, 192, 192))
            text_1 = font.render(f'{your_record}', True, (192, 192, 192))
            screen.blit(text_1, (225, 625))
        else:
            screen.fill((196, 195, 195))
            screen.blit(load_image("cup_bronze.png"), (-525, 50))
            text = font.render(f'ВАШ РЕКОРД:', True, (205, 127, 50))
            text_1 = font.render(f'{your_record}', True, (205, 127, 50))
            screen.blit(text_1, (275, 625))
        screen.blit(text, (50, 525))

    pygame.init()
    size = 600, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Рекорд')
    font_2 = pygame.font.Font('PyGame1Project/data/Rex Bold.ttf', 20)
    text_3 = font_2.render(f'ESC для выхода', True, (0, 0, 0))

    # Получение логина и пароля, зарегистрированного пользователя, из txt файла
    with open("PyGame1Project/data/log_pas.txt") as file:
        data = list(map(str.strip, file.readlines()))
        for elem in data:
            login, password = elem.split()

    font = pygame.font.Font('PyGame1Project/data/Rex Bold.ttf', 100)
    fanfare_sound = pygame.mixer.Sound("PyGame1Project/data/fanfare.wav")
    flag = True

    # Получение рекорда из БД
    conn = sqlite3.connect('PyGame1Project/data/Records.db')
    cursor = conn.cursor()
    find_rec = cursor.execute('''SELECT record FROM records
                    WHERE login = (?) and password = (?)''', (login, password,)).fetchall()
    for elem in find_rec:
        for i in elem:
            record = i
    conn.commit()
    conn.close()

    running = True

    while running:
        if flag:
            fanfare_sound.play()
            flag = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:  # Закрытие окна при нажатии ESCAPE
                if event.key == pygame.K_ESCAPE:
                    running = False
        draw(record)
        screen.blit(text_3, (10, 775))
        pygame.display.flip()


if __name__ == '__main__':
    records()
