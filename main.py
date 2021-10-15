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
RED = (255, 0, 0)

MARGIN = 30
LINE_THICKNESS = 5

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
        message = winner.upper() + " won!"
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
        check_win()


def check_win():
    global board, winner, draw

    # Check rows and columns
    for line in range(0, 3):
        # Rows
        if board[line][0] == board[line][1] == board[line][2] is not None:
            winner = board[line][0]
            pygame.draw.line(WIN, RED,
                             (0, (line+1)*HEIGHT / 3 - HEIGHT / 6),
                             (WIDTH, (line+1)*HEIGHT / 3 - HEIGHT / 6),
                             LINE_THICKNESS)
            break
        # Columns
        elif board[0][line] == board[1][line] == board[2][line] is not None:
            winner = board[0][line]
            pygame.draw.line(WIN, RED,
                             ((line+1)*WIDTH / 3 - WIDTH / 6, 0),
                             ((line+1)*WIDTH / 3 - WIDTH / 6, HEIGHT),
                             LINE_THICKNESS)
            break

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] is not None:  # From left to right
        winner = board[0][0]
        pygame.draw.line(WIN, RED,
                         (0, 0),
                         (WIDTH, HEIGHT),
                         LINE_THICKNESS)
    elif board[0][2] == board[1][1] == board[2][0] is not None:  # From right to left
        winner = board[0][2]
        pygame.draw.line(WIN, RED,
                         (WIDTH, 0),
                         (0, HEIGHT),
                         LINE_THICKNESS)

    # Check if draw
    if all(all(row) for row in board) and winner is None:
        draw = True
        # pygame.draw.line(WIN, RED,
        #                  (WIDTH / 4, HEIGHT / 4),
        #                  (WIDTH - WIDTH / 4, HEIGHT - HEIGHT / 4),
        #                  LINE_THICKNESS)
        # pygame.draw.line(WIN, RED,
        #                  (WIDTH - WIDTH / 4, HEIGHT / 4),
        #                  (WIDTH / 4, HEIGHT - HEIGHT / 4),
        #                  LINE_THICKNESS)


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
