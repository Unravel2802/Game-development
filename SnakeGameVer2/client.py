import pygame, time
from network import Network
snake1 = []
snake2 = []
width = 800
height = 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
effect = 0
speed = 20
size = 20


pygame.init()


def puttext(surf, pos, text, font, size, color, flag):
    fontrend = pygame.font.Font(font, size)
    textrend = fontrend.render(text, True, color)
    if flag == "center":
        textpos = textrend.get_rect()
        textpos = (int(width / 2 - textrend.get_rect().width / 2), int(height / 2 - textrend.get_rect().height / 2))
    elif flag == "left":
        textpos = (surf.get_rect().left + 2, surf.get_rect().top)
    elif flag == "right":
        textpos = (surf.get_rect().right - textrend.get_rect().width - 2, surf.get_rect().top)
    else:
        textpos = pos
    surf.blit(textrend, textpos)


def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))
    player.draw(win)
    player2.draw(win)
    player.Food(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(10)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if (p.getLen() > 2 and p.check_tail_collision()) or p.check_border_collision(width, height):
            print("Your score is: " + str(p.getLen()-1))
            print("The other player score is: " + str(p2.getLen()-1))
            if p.getLen() > p2.getLen():
                print("You win")
            elif p2.getLen() > p.getLen():
                print("The other player wins")
            else:
                print("Draw")
            run = False
            exit()

        elif (p2.getLen() > 2 and p2.check_tail_collision()) or p2.check_border_collision(width, height):
            print("Your score is: " + str(p.getLen()-1))
            print("The other player score is: " + str(p2.getLen()-1))
            if p.getLen() > p2.getLen():
                print("You win")
            elif p2.getLen() > p.getLen():
                print("The other player wins")
            else:
                print("Draw")
            run = False
            exit()


        if p.getHead() == p2.getHead():
            print("Oops, you guys have faced head to head! Whoever has more score will win")
            if p.getLen() > p2.getLen():
                print("You win")
            elif p2.getLen() > p.getLen():
                print("The other player wins")
            else:
                print("Draw")
            quit()

        elif p.getHead() != p2.getHead():
            for i in range(p2.getLen()-1):
                segment = p2.parts[i]
                if p.getHead() == segment:
                    print("Oops, you got into the other player, you lose!")
                    quit()
            for i in range(p.getLen()-1):
                segment = p.parts[i]
                if p2.getHead() == segment:
                    print("Oops, the other player got into you, you win!")
                    quit()
        p.move()
        redrawWindow(win, p, p2)

main()
