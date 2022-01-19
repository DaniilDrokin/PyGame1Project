import sqlite3
import pygame


def records():
    def draw(your_record):
        if your_record >= 200:
            print(1)
        elif your_record >= 100:
            print(2)
        elif your_record >= 50:
            print(3)
        else:
            print(4)

    pygame.init()
    size = 1360, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Рекорд')

    with open("data/log_pas.txt") as file:
        data = list(map(str.strip, file.readlines()))
        for elem in data:
            login, password = elem.split()

    conn = sqlite3.connect('data/Records.db')
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
        screen.fill((196, 195, 195))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw(record)
        pygame.display.flip()


if __name__ == '__main__':
    records()
