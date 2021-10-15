import pygame
import os
import sys
pygame.font.init()

WIDTH, HEIGHT, STATUS_HEIGHT = 500, 500, 100
WIN = pygame.display.set_mode((WIDTH, HEIGHT + STATUS_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

MARGIN = 30

# Font
FONT = pygame.font.SysFont('comicsans', 60)

# X and O images
X_IMAGE = pygame.image.load(os.path.join("Assets", "cross.png"))
O_IMAGE = pygame.image.load(os.path.join("Assets", "circle.png"))

# Global variables
winner = None
draw = None
turn = 'x'

board = [[None]*3, [None]*3, [None]*3]


def draw_board():
    WIN.fill(WHITE)

    # Drawing vertical lines
    pygame.draw.line(WIN, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pygame.draw.line(WIN, BLACK, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)

    # Drawing horizontal lines
    pygame.draw.line(WIN, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 8)
    pygame.draw.line(WIN, BLACK, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 8)

    draw_status()


def draw_status():
    # Filling status area
    WIN.fill(BLACK, (0, WIDTH, HEIGHT, STATUS_HEIGHT))

    # Writing winner or turn
    if winner is None:
        message = "Turn: " + turn.upper()
    else:
        message = winner.upper() + "won!"
    if draw:
        message = "Draw!"

    status_text = FONT.render(message, True, WHITE)
    WIN.blit(status_text, (20, HEIGHT + STATUS_HEIGHT / 2 - status_text.get_height() / 2))

    pygame.display.update()


def draw_xo(row, column):
    global board, turn

    pos_x, pos_y = None, None
    # Setting position x of image with margin
    if row == 1:
        pos_x = MARGIN
    if row == 2:
        pos_x = WIDTH / 3 + MARGIN
    if row == 3:
        pos_x = WIDTH / 3 * 2 + MARGIN

    # Setting position y of image with margin
    if column == 1:
        pos_y = MARGIN
    if column == 2:
        pos_y = HEIGHT / 3 + MARGIN
    if column == 3:
        pos_y = HEIGHT / 3 * 2 + MARGIN

    board[row-1][column-1] = turn

    if turn == 'x':
        # Pasting x image
        WIN.blit(X_IMAGE, (pos_y, pos_x))
        turn = 'o'
    elif turn == 'o':
        # Pasting o image
        WIN.blit(O_IMAGE, (pos_y, pos_x))
        turn = 'x'
    pygame.display.update()


def user_click():
    x, y = pygame.mouse.get_pos()

    # Get column from mouse position
    if x < WIDTH / 3:
        column = 1
    elif x < WIDTH / 3 * 2:
        column = 2
    elif x < WIDTH:
        column = 3
    else:
        column = None

    # Get row from mouse position
    if y < HEIGHT / 3:
        row = 1
    elif y < HEIGHT / 3 * 2:
        row = 2
    elif y < HEIGHT:
        row = 3
    else:
        row = None

    # Draw when mouse is in the correct position
    if row and column and board[row - 1][column - 1] is None:
        draw_xo(row, column)


def main():
    draw_board()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_click()
        draw_status()


if __name__ == "__main__":
    main()
