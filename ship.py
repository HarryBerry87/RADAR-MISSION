import game_board, sprites


class Ship:

    def __init__(self, length: int, row: int,
                 col: int, is_vertical: bool):
        """ Ships are specified by their length, the (row,col)
        coordinate of the bow, and whether they are vertical or
        horizontal. Two examples are illustrated on the board below:

        X = Ship(5,2,4,False)
        Y = Ship(3,5,1,True)

          0|1|2|3|4|5|6|7|8|9|
        A|_|_|_|_|_|_|_|_|_|_|
        B|_|_|_|_|_|_|_|_|_|_|
        C|_|_|_|_|X|X|X|X|X|_|
        D|_|Y|_|_|_|_|_|_|_|_|
        E|_|Y|_|_|_|_|_|_|_|_|
        F|_|Y|_|_|_|_|_|_|_|_|
        G|_|_|_|_|_|_|_|_|_|_|
        H|_|_|_|_|_|_|_|_|_|_|
        I|_|_|_|_|_|_|_|_|_|_|
        J|_|_|_|_|_|_|_|_|_|_|

        """
        self.length = length
        self.row = row
        self.col = col
        self.is_vertical = is_vertical
        # true if _hits == length
        self.sunk = False
        # total hits taken
        self._hits = 0

    def draw(self, board: game_board.GameBoard):
        """
        Draw the ship to the board.
        Use the GameBoard.add_sprite method
        Make sure the bow and stern are the
        correct orientation!

        For example to add a vertical ship's bow to
        location B4:

        board.add_sprite(sprites.ship_top,(1,4))

        """

        # --------- BEGIN YOUR CODE ----------
        if self.is_vertical is True:
            board.add_sprite(sprites.ship_top, (self.row, self.col))
            for i in range(1, self.length - 1):
                board.add_sprite(sprites.ship_vertical, (self.row + i, self.col))

            board.add_sprite(sprites.ship_bottom, (self.row + self.length - 1, self.col))

        if self.is_vertical is False:
            board.add_sprite(sprites.ship_left, (self.row, self.col))
            for i in range(1, self.length - 1):
                board.add_sprite(sprites.ship_horizontal, (self.row, self.col + i))

            board.add_sprite(sprites.ship_right, (self.row, self.col + self.length - 1))
        # --------- END YOUR CODE ----------
