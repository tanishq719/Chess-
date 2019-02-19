#   ************************************************************************************
#                      ***********BLACK SIDE**************
#           Rook  Knight  Bishop   Queen   King   Bishop  Knight   Rook
#            a      b       c       d       e       f       g       h
#        |---------------------------------------------------------------|
#     8  |   0   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |
#        |---------------------------------------------------------------|
#     7  |   8   |   9   |   A   |   B   |   C   |   D   |   E   |   F   |
#        |---------------------------------------------------------------|
#     6  |       |   +   |       |   +   |       |   +   |       |   +   |
#        |---------------------------------------------------------------|
#     5  |   +   |       |   +   |       |   +   |       |   +   |       |
#        |---------------------------------------------------------------|
#     4  |       |   +   |       |   +   |       |   +   |       |   +   |
#        |---------------------------------------------------------------|
#     3  |   +   |       |   +   |       |   +   |       |   +   |       |
#        |---------------------------------------------------------------|
#     2  |   F   |   E   |   D   |   C   |   B   |   A   |   9   |   8   |
#        |---------------------------------------------------------------|
#     1  |   7   |   6   |   5   |   4   |   3   |   2   |   1   |   0   |
#        |---------------------------------------------------------------|
#            a      b       c       d       e       f       g       h
#           Rook  Knight  Bishop   Queen   King   Bishop  Knight   Rook
#                        *********WHITE SIDE***********
#   ***************************************************************************************


class HashElement:

    def __init__(self):
        self.i = 0
        self.wpos_x, self.wpos_y = 'e', 'e'     # here w = (wpos_x, wpos_y) and b = (bpos_x, bpos_y)
        self.bpos_x, self.bpos_y = 'e', 'e'     # here w and b stands for white and black respectively
        # following structure is not needed therefore we made it only for explaination purpose
        # self.w = [self.wpos_x, self.wpos_y]
        # self.b = [self.bpos_x, self.bpos_y]
        # self.piece = [self.w, self.b]


# here we required hash table for searching the positions of different pieces of chessBoard

class Hash:


    p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16 = [HashElement() for i in range(1,17)]

    # here [('e','e'),('e','e')] is for [ white_pieces( pos_x, pos_y ), black_pieces( pos_x, pos_y )]

    _hash = {'F': p1,'E': p2, 'D': p3, 'C': p4, 'B': p5,'A': p6, '9': p7,'8': p8, '7': p9, '6': p10, '5': p11, '4': p12, '3': p13, '2': p14, '1': p15,'0': p16 }

# this class will form the chess board array

