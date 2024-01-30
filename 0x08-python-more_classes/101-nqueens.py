#!/usr/bin/python3
"""Solving the N-queens problem.


Attributes are slate (list): A list of lists (chessboard).
    pack (list): A list of lists - solved puzzle.
"""
import sys


def init_slate(n):
    """Here, we initialize a chessboard with 0's."""
    slate = []
    [slate.append([]) for y in range(n)]
    [row.append(' ') for y in range(n) for row in slate]
    return (slate)


def copy_slate(slate):
    """We return a replic of a chessboard."""
    if isinstance(slate, list):
        return list(map(copy_slate, slate))
    return (slate)


def puzzled(slate):
    """We return solved task as list of lists."""
    pack = []
    for w in range(len(slate)):
        for x in range(len(slate)):
            if slate[w][x] == "Q":
                pack.append([w, x])
                break
    return (pack)


def strike(slate, row, col):
    """check chessboard blocks for non attacking queens.

    Arguments are slate (list) for chessboard,
        row (int) row of queen last spot and
        col (int) column of queen last spot.
    """
    for x in range(col + 1, len(slate)):
        slate[row][x] = "x"
    
    for x in range(col - 1, -1, -1):
        slate[row][x] = "x"

    for w in range(row + 1, len(slate)):
        slate[w][col] = "x"
    
    for w in range(row - 1, -1, -1):
        slate[w][col] = "x"
    
    x = col + 1
    for w in range(row + 1, len(slate)):
        if x >= len(slate):
            break
        slate[w][x] = "x"
        x += 1
    
    x = col - 1
    for w in range(row - 1, -1, -1):
        if x < 0:
            break
        slate[w][x]
        x -= 1
    
    x = col + 1
    for w in range(row - 1, -1, -1):
        if x >= len(slate):
            break
        slate[w][x] = "x"
        x += 1
    
    x = col - 1
    for w in range(row + 1, len(slate)):
        if x < 0:
            break
        slate[w][x] = "x"
        x -= 1


def runner(slate, row, queens, packs):
    """Staging the solving of the puzzle N-queens.

    Arguments are slate (list) the chessboard,
        row (int) - the row,
        queens (int) - the queens,
        packs (list) - list of lists of solved puzzle.
    Will return solutions
    """
    if queens == len(slate):
        packs.append(puzzled(slate))
        return (packs)

    for x in range(len(slate)):
        if slate[row][x] == " ":
            mom_slate = copy_slate(slate)
            mom_slate[row][x] = "Q"
            strike(mom_slate, row, x)
            packs = runner(mom_slate, row + 1, queens + 1, packs)

    return (packs)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    slate = init_slate(int(sys.argv[1]))
    packs = runner(slate, 0, 0, [])
    for out in packs:
        print(out)
