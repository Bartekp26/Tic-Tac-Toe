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

# Font
FONT = pygame.font.SysFont('comicsans', 60)

# X and O images
X_IMAGE = pygame.image.load(os.path.join("Assets", "cross.png"))
O_IMAGE = pygame.image.load(os.path.join("Assets", "circle.png"))

# Global variables
winner = None
draw = None
turn = 'x'


def draw_board():
    WIN.fill(WHITE)

    # Drawing vertical lines
    pygame.draw.line(WIN, BLACK, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pygame.draw.line(WIN, BLACK, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)

    # Drawing horizontal lines
    pygame.draw.line(WIN, BLACK, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 8)
    pygame.draw.line(WIN, BLACK, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 8)


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


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board()
        draw_status()
        pygame.display.update()


if __name__ == "__main__":
    main()
