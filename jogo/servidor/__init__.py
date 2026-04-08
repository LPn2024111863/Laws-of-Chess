# Setup for White Pieces
from servidor.pieces.bishop import Bishop
from servidor.pieces.king import King
from servidor.pieces.knight import Knight
from servidor.pieces.pawn import Pawn
from servidor.pieces.queen import Queen
from servidor.pieces.rook import Rook

wpawn = Pawn("wP", "a2")
wpawn2 = Pawn("wP", "b2")
wpawn3 = Pawn("wP", "c2")
wpawn4 = Pawn("wP", "d2")
wpawn5 = Pawn("wP", "e2")
wpawn6 = Pawn("wP", "f2")
wpawn7 = Pawn("wP", "g2")
wpawn8 = Pawn("wP", "h2")
wking = King("wK", "e1")
wrook1 = Rook("wR", "a1")
wrook2 = Rook("wR", "h1")
wbishop1 = Bishop("wB", "f1")
wbishop2 = Bishop("wB", "c1")
wqueen = Queen("wQ", "d1")
wknight1 = Knight("wT", "b1")
wknight2 = Knight("wT", "g1")
DEFAULT_WHITE_BOARD_MAP = {
    "wP": [wpawn, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8],
    "wK": [wking],
    "wR": [wrook1, wrook2],
    "wB": [wbishop1, wbishop2],
    "wQ": [wqueen],
    "wT": [wknight1,wknight2]
}

# Setup for Black Pieces

bpawn = Pawn("bP", "a7")
bpawn2 = Pawn("bP", "b7")
bpawn3 = Pawn("bP", "c7")
bpawn4 = Pawn("bP", "d7")
bpawn5 = Pawn("bP", "e7")
bpawn6 = Pawn("bP", "f7")
bpawn7 = Pawn("bP", "g7")
bpawn8 = Pawn("bP", "h7")
bking = King("bK", "e8")
brook1 = Rook("bR", "a8")
brook2 = Rook("bR", "h8")
bbishop1 = Bishop("bB", "f8")
bbishop2 = Bishop("bB", "c8")
bqueen = Queen("bQ", "d8")
bknight1 = Knight("bT", "b8")
bknight2 = Knight("bT", "g8")
DEFAULT_BLACK_BOARD_MAP = {
    "bP": [bpawn, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8],
    "bK": [bking],
    "bR": [brook1, brook2],
    "bB": [bbishop1, bbishop2],
    "bQ": [bqueen],
    "bT": [bknight1,bknight2]
}

# Letter checker for board analysis
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#Commands
COMMAND_SIZE = 9
INT_SIZE = 8
END_OP = "stop     "
PLAY   = "play     " # client chooses to enter the queue to play
MOVE   = "move     " # it's the player's turn to play
WAIT   = "wait     " # it's the other player's turn
SELECT = "select   " # player decides to select something
EMPTY =  "empty    " # notifies if the square is empty
OPPO_COL = "oppo_col " # notifies if the piece that is trying to move it's not theirs
VALID_SQUARE = "valid_sqr" # valid square with a piece to move
INVALID_COMMAND = "invalid  " # notifies if the command wasn't a valid one
CHECK = "check    " # notifies the player is in check
CHECKMATE = "checkmate" # notifies that the game has come to a checkmate
STALEMATE = "stalemate" # notifies that the game has come to a stalemate
CARDS = "cards    " # allows the player to select cards
NORMALTURN = "normturn " # hidden value that notifies a normal turn
CARDMINIGAME = "cardmgame" # hidden value that notifies a turn with a card minigame
GESTOR_ID = "gestor_id" # identifies the connection as a GESTOR
CLIENTE_ID = "clienteid" # identifies the connection as a CLIENT
LOGIN = "login    " # allows the client to log in
ACTIVE = "active   "
PORT = 35000
SERVER_ADDRESS = "localhost"