class ChessBoard(Hash):

    row8 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row7 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row6 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row5 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row4 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row3 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row2 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']
    row1 = ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']

    # to keep the colomn of the virtual matrix of 8x8

    clmn = {'1': row1, '2': row2, '3': row3, '4': row4,
            '5': row5, '6': row6, '7': row7, '8': row8}

    # color will give the color of the piece being handeled AND
    # value is the hexadecimal equivalent of chess pieces
    # insert_value() inserts the positions in chess board matrix and in hash table 'hash'
    @classmethod
    def insert_value(cls, color, value, pos_x, pos_y):

        if color is None:
            cls.clmn.get(pos_y)[ord(pos_x) - 65] = 'e'
            # here we have not put empty in hash table as there can be only one position associated with a piece
            # which is not same in chess board matrix

        else:
            cls.clmn.get(pos_y)[ord(pos_x) - 65] = color
            cls.clmn.get(pos_y)[ord(pos_x) - 65] += value
            # here value in its original form mean by hexadecimal equivalent of pieces
            # but as they are being passed in the dictionary 'Hash' they are treated as Key for the dictionary
            if color is 'W':
                cls._hash.get(value).wpos_x = pos_x
                cls._hash.get(value).wpos_y = pos_y

            elif color is 'B':
                cls._hash.get(value).bpos_x = pos_x
                cls._hash.get(value).bpos_y = pos_y

    # this function find the present position of the chess pieces by searching from the hash table
    @classmethod
    def find_present_pos(cls, color, value):

        if color is 'W':
            return cls._hash.get(value).wpos_x, cls._hash.get(value).wpos_y
        elif color is 'B':
            return cls._hash.get(value).bpos_x, cls._hash.get(value).bpos_y

    # this function stores move made either by opponent or by computer
    @classmethod
    def store_move(cls, color, value, pos_x, pos_y):

        Pos_x, Pos_y = cls.find_present_pos(color, value)
        cls.insert_value(color, value, pos_x, pos_y)
        cls.insert_value(None, value, Pos_x, Pos_y)

    @classmethod
    def initialize_board(cls):
        cls.insert_value('W', '0', 'H', '1')
        cls.insert_value('W', '1', 'G', '1')
        cls.insert_value('W', '2', 'F', '1')
        cls.insert_value('W', '3', 'E', '1')
        cls.insert_value('W', '4', 'D', '1')
        cls.insert_value('W', '5', 'C', '1')
        cls.insert_value('W', '6', 'B', '1')
        cls.insert_value('W', '7', 'A', '1')
        cls.insert_value('W', '8', 'H', '2')
        cls.insert_value('W', '9', 'G', '2')
        cls.insert_value('W', 'A', 'F', '2')
        cls.insert_value('W', 'B', 'E', '2')
        cls.insert_value('W', 'C', 'D', '2')
        cls.insert_value('W', 'D', 'C', '2')
        cls.insert_value('W', 'E', 'B', '2')
        cls.insert_value('W', 'F', 'A', '2')
        cls.insert_value('B', '0', 'A', '8')
        cls.insert_value('B', '1', 'B', '8')
        cls.insert_value('B', '2', 'C', '8')
        cls.insert_value('B', '3', 'D', '8')
        cls.insert_value('B', '4', 'E', '8')
        cls.insert_value('B', '5', 'F', '8')
        cls.insert_value('B', '6', 'G', '8')
        cls.insert_value('B', '7', 'H', '8')
        cls.insert_value('B', '8', 'A', '7')
        cls.insert_value('B', '9', 'B', '7')
        cls.insert_value('B', 'A', 'C', '7')
        cls.insert_value('B', 'B', 'D', '7')
        cls.insert_value('B', 'C', 'E', '7')
        cls.insert_value('B', 'D', 'F', '7')
        cls.insert_value('B', 'E', 'G', '7')
        cls.insert_value('B', 'F', 'H', '7')

    # here color refers to the color choosed by the user

    @classmethod
    def print_matrix(cls, color):
        if color is 'W':
            for i in range(17, 0, -1):
                if i % 2 is 1 :
                    for j in range(0, 81):
                        if (i == 17 and j == 0) or (i == 17 and j == 80) or (i == 1 and j == 0) or (i == 1 and j == 80):
                            print("+",end = "")
                        else:
                            print("-",end = "")
                    print()
                else:
                    for j in range(0, 9):
                        if j is not 8:  # for the last placeholder

                            block = cls.clmn.get(str(i // 2))[j]
                            if block is 'e':

                                if not ((i//2 + j) % 2) :
                                    print("|    {}   ".format('+'),end = " ")
                                else:
                                    print("|        ", end=" ")

                            else:
                                print("|   {}   ".format(block), end=" ")

                        else:

                            print("|",end = "")

                    print()
        if color is 'B':
            for i in range(0, 17):
                if i % 2 is not 1 :
                    for j in range(0, 81):
                        if (i == 0 and j == 0) or (i == 0 and j == 80) or (i == 16 and j == 0) or (i == 16 and j == 80):
                            print("+",end = "")
                        else:
                            print("-",end = "")
                    print()
                else:
                    for j in range(7, -2, -1):
                        if j is not -1:  # for the last placeholder

                            block = cls.clmn.get(str((i // 2)+1))[j]
                            if block is 'e':

                                if not ((i//2 + j) % 2) :
                                    print("|    {}   ".format('+'),end = " ")
                                else:
                                    print("|        ", end=" ")

                            else:
                                print("|   {}   ".format(block), end=" ")

                        else:

                            print("|",end = "")

                    print()

class King(ChessBoard):

    def __init__(self, color):
        self.initialize_board()
        self.color = color
        self.pace = 1
        self.direct = [1, 2, 3, 4, 5, 6, 7, 8]
        # these are direction conventions
        #          2  1  8
        #           \ | /
        #            \|/
        #         3-------7
        #            /|\
        #           / | \
        #          4  5  6
        # these direction does not have any dependancy on the move taken by specific color
    def make_move(self, direct):

        if self.color is 'B':
            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, '4')
            if direct is 1:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y)-self.pace)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x)+self.pace)
                self.pos_y = str(int(self.pos_y)-self.pace)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x)+self.pace)
                self.pos_y = self.pos_y
            elif direct is 4:
                self.pos_x = chr(ord(self.pos_x)+self.pace)
                self.pos_y = str(int(self.pos_y)+self.pace)
            elif direct is 5:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y)+self.pace)
            elif direct is 6:
                self.pos_x = chr(ord(self.pos_x)-self.pace)
                self.pos_y = str(int(self.pos_y)+self.pace)
            elif direct is 7:
                self.pos_x = chr(ord(self.pos_x) - self.pace)
                self.pos_y = self.pos_y
            elif direct is 8:
                self.pos_x = chr(ord(self.pos_x) - self.pace)
                self.pos_y = str(int(self.pos_y) - self.pace)

            # the below condition checks that whether there is a already a piece of same color
            # or there is a wall which blocks the piece on the positions of x and y
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'B'):
                print("invalid move!!!")
            else:
                self.store_move('B', '4', self.pos_x, self.pos_y)
        else:
            self.pos_x, self.pos_y = self.find_present_pos(self.color, '3')
            if direct is 1:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y) + self.pace)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x) - self.pace)
                self.pos_y = str(int(self.pos_y)+self.pace)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x)-self.pace)
                self.pos_y = self.pos_y
            elif direct is 4:
                self.pos_x = chr(ord(self.pos_x)-self.pace)
                self.pos_y = str(int(self.pos_y)-self.pace)
            elif direct is 5:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y) - self.pace)
            elif direct is 6:
                self.pos_x = chr(ord(self.pos_x) + self.pace)
                self.pos_y = str(int(self.pos_y) - self.pace)
            elif direct is 7:
                self.pos_x = chr(ord(self.pos_x) + self.pace)
                self.pos_y = self.pos_y
            elif direct is 8:
                self.pos_x = chr(ord(self.pos_x) + self.pace)
                self.pos_y = str(int(self.pos_y) + self.pace)
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'W'):
                print("invalid move!!!")
            else:
                self.store_move('W', '3', self.pos_x, self.pos_y)

