import sys, pygame
from pygame.locals import K_SPACE, K_ESCAPE

pygame.init()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

size = [600, 600]
display_features = pygame.HWSURFACE | pygame.DOUBLEBUF
screen = pygame.display.set_mode(size, display_features)
screen_color = 0,0,0
top_text = 'Tic Tac Toe'
player_X_won_text = "X Wins!!!"
player_O_won_text = "O Wins!!!"
draw_text = "Draw!!!"
pygame.display.set_caption("Tic Tac Toe Ver 0.1 by Mihail Lungu")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def victory_check(icon):
    if (images[0] == icon and images[1] == icon and images[2] == icon) or \
       (images[3] == icon and images[4] == icon and images[5] == icon) or \
       (images[6] == icon and images[7] == icon and images[8] == icon) or \
       (images[0] == icon and images[3] == icon and images[6] == icon) or \
       (images[1] == icon and images[4] == icon and images[7] == icon) or \
       (images[2] == icon and images[5] == icon and images[8] == icon) or \
       (images[0] == icon and images[4] == icon and images[8] == icon) or \
       (images[2] == icon and images[4] == icon and images[6] == icon):
        return True
    else:
        return False

def draw_check():
    if None not in images:
        return True
    else:
        return False

def draw_line():
    line_1 = pygame.draw.line(screen, (32,178,170), [225, 500], [225, 100], 10)
    line_2 = pygame.draw.line(screen, (32,178,170), [375, 500], [375, 100], 10)
    line_3 = pygame.draw.line(screen, (32,178,170), [500, 225], [100, 225], 10)
    line_4 = pygame.draw.line(screen, (32,178,170), [500, 375], [100, 375], 10)

def font_name():
    font = pygame.font.Font(None, 80)
    game_name = font.render(top_text, True, (173,255,47))
    rect_game_name = game_name.get_rect()
    rect_game_name = rect_game_name.move((150, 25))
    screen.blit(game_name, rect_game_name)

def X_won():
    font1 = pygame.font.Font(None, 50)
    Xwon = font1.render(player_X_won_text, True, (173,255,47))
    rectXwon = Xwon.get_rect()
    rectXwon = rectXwon.move((200, 550))
    screen.blit(Xwon, rectXwon)

def O_won():
    font2 = pygame.font.Font(None, 50)
    Owon = font2.render(player_O_won_text, True, (173,255,47))
    rectOwon = Owon.get_rect()
    rectOwon = rectOwon.move((200, 550))
    screen.blit(Owon, rectOwon)

def draw():
    font3 = pygame.font.Font(None, 50)
    draw1 = font3.render(draw_text, True, (173,255,47))
    rectdraw = draw1.get_rect()
    rectdraw = rectdraw.move((200, 550))
    screen.blit(draw1, rectdraw)

def resetgame():
    global images, rects
    images = [None for i in range(9)]
    rects = [rect, rect_second, rect_third,
             rect_fourth, rect_fith, rect_six,
             rect_seven, rect_eight, rect_nine]
    screen.fill(screen_color)
    font_name()
    draw_line()
    play_game()


def play_game():
    player_turn = "X"
    running = True
    gameover = 1
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT or keys[K_ESCAPE]:
                sys.exit()
            if keys[K_SPACE]:
                resetgame()
            elif gameover == 1:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    for i, image in enumerate(images):
                        if rects[i].collidepoint(pos):
                            if images[i]:
                                continue
                            if player_turn == "X":
                                screen.blit(X_image, rects[i].topleft)
                                images[i] = X_image
                                player_turn = "O"
                                if victory_check(X_image):
                                    X_won()
                                    gameover = 0
                                elif draw_check():
                                    draw()
                            else:
                                screen.blit(O_image, rects[i].topleft)
                                images[i] = O_image
                                player_turn = "X"
                                if victory_check(O_image):
                                    O_won()
                                    gameover = 0
                                elif draw_check():
                                    draw()
                            pygame.display.update()
        pygame.display.flip()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

picture = pygame.image.load("square1.jpg")
picture = pygame.transform.scale(picture, (110, 110))
rect = picture.get_rect()
rect = rect.move((105, 105))

picture_second = picture
rect_second = picture_second.get_rect()
rect_second = rect_second.move((240, 105))

picture_third = picture
rect_third = picture_third.get_rect()
rect_third = rect_third.move((385, 105))

picture_fourth = picture
rect_fourth = picture_fourth.get_rect()
rect_fourth = rect_fourth.move((105, 240))

picture_fith = pygame.image.load("square1.jpg")
picture_fith = pygame.transform.scale( picture, (110, 110))
rect_fith = picture_fith.get_rect()
rect_fith = rect_fith.move((240, 240))

picture_six = picture
rect_six = picture_six.get_rect()
rect_six = rect_six.move((385, 240))

picture_seven = picture
rect_seven = picture_seven.get_rect()
rect_seven = rect_seven.move((100, 400))

picture_eight = picture
rect_eight = picture_eight.get_rect()
rect_eight = rect_eight.move((250, 400))

picture_nine = picture
rect_nine = picture_nine.get_rect()
rect_nine = rect_nine.move((400, 400))

X_image = pygame.image.load("Ximage.gif")
X_image = pygame.transform.scale(X_image, (110, 110))
rect_X = X_image.get_rect()

O_image = pygame.image.load("Oimage.gif")
O_image = pygame.transform.scale(O_image, (110, 110))
rect_O = O_image.get_rect()

rects = [rect, rect_second, rect_third,
        rect_fourth, rect_fith, rect_six,
        rect_seven, rect_eight, rect_nine]

images = [None for i in range(9)]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
screen.fill(screen_color)
font_name()
draw_line()
play_game()
