from pygame.sprite import Sprite, spritecollideany
from const import square_side, squareGroup, staticSquareGroup, figureGroup, SCREEN_WIDTH, SCREEN_HEIGHT, photos
from SquareClass import Square


class Figure(Sprite):
    def __init__(self, type_id):
        super().__init__()
        self.id = type_id
        self.position = 0
        if type_id == 0:  # i
            self.contain = [Square(4 * square_side, 0, photos[type_id]),
                            Square(4 * square_side, square_side, photos[type_id]),
                            Square(4 * square_side, square_side * 2, photos[type_id]),
                            Square(4 * square_side, square_side * 3, photos[type_id])]
        elif type_id == 1:  # j
            self.contain = [Square(square_side * 5, 0, photos[type_id]),
                            Square(square_side * 5, square_side, photos[type_id]),
                            Square(square_side * 5, square_side * 2, photos[type_id]),
                            Square(4 * square_side, square_side * 2, photos[type_id])]
        elif type_id == 2:  # l
            self.contain = [Square(4 * square_side, 0, photos[type_id]),
                            Square(4 * square_side, square_side, photos[type_id]),
                            Square(4 * square_side, square_side * 2, photos[type_id]),
                            Square(square_side * 5, square_side * 2, photos[type_id])]
        elif type_id == 3:  # o
            self.contain = [Square(4 * square_side, 0, photos[type_id]),
                            Square(4 * square_side, square_side, photos[type_id]),
                            Square(square_side * 5, 0, photos[type_id]),
                            Square(square_side * 5, square_side, photos[type_id])]
        elif type_id == 4:  # z
            self.contain = [Square(4 * square_side, 0, photos[type_id]),
                            Square(square_side * 5, 0, photos[type_id]),
                            Square(square_side * 5, square_side, photos[type_id]),
                            Square(square_side * 6, square_side, photos[type_id])]
        elif type_id == 5:  # s
            self.contain = [Square(4 * square_side, square_side, photos[type_id]),
                            Square(square_side * 5, square_side, photos[type_id]),
                            Square(square_side * 5, 0, photos[type_id]),
                            Square(square_side * 6, 0, photos[type_id])]
        elif type_id == 6:  # t
            self.contain = [Square(4 * square_side, 0, photos[type_id]),
                            Square(square_side * 5, 0, photos[type_id]),
                            Square(square_side * 6, 0, photos[type_id]),
                            Square(square_side * 5, square_side, photos[type_id])]

    def update(self, x, y):
        if not any([i.rect.right + x > SCREEN_WIDTH or i.rect.left + x < 0 or i.rect.bottom + y > SCREEN_HEIGHT for i in
                    self]):
            for i in self:
                i.update(x, y)
        if y == 0 and any([spritecollideany(i, staticSquareGroup) for i in self]):
            for i in self:
                i.update(-x, y)

    def is_normal(self):
        for i in self:
            if not i.is_normal():
                return False
        return True

    def delete(self, cup, is_collision=0):
        for i in self:
            squareGroup.remove(i)
            m = Square(i.rect.left, i.rect.top - square_side * is_collision, photos[self.id])
            staticSquareGroup.add(m)
            cup[(i.rect.top - square_side * is_collision) // square_side][i.rect.left // square_side] = (True, m)
        figureGroup.remove(self)

    def rotate(self):
        if self.id == 0:  # i
            if self.position == 0:
                self[0].rect.top += square_side
                self[0].rect.left += square_side * 2
                self[1].rect.left += square_side
                self[2].rect.top -= square_side
                self[3].rect.left -= square_side
                self[3].rect.top -= square_side * 2
                self.position += 1
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side
                    self[0].rect.left -= square_side * 2
                    self[1].rect.left -= square_side
                    self[2].rect.top += square_side
                    self[3].rect.left += square_side
                    self[3].rect.top += square_side * 2
            elif self.position == 1:
                self[0].rect.top -= square_side
                self[0].rect.left -= square_side
                self[2].rect.top += square_side
                self[2].rect.left += square_side
                self[3].rect.left += square_side * 2
                self[3].rect.top += square_side * 2
                self.position = self.position + 1
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top += square_side
                    self[0].rect.left += square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left -= square_side
                    self[3].rect.left -= square_side * 2
                    self[3].rect.top -= square_side * 2
            elif self.position == 2:
                self[0].rect.top += square_side * 2
                self[0].rect.left += square_side
                self[1].rect.top += square_side
                self[2].rect.left -= square_side
                self[3].rect.left -= square_side * 2
                self[3].rect.top -= square_side
                self.position += 1
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side * 2
                    self[0].rect.left -= square_side
                    self[1].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[3].rect.left += square_side * 2
                    self[3].rect.top += square_side
            elif self.position == 3:
                self[0].rect.top -= square_side * 2
                self[0].rect.left -= square_side * 2
                self[1].rect.left -= square_side
                self[1].rect.top -= square_side
                self[3].rect.left += square_side
                self[3].rect.top += square_side
                self.position = 0
                if not self.is_normal():
                    self[0].rect.top += square_side * 2
                    self[0].rect.left += square_side * 2
                    self[1].rect.left += square_side
                    self[1].rect.top += square_side
                    self[3].rect.left -= square_side
                    self[3].rect.top -= square_side
                    self.position = 3

        if self.id == 1:  # j
            if self.position == 0:
                self.position += 1
                self[0].rect.left += square_side
                self[0].rect.top += square_side
                self[2].rect.left -= square_side
                self[2].rect.top -= square_side
                self[3].rect.top -= square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left -= square_side
                    self[0].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[2].rect.top += square_side
                    self[3].rect.top += square_side * 2
            elif self.position == 1:
                self.position += 1
                self[0].rect.top += square_side
                self[0].rect.left -= square_side
                self[2].rect.top -= square_side
                self[2].rect.left += square_side
                self[3].rect.left += square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side
                    self[0].rect.left += square_side
                    self[2].rect.top += square_side
                    self[2].rect.left -= square_side
                    self[3].rect.left -= square_side * 2
            elif self.position == 2:
                self.position += 1
                self[0].rect.top -= square_side
                self[0].rect.left -= square_side
                self[2].rect.top += square_side
                self[2].rect.left += square_side
                self[3].rect.top += square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top += square_side
                    self[0].rect.left += square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left -= square_side
                    self[3].rect.top -= square_side * 2
            elif self.position == 3:
                self.position = 0
                self[0].rect.top -= square_side
                self[0].rect.left += square_side
                self[2].rect.top += square_side
                self[2].rect.left -= square_side
                self[3].rect.left -= square_side * 2
                if not self.is_normal():
                    self.position = 3
                    self[0].rect.top += square_side
                    self[0].rect.left -= square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[3].rect.left += square_side * 2
        if self.id == 2:  # l
            if self.position == 0:
                self.position += 1
                self[0].rect.left += square_side
                self[0].rect.top += square_side
                self[2].rect.left -= square_side
                self[2].rect.top -= square_side
                self[3].rect.left -= square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left -= square_side
                    self[0].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[2].rect.top += square_side
                    self[3].rect.left += square_side * 2
            elif self.position == 1:
                self.position += 1
                self[0].rect.top += square_side
                self[0].rect.left -= square_side
                self[2].rect.top -= square_side
                self[2].rect.left += square_side
                self[3].rect.top -= square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side
                    self[0].rect.left += square_side
                    self[2].rect.top += square_side
                    self[2].rect.left -= square_side
                    self[3].rect.top += square_side * 2
            elif self.position == 2:
                self.position += 1
                self[0].rect.top -= square_side
                self[0].rect.left -= square_side
                self[2].rect.top += square_side
                self[2].rect.left += square_side
                self[3].rect.left += square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top += square_side
                    self[0].rect.left += square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left -= square_side
                    self[3].rect.left -= square_side * 2
            elif self.position == 3:
                self.position = 0
                self[0].rect.top -= square_side
                self[0].rect.left += square_side
                self[2].rect.top += square_side
                self[2].rect.left -= square_side
                self[3].rect.top += square_side * 2
                if not self.is_normal():
                    self.position = 3
                    self[0].rect.top += square_side
                    self[0].rect.left -= square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[3].rect.top -= square_side * 2
        if self.id == 4:  # z
            if self.position == 0:
                self.position += 1
                self[0].rect.left += square_side * 2
                self[1].rect.top += square_side
                self[1].rect.left += square_side
                self[3].rect.top += square_side
                self[3].rect.left -= square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left -= square_side * 2
                    self[1].rect.top -= square_side
                    self[1].rect.left -= square_side
                    self[3].rect.top -= square_side
                    self[3].rect.left += square_side
            elif self.position == 1:
                self.position += 1
                self[0].rect.top += square_side * 2
                self[1].rect.top += square_side
                self[1].rect.left -= square_side
                self[3].rect.top -= square_side
                self[3].rect.left -= square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side * 2
                    self[1].rect.top -= square_side
                    self[1].rect.left += square_side
                    self[3].rect.top += square_side
                    self[3].rect.left += square_side
            elif self.position == 2:
                self.position += 1
                self[0].rect.left -= square_side * 2
                self[1].rect.top -= square_side
                self[1].rect.left -= square_side
                self[3].rect.top -= square_side
                self[3].rect.left += square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left += square_side * 2
                    self[1].rect.top += square_side
                    self[1].rect.left += square_side
                    self[3].rect.top += square_side
                    self[3].rect.left -= square_side
            elif self.position == 3:
                self.position = 0
                self[0].rect.top -= square_side * 2
                self[1].rect.top -= square_side
                self[1].rect.left += square_side
                self[3].rect.top += square_side
                self[3].rect.left += square_side
                if not self.is_normal():
                    self.position = 3
                    self[0].rect.top += square_side * 2
                    self[1].rect.top += square_side
                    self[1].rect.left -= square_side
                    self[3].rect.top -= square_side
                    self[3].rect.left -= square_side
        elif self.id == 5:  # s
            if self.position == 0:
                self.position += 1
                self[0].rect.top -= square_side
                self[0].rect.left += square_side
                self[2].rect.top += square_side
                self[2].rect.left += square_side
                self[3].rect.top += square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top += square_side
                    self[0].rect.left -= square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left -= square_side
                    self[3].rect.top -= square_side * 2
            elif self.position == 1:
                self.position += 1
                self[0].rect.top += square_side
                self[0].rect.left += square_side
                self[2].rect.top += square_side
                self[2].rect.left -= square_side
                self[3].rect.left -= square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side
                    self[0].rect.left -= square_side
                    self[2].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[3].rect.left += square_side * 2
            elif self.position == 2:
                self.position += 1
                self[0].rect.top += square_side
                self[0].rect.left -= square_side
                self[2].rect.top -= square_side
                self[2].rect.left -= square_side
                self[3].rect.top -= square_side * 2
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.top -= square_side
                    self[0].rect.left += square_side
                    self[2].rect.top += square_side
                    self[2].rect.left += square_side
                    self[3].rect.top += square_side * 2
            elif self.position == 3:
                self.position = 0
                self[0].rect.top -= square_side
                self[0].rect.left -= square_side
                self[2].rect.top -= square_side
                self[2].rect.left += square_side
                self[3].rect.left += square_side * 2
                if not self.is_normal():
                    self.position = 3
                    self[0].rect.top += square_side
                    self[0].rect.left += square_side
                    self[2].rect.top += square_side
                    self[2].rect.left -= square_side
                    self[3].rect.left -= square_side * 2
        elif self.id == 6:  # t
            if self.position == 0:
                self.position += 1
                self[0].rect.left += square_side
                self[0].rect.top -= square_side
                self[2].rect.left -= square_side
                self[2].rect.top += square_side
                self[3].rect.left -= square_side
                self[3].rect.top -= square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left -= square_side
                    self[0].rect.top += square_side
                    self[2].rect.left += square_side
                    self[2].rect.top -= square_side
                    self[3].rect.left += square_side
                    self[3].rect.top += square_side
            elif self.position == 1:
                self.position += 1
                self[0].rect.left += square_side
                self[0].rect.top += square_side
                self[2].rect.left -= square_side
                self[2].rect.top -= square_side
                self[3].rect.left += square_side
                self[3].rect.top -= square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left -= square_side
                    self[0].rect.top -= square_side
                    self[2].rect.left += square_side
                    self[2].rect.top += square_side
                    self[3].rect.left -= square_side
                    self[3].rect.top += square_side
            elif self.position == 2:
                self.position += 1
                self[0].rect.left -= square_side
                self[0].rect.top += square_side
                self[2].rect.left += square_side
                self[2].rect.top -= square_side
                self[3].rect.left += square_side
                self[3].rect.top += square_side
                if not self.is_normal():
                    self.position -= 1
                    self[0].rect.left += square_side
                    self[0].rect.top -= square_side
                    self[2].rect.left -= square_side
                    self[2].rect.top += square_side
                    self[3].rect.left -= square_side
                    self[3].rect.top -= square_side
            elif self.position == 3:
                self.position = 0
                self[0].rect.left -= square_side
                self[0].rect.top -= square_side
                self[2].rect.left += square_side
                self[2].rect.top += square_side
                self[3].rect.left -= square_side
                self[3].rect.top += square_side
                if not self.is_normal():
                    self.position = 3
                    self[0].rect.left += square_side
                    self[0].rect.top += square_side
                    self[2].rect.left -= square_side
                    self[2].rect.top -= square_side
                    self[3].rect.left += square_side
                    self[3].rect.top -= square_side

    def __getitem__(self, item):
        return self.contain[item]