class Queen(ChessBoard):

    def __init__(self,color):
        self.color = color
        self.pace = 8
        # these are direction conventions
        #          2  1  8
        #           \ | /
        #            \|/
        #         3-------7
        #            /|\
        #           / | \
        #          4  5  6
    def make_move(self, direct, pace_length):
        self.pace = pace_length
        self.flag = 1
        if self.color is 'B':
            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, '3')
            if direct is 1:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y)-1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':   # this condition checks that whether there is a piece of same color or not
                        self.flag = 0                                               # is a piece of same color or not
                        print("invalid move!!!")

            elif direct is 2:
                for self.l in range(1, self.pace + 1):  # here 1 is taken instead of any pace because pos_x and pos_y are continueously being changed
                    self.pos_x = chr(ord(self.pos_x)+1)
                    self.pos_y = str(int(self.pos_y)-1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 3:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x)+1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 4:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x)+1)
                    self.pos_y = str(int(self.pos_y)+1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 5:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y)+1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 6:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x)-1)
                    self.pos_y = str(int(self.pos_y)+1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 7:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 8:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            # the below condition checks that whether there
            # is a wall which blocks the piece on the positions of x and y
            if ((ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9)) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('B', '3', self.pos_x, self.pos_y)
        else:
            self.pos_x, self.pos_y = self.find_present_pos(self.color, '4')
            if direct is 1:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 2:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y)+1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 3:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x)-1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 4:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x)-1)
                    self.pos_y = str(int(self.pos_y)-1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 5:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 6:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 7:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 8:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('W', '4', self.pos_x, self.pos_y)


class Bishop(ChessBoard):
    def __init__(self, color, side):
        self.color = color
        self.side = side
        self.pace = 8

        # these are direction conventions
        #          2     8
        #           \   /
        #            \ /
        #            / \
        #           /   \
        #          4     6
    def make_move(self, direct, pace_length):
        self.pace = pace_length
        self.flag = 1
        if self.side is 'L':  # here side simply mean by associativity of the piece with the king that is whether right or left
            self.piece_value = '5'
        elif self.side is 'R':
            self.piece_value = '2'

        if self.color is 'B':
            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, self.piece_value)
            if direct is 2:
                for self.l in range(1, self.pace + 1):  # here 1 is taken instead of any pace because pos_x and pos_y are continueously being changed
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 4:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 6:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 8:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            # the below condition checks that whether there
            # is a wall which blocks the piece on the positions of x and y
            if ((ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9)) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('B', self.piece_value, self.pos_x, self.pos_y)
        else:
            self.pos_x, self.pos_y = self.find_present_pos(self.color, self.piece_value)

            if direct is 2:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 4:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 6:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 8:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (
                    int(self.pos_y) is 9) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('W', self.piece_value, self.pos_x, self.pos_y)

