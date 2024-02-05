# import pygame
# from .group import SpriteGroup, RectangleGroup
# import SwitchGame as sw

from .group import SpriteGroup, RectangleGroup

import pygame


class Collider:
    
    @classmethod
    def group_collider(cls, __sprite, *__groups: SpriteGroup | RectangleGroup) -> list[pygame.Rect]:
        collisions = []

        for group in __groups:
            for sprite in group.get():
                if isinstance(group, SpriteGroup):
                    if cls.__collide_rect(__sprite.rectangle, sprite.rectangle):
                        collisions.append(sprite.rectangle)

                if isinstance(group, RectangleGroup):
                    if cls.__collide_rect(__sprite.rectangle, sprite):
                        collisions.append(sprite)
        
        return collisions
    
    @classmethod
    def __collide_rect(cls, __rect_0: pygame.Rect, __rect_1: pygame.Rect) -> bool:
        return __rect_0.colliderect(__rect_1)