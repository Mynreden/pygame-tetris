from pygame.sprite import Sprite, spritecollideany
from pygame.font import Font, get_default_font
from const import SCREEN_WIDTH


class Score(Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)
        self.number = 0
        self.text = f"Score: {str(self.number)}"
        self.font = None

    def set_font(self):
        self.font = Font(get_default_font(), 20)
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH + 100, 200)

    def add_score(self, num=0):
        self.number += num
        self.text = f"Score: {str(self.number)}"
        self.image = self.font.render(self.text, 1, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH + 100, 200)