class Knight(ChessBoard):
    def __init__(self, color, side):
        self.color = color
        self.side = side
        self.pace = 2.5

    # the directions are as follow
    #           1---++---8
    #        2      ||      7
    #        |      ||      |
    #        +------  ------+
    #        +------  ------+
    #        |      ||      |
    #        3      ||      6
    #           4---++---5

    def make_move(self, direct):
        if self.side is 'L':
            self.piece_value = '6'
        elif self.side is 'R':
            self.piece_value = '1'

        if self.color is 'B':

            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, self.piece_value)
            if direct is 1:
                self.pos_x = chr(ord(self.pos_x) + 1)
                self.pos_y = str(int(self.pos_y) - 2)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x)+2)
                self.pos_y = str(int(self.pos_y)-1)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x)+2)
                self.pos_y = str(int(self.pos_y)+1)
            elif direct is 4:
                self.pos_x = chr(ord(self.pos_x)+1)
                self.pos_y = str(int(self.pos_y)+2)
            elif direct is 5:
                self.pos_x = chr(ord(self.pos_x)-1)
                self.pos_y = str(int(self.pos_y)+2)
            elif direct is 6:
                self.pos_x = chr(ord(self.pos_x)-2)
                self.pos_y = str(int(self.pos_y)+1)
            elif direct is 7:
                self.pos_x = chr(ord(self.pos_x)-2)
                self.pos_y = str(int(self.pos_y)-1)
            elif direct is 8:
                self.pos_x = chr(ord(self.pos_x) - 1)
                self.pos_y = str(int(self.pos_y) - 2)

            # the below condition checks that whether there is a already a piece of same color
            # or there is a wall which blocks the piece on the positions of x and y
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'B'):
                print("invalid move!!!")
            else:
                self.store_move('B', self.piece_value, self.pos_x, self.pos_y)

        else:

            self.pos_x, self.pos_y = self.find_present_pos(self.color, piece_value)
            if direct is 1:
                self.pos_x = chr(ord(self.pos_x) - 1)
                self.pos_y = str(int(self.pos_y) + 2)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x) - 2)
                self.pos_y = str(int(self.pos_y)+1)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x)-2)
                self.pos_y = str(int(self.pos_y)-1)
            elif direct is 4:
                self.pos_x = chr(ord(self.pos_x)-1)
                self.pos_y = str(int(self.pos_y)-2)
            elif direct is 5:
                self.pos_x = chr(ord(self.pos_x)+1)
                self.pos_y = str(int(self.pos_y)-2)
            elif direct is 6:
                self.pos_x = chr(ord(self.pos_x) + 2)
                self.pos_y = str(int(self.pos_y) - 1)
            elif direct is 7:
                self.pos_x = chr(ord(self.pos_x) + 2)
                self.pos_y = str(int(self.pos_y) + 1)
            elif direct is 8:
                self.pos_x = chr(ord(self.pos_x) + 1)
                self.pos_y = str(int(self.pos_y) + 2)
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'W'):
                print("invalid move!!!")
            else:
                self.store_move('W', self.piece_value, self.pos_x, self.pos_y)


