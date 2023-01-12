from pygame.sprite import Sprite, spritecollideany
from const import staticSquareGroup, SCREEN_WIDTH, SCREEN_HEIGHT


class Square(Sprite):
    def __init__(self, x, y, photo):
        super().__init__()
        self.image = photo
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self, x, y):
        self.rect.center = [self.rect.centerx + x, self.rect.centery + y]

    def is_normal(self):
        return self.rect.top >= 0 and self.rect.left >= 0 and self.rect.bottom <= SCREEN_HEIGHT and \
               self.rect.right <= SCREEN_WIDTH and not spritecollideany(self, staticSquareGroup)
