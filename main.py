import pew
import random
import time


ALL_ON = pew.Pix.from_iter([[3 for i in range(8)] for j in range(8)])
ALL_OFF = pew.Pix.from_iter([[0 for i in range(8)] for j in range(8)])


def neighbors(cell):
    """
    Yields neighbours of cell.
    """
    x, y = cell
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x - 1, y + 1
    yield x - 1, y - 1


def advance(board):
    """
    Advance to next generation in Conway's Game of Life.
    """
    new_board = set()
    for cell in ((x, y) for x in range(8) for y in range(8)):
        count = sum((neigh in board) for neigh in neighbors(cell))
        if count == 3 or (count == 2 and cell in board):
            new_board.add(cell)
    return new_board, new_board == board


def generate_board():
    """
    Returns random board.
    """
    board = set()
    for x in range(8):
        for y in range(8):
            if random.randint(0, 1):
                board.add((x, y))
    return board


def board_to_pix(board):
    """
    Returns board converted to pew.Pix.
    """
    pix = pew.Pix()
    for x, y in board:
        pix.pixel(x, y, 3)
    return pix


def restart_animation():
    """
    Shows restart animation on display.
    """
    pew.show(ALL_ON)
    time.sleep(1)
    pew.show(ALL_OFF)
    time.sleep(0.5)


if __name__ == "__main__":
    pew.init()

    board, still_life = None, False

    while True:
        # init or restart of the game
        if still_life or not board:
            board = generate_board()
            restart_animation()
            pew.show(board_to_pix(board))

        time.sleep(0.5)
        # advance to next generation
        board, still_life = advance(board)
        pew.show(board_to_pix(board))

        # finish dead
        if not board:
            time.sleep(1.5)

        # finish still
        if still_life:
            time.sleep(3)