class Rook(ChessBoard):
    def __init__(self, color, side):
        self.color = color
        self.side = side
        self.pace = 8

        # these are direction conventions
        #             1
        #             |
        #             |
        #         3-------7
        #             |
        #             |
        #             5

    def make_move(self, direct, pace_length):
        self.pace = pace_length
        if self.side is 'L':
            self.piece_value = '7'
        elif self.side is 'R':
            self.piece_value = '0'
        self.flag = 1

        if self.color is 'B':

            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, self.piece_value)

            if direct is 1:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':  # this condition checks that whether there is a piece of same color or not
                        self.flag = 0  # is a piece of same color or not
                        print("invalid move!!!")

            elif direct is 3:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 5:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 7:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'B':
                        self.flag = 0
                        print("invalid move!!!")

            # the below condition checks that whether there
            # is a wall which blocks the piece on the positions of x and y

            if ((ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (
                    int(self.pos_y) is 9)) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('B', self.piece_value, self.pos_x, self.pos_y)

        else:

            self.pos_x, self.pos_y = self.find_present_pos(self.color, self.piece_value)

            if direct is 1:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) + 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 3:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) - 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 5:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = self.pos_x
                    self.pos_y = str(int(self.pos_y) - 1)
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            elif direct is 7:
                for self.l in range(1, self.pace + 1):
                    self.pos_x = chr(ord(self.pos_x) + 1)
                    self.pos_y = self.pos_y
                    if self.clmn.get(self.pos_y)[ord(self.pos_x) - 65][0] is 'W':
                        self.flag = 0
                        print("invalid move!!!")

            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) and self.flag:
                print("invalid move!!!")
            elif self.flag:
                self.store_move('W', self.piece_value, self.pos_x, self.pos_y)

class Pawn(ChessBoard):
    def __init__(self, color, piece_value):
        self.color = color
        self.piece_value = piece_value
        self.pace = 1

    # these are direction conventions
    #          2  1  3
    #           \ | /
    #            \|/

    def make_move(self, direct):
        if self.color is 'B':

            self.pos_x, self.pos_y = ChessBoard.find_present_pos(self.color, self.piece_value)
            if direct is 1:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y)-self.pace)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x)+self.pace)
                self.pos_y = str(int(self.pos_y)-self.pace)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x)-self.pace)
                self.pos_y = str(int(self.pos_y) - self.pace)
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'B'):
                print("invalid move!!!")
            else:
                self.store_move('B', self.piece_value, self.pos_x, self.pos_y)

        else:

            self.pos_x, self.pos_y = self.find_present_pos(self.color, self.piece_value)
            if direct is 1:
                self.pos_x = self.pos_x
                self.pos_y = str(int(self.pos_y) + self.pace)
            elif direct is 2:
                self.pos_x = chr(ord(self.pos_x) - self.pace)
                self.pos_y = str(int(self.pos_y) + self.pace)
            elif direct is 3:
                self.pos_x = chr(ord(self.pos_x) + self.pace)
                self.pos_y = str(int(self.pos_y) + self.pace)
            if (ord(self.pos_x) == 64) or (ord(self.pos_x) == 73) or (int(self.pos_y) is 0) or (int(self.pos_y) is 9) or (self.clmn.get(self.pos_y)[ord(self.pos_x)-65][0] is 'B'):
                print("invalid move!!!")
            else:
                self.store_move('W', self.piece_value, self.pos_x, self.pos_y)

