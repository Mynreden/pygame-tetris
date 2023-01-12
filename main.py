import pygame
from random import choice as ch
from const import square_side, squareGroup, staticSquareGroup, figureGroup, scoreGroup, SCREEN_WIDTH, SCREEN_HEIGHT, \
    FPS, speed, background, space_image, scores
from FigureClass import Figure
from ScoreClass import Score
from pygame.locals import (
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE
)


def create_new_figure():
    fig = Figure(ch(types))
    for _ in fig:
        squareGroup.add(_)
    figureGroup.add(fig)
    flag = True
    return fig, flag


# def out(cup): Вывод состояния стакана в виде массива
#     for i in range(len(cup)):
#         for j in range(len(cup[i])):
#             print(int(cup[i][j][0]), end=' ')
#         print()


clock = pygame.time.Clock()  # обьект для ФПС

cup = []
for i in range(20):
    temp = []
    for j in range(10):
        temp.append((False, None))
    cup.append(temp)

fall = False  # проверка упал обьект или нет
types = [0, 1, 2, 3, 4, 5, 6]  # типы фигур

figure = Figure(ch(types))  # создание обьекта в дальнейшем будет выполняться функция

for i in figure:  # добавление в группы
    squareGroup.add(i)
figureGroup.add(figure)

# создание счетчика очков
score = Score()
scoreGroup.add(score)

pygame.init()  # запуск игры
score.set_font() # добавление шрифта
screen = pygame.display.set_mode((SCREEN_WIDTH + 200, SCREEN_HEIGHT))
running = True

timer = 0  # счетчик кадров, от него зависит скорость

while running:
    # действия по кнопкам
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_RIGHT:
                figureGroup.update(square_side, 0)
            elif event.key == K_LEFT:
                figureGroup.update(-square_side, 0)
            elif event.key == K_DOWN:
                figureGroup.update(0, square_side)
            elif event.key == K_SPACE:
                figure.rotate()

    # движение фигуры
    timer += 1
    if timer == speed:
        figureGroup.update(0, square_side)
        timer = 0

    # удаление и создание обекта при падении
    if any([pygame.sprite.spritecollideany(i, staticSquareGroup) for i in figure]):
        figure.delete(cup, 1)
        figure, fall = create_new_figure()
    elif any([i.rect.bottom == SCREEN_HEIGHT for i in figure]):
        figure.delete(cup)
        figure, fall = create_new_figure()

    # удаление строк при заполнении
    if fall:
        fall = not fall
        i = 19
        killed_lines = 0
        while any(list(map(lambda x: x[0], cup[i]))):
            if all(list(map(lambda x: x[0], cup[i]))):  # проверка если линия заполнена
                # удаление заполненой строки
                for j in range(10):
                    cup[i][j][1].kill()
                cup[i].clear()
                for j in range(10):
                    cup[i].append((False, None))

                killed_lines += 1 # Счетчик удаленных строк

                # понижение всех элементов находящихся выше удаляемой строки
                for j in range(i, 0, -1):
                    for _ in range(10):
                        if cup[j][_][0]:
                            cup[j][_][1].update(0, square_side)
                    cup[j].clear()
                    for m in cup[j - 1]:
                        cup[j].append(m)
                continue
            i -= 1
            # завершение игры
            if i == 0:
                print("it is end")
                running = False
                break
        score.add_score(scores[killed_lines - 1])

    # обновление фото
    screen.blit(background, (0, 0))
    screen.blit(space_image, (SCREEN_WIDTH, 0))
    staticSquareGroup.draw(screen)
    squareGroup.draw(screen)
    scoreGroup.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()
