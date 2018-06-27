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

        self.movingI = -1
        self.movingJ = -1

        self.frameSurface = pygame.transform.scale(pygame.image.load("img/frame.png").convert_alpha(), (int(dimm[0]/8), int(dimm[1]/8)))
        self.circleSurface = pygame.transform.scale(pygame.image.load("img/point.png").convert_alpha(), (int(dimm[0]/32), int(dimm[1]/32)))
        self.greenSquare = pygame.Surface((int(dimm[0]/8), int(dimm[1]/8)))
        self.greenSquare.fill((119, 149, 86))
        self.yellowSquare = pygame.Surface((int(dimm[0]/8), int(dimm[1]/8)))
        self.yellowSquare.fill((235, 236, 208))

        self.pieceSurfaces[0].set_alpha(0)
        self.circleSurface.set_alpha(70)
        self.grid = [[[0, Pieces.NONE, 0] for x in range(8)] for y in range(8)]
        for i in range(0,8):
            for j in range(0,8):
                if (i+j)%2 == 0:
                    self.grid[i][j][0] = 1

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

    def possibleMove(self, i, j, team):
        if (i >= 8 or i < 0 or j >= 8 or j < 0):
             return False
        if (self.grid[i][j][1].value >= 1 and self.grid[i][j][1].value <= 6 and not team) or (self.grid[i][j][1].value > 6 and team):
            return False
        return True

    def calculatePossibleMoves(self, i, j, team):
        if self.grid[i][j][1].value == 1 or self.grid[i][j][1].value == 7:
            if self.possibleMove(i+1, j, team ):
                self.mark(i+1, j)
            if self.possibleMove(i+1, j+1, team ):
                self.mark(i+1, j+1)
            if self.possibleMove(i, j+1, team ):
                self.mark(i,j+1)
            if self.possibleMove(i-1, j+1, team ):
                self.mark(i-1,j+1)
            if self.possibleMove(i+1, j-1, team ):
                self.mark(i+1,j-1)
            if self.possibleMove(i, j-1, team ):
                self.mark(i, j-1)
            if self.possibleMove(i-1, j, team ):
                self.mark(i-1,j)
            if self.possibleMove(i-1, j-1, team ):
                self.mark(i-1,j-1)
        elif self.grid[i][j][1].value == 2 or self.grid[i][j][1].value == 8:
            self.evaluateIrect(i, j, team)
            self.evaluateJrect(i, j, team)
            self.evaluateInegrect(i, j, team)
            self.evaluateJnegrect(i, j, team)
            self.evaluateIJdiag(i , j, team)
            self.evaluateInegJdiag(i, j, team)
            self.evaluateIJnegdiag(i, j, team)
            self.evaluateInegJnegdiag(i, j, team)
        elif self.grid[i][j][1].value == 3 or self.grid[i][j][1].value == 9:
            self.evaluateIrect(i, j, team)
            self.evaluateInegrect(i, j, team)
            self.evaluateJrect(i, j, team)
            self.evaluateJnegrect(i, j, team)
        elif self.grid[i][j][1].value == 4 or self.grid[i][j][1].value == 10:
            self.evaluateIJdiag(i, j, team)
            self.evaluateInegJdiag(i, j, team)
            self.evaluateInegJnegdiag(i, j, team)
            self.evaluateIJnegdiag(i, j, team)
        elif self.grid[i][j][1].value == 5 or self.grid[i][j][1].value == 11:
            if self.possibleMove(i+2, j+1, team):
                self.mark(i+2, j+1)
            if self.possibleMove(i+2, j-1, team):
                self.mark(i+2, j-1)
            if self.possibleMove(i-2, j+1, team):
                self.mark(i-2, j+1)
            if self.possibleMove(i-2, j-1, team):
                self.mark(i-2, j-1)
            if self.possibleMove(i+1, j+2, team):
                self.mark(i+1, j+2)
            if self.possibleMove(i-1, j+2, team):
                self.mark(i-1, j+2)
            if self.possibleMove(i+1, j-2, team):
                self.mark(i+1, j-2)
            if self.possibleMove(i-1, j-2, team):
                self.mark(i-1, j-2)
        elif self.grid[i][j][1].value == 6:
            can_move_second = False
            if self.empty(i, j-1):
                can_move_second = True
                self.mark(i, j-1)
            if self.grid[i-1][j-1][1].value > 6:
                self.mark(i-1, j-1)
            if self.grid[i+1][j-1][1].value > 6:
                self.mark(i+1, j-1)
            if j == 6 and can_move_second:
                if self.empty(i, j-2):
                    self.mark(i, j-2)
        elif self.grid[i][j][1].value == 12:
            can_move_second = False
            if self.empty(i, j+1):
                can_move_second = True
                self.mark(i, j+1)
            if self.grid[i-1][j+1][1].value <= 6 and self.grid[i-1][j+1][1].value > 0:
                self.mark(i-1, j+1)
            if self.grid[i+1][j+1][1].value <= 6 and self.grid[i+1][j+1][1].value > 0:
                self.mark(i+1, j+1)
            if j == 1 and can_move_second:
                if self.empty(i, j+2):
                    self.mark(i, j+2)

    def evaluateIrect(self, i, j, team):
        b = True
        while b:
            i+=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False

    def evaluateInegrect(self,i, j, team):
        b = True
        while b:
            i-=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False

    def evaluateJrect(self,i, j, team):
        b = True
        while b:
            j+=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def evaluateJnegrect(self,i, j, team):
        b = True
        while b:
            j-=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def evaluateIJdiag(self,i, j, team):
        b = True
        while b:
            j+=1
            i+=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def evaluateIJnegdiag(self,i, j, team):
        b = True
        while b:
            j-=1
            i+=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def evaluateInegJdiag(self,i,j, team):
        b = True
        while b:
            j+=1
            i-=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def evaluateInegJnegdiag(self,i,j, team):
        b = True
        while b:
            j-=1
            i-=1
            if self.possibleMove(i, j, team):
                self.mark(i, j)
                if self.grid[i][j][1].value > 0:
                    b = False
            else:
                b = False
    def click(self, i, j):
        if ((not self.turn and self.grid[i][j][1].value >= 1 and self.grid[i][j][1].value <= 6) or (self.turn and self.grid[i][j][1].value > 6)) and not self.moving:
            self.grid[i][j][2] = 1
            self.calculatePossibleMoves(i, j, self.turn)
            self.moving = True
            self.movingI = i
            self.movingJ = j
        elif self.grid[i][j][2] > 0 and self.moving and (self.movingI, self.movingJ) != (i, j):
            self.grid[i][j][1] = self.grid[self.movingI][self.movingJ][1]
            self.grid[self.movingI][self.movingJ][1] = Pieces.NONE
            self.movingI = -1
            self.movingJ = -1
            self.moving = False
            self.turn = not self.turn
            self.clear_board_markers()
        else:
            self.movingI = -1
            self.movingJ = -1
            self.moving = False
            self.clear_board_markers()


    def mark(self, i, j):
        if self.grid[i][j][1].value == 0:
            self.grid[i][j][2] = 2
        else:
            self.grid[i][j][2] = 1
    def empty(self, i, j):
        if i > 7 or i < 0 or j < 0 or j > 7: return False
        if self.grid[i][j][1].value == 0:
            return True
        return False
    def clear_board_markers(self):
        for i in self.grid:
            for elem in i:
                elem[2] = 0
