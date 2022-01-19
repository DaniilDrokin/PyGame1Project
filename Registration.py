import pygame

import sqlite3


def registration():

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
    size = 600, 330
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Регистрация')

    running = True

    font = pygame.font.Font('data/Days.ttf', 40)
    font_er = pygame.font.Font('data/Days.ttf', 30)
    text_1 = font.render(f'пароль:', True, (0, 0, 0))
    text_2 = font.render(f'логин:', True, (0, 0, 0))
    text_3 = font.render(f'', True, (0, 0, 0))
    text_4 = font.render(f'', True, (0, 0, 0))
    text_5 = font_er.render(f'Извините, но вы не можете', True, (0, 0, 0))
    text_6 = font_er.render(f'использовать данный символ :(', True, (0, 0, 0))
    text_8 = font_er.render(f'или вы достигли предела символов', True, (0, 0, 0))
    text_7 = font_er.render(f'Этот логин или пароль уже заняты', True, (0, 0, 0))
    login_text = ''
    password_text = ''
    password_flag = False
    login_flag = False
    error_flag = False
    error_log_pas = False
    space_flag = False
    login = ''
    password = ''

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
                if event.key == pygame.K_SPACE and password_text != '' and login_text != '':
                    conn = sqlite3.connect('data/Records.db')
                    cursor = conn.cursor()
                    was_login_before = cursor.execute('''SELECT login, password FROM records
                    WHERE login = (?) and  password = (?)''', (login_text, password_text,)).fetchall()
                    log_in_db = cursor.execute('''SELECT login FROM records
                    WHERE login = (?)''', (login_text,)).fetchall()
                    pas_in_db = cursor.execute('''SELECT login FROM records
                    WHERE password = (?)''', (password_text,)).fetchall()
                    if was_login_before:
                        for elem in was_login_before:
                            login, password = elem
                        with open("data/log_pas.txt", 'w') as f:
                            f.write(f'{login} {password}')
                        running = False
                    elif not log_in_db and not pas_in_db:
                        cursor.execute('''insert into records (login, password, record) values (?, ?, ?)''',
                                       (login_text, password_text, 0,))
                        with open("data/log_pas.txt", 'w') as f:
                            f.write(f'{login_text} {password_text}')
                        running = False
                    else:
                        error_log_pas = True
                    conn.commit()
                    conn.close()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in lines_sprites:
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if button.return_name() == 'login':
                            login_flag = True
                            password_flag = False
                        else:
                            login_flag = False
                            password_flag = True

            if event.type == pygame.KEYDOWN and login_flag:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and login_text != '':
                    login_text = login_text[:-1]
                    text_3 = font.render(login_text, True, (0, 0, 0))
                else:
                    if 65 <= event.key <= 122 and event.key != 91 and event.key != 92 and event.key != 93\
                            and len(login_text) < 12:
                        login_text += chr(event.key)
                        text_3 = font.render(login_text, True, (0, 0, 0))
                        error_flag = False
                    else:
                        error_flag = True

            if event.type == pygame.KEYDOWN and password_flag:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and password_text != '':
                    password_text = password_text[:-1]
                    text_4 = font.render(password_text, True, (0, 0, 0))
                else:
                    if 65 <= event.key <= 122 and event.key != 91 and event.key != 92 and event.key != 93\
                            and len(password_text) < 12:
                        password_text += chr(event.key)
                        text_4 = font.render(password_text, True, (0, 0, 0))
                        error_flag = False
                    else:
                        error_flag = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_flag = True
                else:
                    space_flag = False
        draw()
        lines_sprites.draw(screen)
        lines_sprites.update()
        if error_flag and not space_flag:
            screen.blit(text_5, (75, 230))
            screen.blit(text_6, (35, 260))
            screen.blit(text_8, (0, 290))
        if error_log_pas:
            screen.blit(text_7, (5, 0))
        screen.blit(text_3, (55, 70))
        screen.blit(text_4, (55, 170))
        pygame.display.flip()


if __name__ == '__main__':
    registration()
