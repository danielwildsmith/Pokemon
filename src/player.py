from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, invisible_sprites):
        super().__init__(group)
        self.image = pygame.image.load('../graphics/player/down/0.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect.inflate((-60, -10))
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.status = 'down'
        self.frame_index = 0
        self.animation_speed = 0.15

        self.invisible_sprites = invisible_sprites

        self.animations = self.import_player_animations()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        elif keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')

        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.invisible_sprites:
                if sprite.sprite_type == 'boundary' and sprite.rect.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.rect.right
        if direction == 'vertical':
            for sprite in self.invisible_sprites:
                if sprite.sprite_type == 'boundary' and sprite.rect.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.rect.bottom

    def in_wild_area(self):
        for sprite in self.invisible_sprites:
            if sprite.sprite_type == 'wild_area' and sprite.rect.colliderect(self.hitbox):
                return True
        return False

    def import_player_animations(self):
        player_path = '../graphics/player/'
        animations = {'up': [], 'down': [], 'left': [], 'right': []}
        for animation in animations:
            path = player_path + animation
            animations[animation] = import_folder(path)
        return animations

    def animate(self):
        animation = self.animations[self.status]

        if self.direction.magnitude() == 0:
            self.image = animation[0]
        else:
            self.frame_index += self.animation_speed
            if self.frame_index >= len(animation):
                self.frame_index = 0

            self.image = animation[int(self.frame_index)]
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect(center=self.hitbox.center)

    def update(self):
        self.input()
        self.move()
        self.animate()
