import random

import pygame
import os


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
            self.image = load_image('gee.png')
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.position = number
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
            if pygame.sprite.collide_mask(self, grass):
                self.flag = True
                self.image = load_image('broken_egg.png')
                for elem in heart_sprites:
                    while self.count == 1:
                        elem.kill()
                        self.count -= 1

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

    class Basket(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(all_sprites)
            self.image = load_image('basket.png')
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x = 500
            self.rect.y = 500
            self.score = 0

        def move(self, x, y):
            self.rect.x = x
            self.rect.y = y

        def update(self):
            for elem in egg_sprites:
                if pygame.sprite.collide_mask(self, elem) and not elem.flag:
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

    all_sprites = pygame.sprite.Group()
    egg_sprites = pygame.sprite.Group()
    heart_sprites = pygame.sprite.Group()

    f = pygame.font.Font('data/Rex Bold.ttf', 100)

    grass = Grass()
    basket = Basket()
    house_1 = House('pixel_house_1.png', 0)
    house_2 = House('pixel_house_2.png', 1020)

    clock = pygame.time.Clock()
    running = True
    positions_for_eggs = [(0, 200), (0, 425), (1200, 200), (1200, 425)]

    my_event = pygame.USEREVENT + 1
    timer = 3000
    pygame.time.set_timer(my_event, timer)
    count_of_eggs = 0
    velocity = 1
    pos_x_hearts = 1000
    egg_flag = True
    second_egg = False

    for i in range(3):
        name = 'heart' + str(i)
        Heart(pos_x_hearts, name)
        pos_x_hearts -= 125

    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == my_event and heart_sprites:
                count_of_eggs += 1
                number = random.randint(0, 3)
                Egg(positions_for_eggs[number], number)
                if second_egg:
                    if number == 0:
                        number = random.choice([1, 2, 3])
                    if number == 1:
                        number = random.choice([0, 2, 3])
                    if number == 2:
                        number = random.choice([0, 1, 3])
                    if number == 3:
                        number = random.choice([0, 1, 2])
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

            if event.type == pygame.KEYDOWN and heart_sprites:
                if event.key == pygame.K_r:
                    basket.move(240, 250)
                if event.key == pygame.K_f:
                    basket.move(240, 475)
                if event.key == pygame.K_i:
                    basket.move(835, 250)
                if event.key == pygame.K_j:
                    basket.move(835, 475)

        screen.fill((179, 221, 247))
        all_sprites.draw(screen)
        all_sprites.update()
        egg_sprites.draw(screen)
        egg_sprites.update(velocity)
        heart_sprites.draw(screen)
        heart_sprites.update()

        text = f.render(f'{basket.score}', True, (196, 30, 58))
        screen.blit(text, (300, 80))

        screen.blit(load_image("bush.png"), (-13, 580))
        screen.blit(load_image("bush.png"), (1087, 580))

        if not heart_sprites:
            f_1 = pygame.font.Font('data/Rex Bold.ttf', 200)
            text = f_1.render(f'ВЫ ПРОИГРАЛИ!', True, (196, 30, 58))
            screen.blit(text, (100, 300))
            for egg in egg_sprites:
                egg.kill()

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    game()
