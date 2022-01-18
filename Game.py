import random
import pygame
import os
import sqlite3


def game():
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

    class Grass(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(all_sprites)
            self.image = load_image("grass.png")
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.bottom = height + 60

    class Egg(pygame.sprite.Sprite):
        def __init__(self, position, number):
            super().__init__(egg_sprites)
            self.images = []
            self.position = number

            if self.position == 0 or self.position == 1:
                self.images.append(load_image('egg1.png'))
                self.images.append(load_image('egg6.png'))
                self.images.append(load_image('egg2.png'))
                self.images.append(load_image('egg7.png'))
                self.images.append(load_image('egg3.png'))
                self.images.append(load_image('egg8.png'))
                self.images.append(load_image('egg4.png'))
                self.images.append(load_image('egg5.png'))
            else:
                self.images.append(load_image('egg1.png'))
                self.images.append(load_image('egg5.png'))
                self.images.append(load_image('egg4.png'))
                self.images.append(load_image('egg8.png'))
                self.images.append(load_image('egg3.png'))
                self.images.append(load_image('egg7.png'))
                self.images.append(load_image('egg2.png'))
                self.images.append(load_image('egg6.png'))

            self.index = 0
            self.counter = 0
            self.frame = 8
            self.image = self.images[self.index]

            self.sound_flag = True
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = position[0]
            self.rect.y = position[1]
            self.flag = False
            self.count = 1

        def update(self, *args):
            speed = args[0]
            if self.position == 0 or self.position == 1:
                if not pygame.sprite.collide_mask(self, grass) and pygame.sprite.collide_mask(self, house_1):
                    self.rect = self.rect.move(speed, 0)
                if not pygame.sprite.collide_mask(self, grass) and not pygame.sprite.collide_mask(self, house_1):
                    self.rect = self.rect.move(0, speed + 2)
            else:
                if not pygame.sprite.collide_mask(self, grass) and pygame.sprite.collide_mask(self, house_2):
                    self.rect = self.rect.move(-speed, 0)
                if not pygame.sprite.collide_mask(self, grass) and not pygame.sprite.collide_mask(self, house_2):
                    self.rect = self.rect.move(0, speed + 2)

            if speed % 20 == 0 and self.frame >= 4:
                self.frame -= 1

            if pygame.sprite.collide_mask(self, grass):
                self.flag = True
                self.image = load_image('broken_egg.png')
                if self.sound_flag:
                    broken_sound.play()
                    self.sound_flag = False
                for elem in heart_sprites:
                    while self.count == 1:
                        elem.kill()
                        self.count -= 1
            else:
                self.counter += 1
                if self.counter == self.frame:
                    self.index += 1
                    self.counter = 0
                if self.index >= len(self.images):
                    self.index = 0
                self.image = self.images[self.index]

        def flag(self):
            return self.flag

    class House(pygame.sprite.Sprite):
        def __init__(self, picture, x):
            super().__init__(all_sprites)
            self.image = load_image(picture)
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x
            self.rect.bottom = height - 100

    class Wolf(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(all_sprites)
            self.image = load_image('wolf_1.png')
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = 560
            self.rect.y = 340
            self.score = 0

        def move(self, x, y, photo):
            self.image = load_image(photo)
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x
            self.rect.y = y

        def update(self):
            for elem in egg_sprites:
                if pygame.sprite.collide_mask(self, elem) and not elem.flag:
                    fall_sound.play()
                    elem.kill()
                    self.score += 1

    class Heart(pygame.sprite.Sprite):
        def __init__(self, x, name):
            super().__init__(heart_sprites)
            self.image = load_image('heart.png')
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = x
            self.rect.y = 80
            self.name = name

    pygame.init()
    size = width, height = 1360, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('НУ, ПОГОДИ!')

    sad_sound = pygame.mixer.Sound("data/sad_sound.wav")
    sad_sound.set_volume(0.5)
    broken_sound = pygame.mixer.Sound("data/egg_shell.wav")
    win_sound = pygame.mixer.Sound("data/win.wav")
    win_sound.set_volume(0.5)
    sound = pygame.mixer.Sound("data/background_sound.wav")
    sound.set_volume(0.2)
    fall_sound = pygame.mixer.Sound("data/fall.wav")
    fall_sound.set_volume(0.4)

    all_sprites = pygame.sprite.Group()
    egg_sprites = pygame.sprite.Group()
    heart_sprites = pygame.sprite.Group()

    f = pygame.font.Font('data/Rex Bold.ttf', 100)

    grass = Grass()
    wolf = Wolf()
    house_1 = House('pixel_house_1.png', 0)
    house_2 = House('pixel_house_2.png', 1020)

    clock = pygame.time.Clock()
    running = True
    sound_flag = True
    background_sound_flag = True
    end_flag = False
    positions_for_eggs = [(55, 200), (45, 425), (1230, 200), (1230, 425)]

    my_event = pygame.USEREVENT + 1
    timer = 3000
    pygame.time.set_timer(my_event, timer)
    count_of_eggs = 0
    velocity = 1
    pos_x_hearts = 1000
    egg_flag = True
    second_egg = False
    record = 0

    for i in range(3):
        name = 'heart' + str(i)
        Heart(pos_x_hearts, name)
        pos_x_hearts -= 125
    while running:
        if background_sound_flag:
            sound.play(loops=-1)
            background_sound_flag = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sound.stop()
                running = False

            if event.type == my_event and heart_sprites:
                count_of_eggs += 1
                number = random.randint(0, 3)
                Egg(positions_for_eggs[number], number)
                if second_egg:
                    if number == 0:
                        number = random.choice([1, 2, 2, 3, 3])
                    elif number == 1:
                        number = random.choice([0, 2, 2, 3, 3])
                    elif number == 2:
                        number = random.choice([0, 0, 1, 1, 3])
                    elif number == 3:
                        number = random.choice([0, 0, 1, 1, 2])
                    Egg(positions_for_eggs[number], number)
                if count_of_eggs == 10 and velocity < 15:
                    velocity += 1
                if count_of_eggs == 20 and timer > 300:
                    timer -= 300
                    pygame.time.set_timer(my_event, timer)
                    count_of_eggs = 0
                if count_of_eggs == 15 and egg_flag:
                    egg_flag = False
                    second_egg = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and end_flag:
                    conn = sqlite3.connect('data/Records.db')
                    cursor = conn.cursor()

                    with open("data/log_pas.txt") as file:
                        data = list(map(str.strip, file.readlines()))
                        for elem in data:
                            login, password = elem.split()

                    b = cursor.execute('''SELECT record FROM records
                    WHERE login = (?)''', (login,)).fetchall()
                    for elem in b:
                        record = int(elem[0])
                    print(record)
                    if wolf.score > record:
                        cursor.execute('''Update records set record = (?)
                        WHERE login = (?) and  password = (?)''', (wolf.score, login, password))
                    conn.commit()
                    conn.close()
                    running = False
                if event.key == pygame.K_e and heart_sprites:
                    wolf.move(240, 340, "wolf_3.png")
                if event.key == pygame.K_f and heart_sprites:
                    wolf.move(240, 410, "wolf_4.png")
                if event.key == pygame.K_i and heart_sprites:
                    wolf.move(560, 340, "wolf_1.png")
                if event.key == pygame.K_j and heart_sprites:
                    wolf.move(600, 410, "wolf_2.png")

        screen.fill((179, 221, 247))
        screen.blit(load_image("fence.png"), (0, 440))
        all_sprites.draw(screen)
        all_sprites.update()
        egg_sprites.draw(screen)
        egg_sprites.update(velocity)
        heart_sprites.draw(screen)
        heart_sprites.update()

        text = f.render(f'{wolf.score}', True, (196, 30, 58))
        screen.blit(text, (300, 80))

        screen.blit(load_image("bush.png"), (-13, 580))
        screen.blit(load_image("bush.png"), (1087, 580))
        screen.blit(load_image("chicken.png"), (-70, 380))
        screen.blit(load_image("chicken_2.png"), (1300, 155))
        screen.blit(load_image("rooster.png"), (1300, 350))
        screen.blit(load_image("chick.png"), (-20, 215))
        screen.blit(load_image("nest.png"), (-80, 165))

        if not heart_sprites:
            sound.stop()
            end_flag = True
            pygame.draw.rect(screen, (255, 250, 205), (0, 0, width, height), 0)
            f_2 = pygame.font.Font('data/Rex Bold.ttf', 30)
            if wolf.score >= 100:
                f_1 = pygame.font.Font('data/Rex Bold.ttf', 130)
                obj = 'ВЫ ХОРОШО ДЕРЖАЛИСЬ!'
                if sound_flag:
                    win_sound.play()
                    sound_flag = False
                screen.blit(load_image("wolf_6.png"), (500, 375))
                text = f_1.render(obj, True, (196, 30, 58))
                screen.blit(text, (60, 250))
            else:
                f_1 = pygame.font.Font('data/Rex Bold.ttf', 200)
                obj = 'ВЫ ПРОИГРАЛИ!'
                if sound_flag:
                    sad_sound.play()
                    sound_flag = False
                screen.blit(load_image("wolf_7.png"), (400, 450))
                text = f_1.render(obj, True, (196, 30, 58))
                screen.blit(text, (100, 250))
            text_2 = f_2.render("НАЖМИТЕ SPACE, ЧТОБЫ ВЫЙТИ", True, (196, 30, 58))
            screen.blit(text_2, (500, 760))

            for egg in egg_sprites:
                egg.kill()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    game()
