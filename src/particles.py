import pygame
from settings import import_folder


class ParticleAnimationPlayer:
    def __init__(self):
        self.frames = {
            # animations from Ninja Boy's Adventure Asset Pack
            'thunder': import_folder('../graphics/particles/thunder'),
            'heal': import_folder('../graphics/particles/heal'),
            'slash': import_folder('../graphics/particles/slash'),
            'stat_move': import_folder('../graphics/particles/stat_move/frames')
        }

    def create_particles(self, animation_type, pos, group):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, group)


# Code altered slightly from Clear Code's YT Zelda tutorial
class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self, pos, animation_frames, group):
        super().__init__(group)
        self.frame_index = 0
        self.animation_speed = 0.10
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()
