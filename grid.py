import pygame
from pygame.locals import *
from pieces import Pieces
class Map():
    def __init__(self, dimm):
        super().__init__()
        self.turn = False #false = white turn  true black turn
        self.moving = False
        self.pieceSurfaces = [
            pygame.Surface((1,1)),
            pygame.transform.scale(pygame.image.load("img/whiteKing.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/whiteQueen.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/whiteRook.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/whiteBishop.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/whiteKnight.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/whitePawn.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackKing.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackQueen.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackRook.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackBishop.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackKnight.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8))),
            pygame.transform.scale(pygame.image.load("img/blackPawn.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8)))

        ]

        self.frameSurface = pygame.transform.scale(pygame.image.load("img/frame.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8)))
        self.circleSurface = pygame.transform.scale(pygame.image.load("img/point.png").convert_alpha(), (int(dimm[0]/32), int(dimm[1]/32)))
        pygame.draw.circle(self.circleSurface, (22,23,23), (25,25), 10, 0)
        self.pieceSurfaces[0].set_alpha(0)
        self.circleSurface.set_alpha(70)
        self.grid = [[[pygame.Surface((int(dimm[0]/8), int(dimm[1]/8))), Pieces.NONE, 0] for x in range(8)] for y in range(8)]
        for i in range(0,8):
            for j in range(0,8):
                if (i+j)%2 == 0:
                    self.grid[i][j][0].fill((235, 236, 208))
                else:
                    self.grid[i][j][0].fill((119, 149, 86))
        self.grid[0][6][1] = Pieces.W_PAWN
        self.grid[1][6][1] = Pieces.W_PAWN
        self.grid[2][6][1] = Pieces.W_PAWN
        self.grid[3][6][1] = Pieces.W_PAWN
        self.grid[4][6][1] = Pieces.W_PAWN
        self.grid[5][6][1] = Pieces.W_PAWN
        self.grid[6][6][1] = Pieces.W_PAWN
        self.grid[7][6][1] = Pieces.W_PAWN

        self.grid[0][1][1] = Pieces.B_PAWN
        self.grid[1][1][1] = Pieces.B_PAWN
        self.grid[2][1][1] = Pieces.B_PAWN
        self.grid[3][1][1] = Pieces.B_PAWN
        self.grid[4][1][1] = Pieces.B_PAWN
        self.grid[5][1][1] = Pieces.B_PAWN
        self.grid[6][1][1] = Pieces.B_PAWN
        self.grid[7][1][1] = Pieces.B_PAWN

        self.grid[0][7][1] = Pieces.W_ROOK
        self.grid[1][7][1] = Pieces.W_KNIGHT
        self.grid[2][7][1] = Pieces.W_BISHOP
        self.grid[3][7][1] = Pieces.W_QUEEN
        self.grid[4][7][1] = Pieces.W_KING
        self.grid[5][7][1] = Pieces.W_BISHOP
        self.grid[6][7][1] = Pieces.W_KNIGHT
        self.grid[7][7][1] = Pieces.W_ROOK

        self.grid[0][0][1] = Pieces.B_ROOK
        self.grid[1][0][1] = Pieces.B_KNIGHT
        self.grid[2][0][1] = Pieces.B_BISHOP
        self.grid[3][0][1] = Pieces.B_QUEEN
        self.grid[4][0][1] = Pieces.B_KING
        self.grid[5][0][1] = Pieces.B_BISHOP
        self.grid[6][0][1] = Pieces.B_KNIGHT
        self.grid[7][0][1] = Pieces.B_ROOK

    def mark(self, i, j):
        self.grid[i][j][2] = 2

        if not self.turn and self.grid[i][j][1].value >= 1 and self.grid[i][j][1].value <= 6 and not self.moving:
            self.grid[i][j][2] = 2
            #calculatePossibleMoves(i, j)

    def calculatePossibleMoves(self, i, j):
        if self.grid[i][j][1].value == 1 or self.grid[i][j][1].value == 7:
            pass
        pass
