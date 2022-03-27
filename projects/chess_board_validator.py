'''Chess Dictionary Validator

In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard() that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can't be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.'''

board = {'1h': 'bking', '6c': 'wqueen',
         '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}


def is_valid_chessboard(board: dict):
    # check space (key)
    spaces = list(board.keys())
    for space in spaces:
        if not 1 <= int(space[0]) <= 8 or not 'a' <= space[1] <= 'h':
            return False

    # check pieces
    valid_title = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    vals = list(board.values())
    black = []
    white = []
    for val in vals:
        if val[0] == 'b':
            black.append(val)
        elif val[0] == 'w':
            white.append(val)
        else:
            return False
        
        if val[1:] not in valid_title:
            return False

    if len(black) > 16 or len(white) > 16 or \
        black.count('bking') != 1 or white.count('wking') != 1 or \
        black.count('bpawn') > 8 or white.count('wpawn') > 8:
        return False

    return True


print(is_valid_chessboard(board))