class Game:

    def __init__(self):
        self.kingB = King(color = 'B')
        self.kingW = King(color = 'W')
        self.queenB = Queen(color = 'B')
        self.queenW = Queen(color = 'W')
        self.rookBL = Rook(color = 'B', side = 'L')
        self.rookBR = Rook(color='B', side='R')
        self.rookWL = Rook(color='W', side='L')
        self.rookWR = Rook(color='W', side='R')
        self.knightBL = Knight(color='B', side='L')
        self.knightBR = Knight(color='B', side='R')
        self.knightWL = Knight(color='W', side='L')
        self.knightWR = Knight(color = 'W', side = 'R')
        self.bishopBL = Bishop(color = 'B', side = 'L')
        self.bishopBR = Bishop(color='B', side='R')
        self.bishopWL = Bishop(color='W', side='L')
        self.bishopWR = Bishop(color='W', side='R')
        self.pawnB_8 = Pawn(color = 'B', piece_value= '8')
        self.pawnB_9 = Pawn(color='B', piece_value='9')
        self.pawnB_A = Pawn(color='B', piece_value='A')
        self.pawnB_B = Pawn(color='B', piece_value='B')
        self.pawnB_C = Pawn(color='B', piece_value='C')
        self.pawnB_D = Pawn(color='B', piece_value='D')
        self.pawnB_E = Pawn(color='B', piece_value='E')
        self.pawnB_F = Pawn(color='B', piece_value='F')
        self.pawnW_8 = Pawn(color='W', piece_value='8')
        self.pawnW_9 = Pawn(color='W', piece_value='9')
        self.pawnW_A = Pawn(color='W', piece_value='A')
        self.pawnW_B = Pawn(color='W', piece_value='B')
        self.pawnW_C = Pawn(color='W', piece_value='C')
        self.pawnW_D = Pawn(color='W', piece_value='D')
        self.pawnW_E = Pawn(color='W', piece_value='E')
        self.pawnW_F = Pawn(color='W', piece_value='F')

    # in the below function we are only checking the proper direction and pace length of perticular piece
    # the other overheads are resolved by the function make_move of perticular class

   # def make_move(self, color, piece_value, position):

       # if color is 'B':
          #  if piece_value is '0':
             #  if position[}
ha = Hash()
cb = ChessBoard()
#cb.store_move('W','B','E','4')

k = King(color = "W")
k.store_move('W','B','E','4')
k.make_move(1)
k.print_matrix('B')
q = Queen(color = 'B')
q.store_move('B', 'C', 'E', '5')
q.make_move(2, 4)
k.print_matrix('B')
br = Bishop(color = 'B', side = 'R')
br.make_move(8, 3)
br.print_matrix('B')
kl = Knight(color = 'B', side = 'L')
kl.make_move(1)
kl.print_matrix('B')
r1 = Rook(color = 'B', side = 'R')
r1.store_move('B', '8', 'A', '3')
r1.make_move(1,4)
r1.print_matrix('B')
p1 = Pawn(color = 'W', piece_value = 'E')
p1.make_move(3)
p1.print_matrix('B')
