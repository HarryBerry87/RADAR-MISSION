import ship, game_board, sprites
from random import randint, choice
import time
from typing import List, Tuple, Optional


class Computer:
    """ A computer player"""

    def __init__(self):

        # list of ship objects
        self._my_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._my_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._my_hits: List[Tuple[int, int]] = []
        # list of ship objects
        self._sunk_ships: List[ship.Ship] = []
        # list of (row,col) coordinates
        self._their_misses: List[Tuple[int, int]] = []
        # list of (row,col) coordinates
        self._their_hits: List[Tuple[int, int]] = []

        # the board matrix is a 10x10 structure with
        # pointers to ship objects. Initialize to all
        # None values- no ships are on the board
        self._board_matrix: List[List[Optional[ship.Ship]]] = [[None] * 10 for _ in range(10)]

        # set to True if all opponent's ships are sunk
        self.complete: bool = False

    def initialize(self):
        """ Create a valid ship layout
        This function populates
        _my_ships and _board_matrix

        Ship Type  | Length
        -----------|-------
        Carrier    |   5
        Battleship |   4
        Cruiser    |   3
        Submarine  |   3
        Destroyer  |   2

        * the ship type is just FYI, it is not used in the game *
        """

        for ship_length in [5, 4, 3, 3, 2]:
            # --------- BEGIN YOUR CODE ----------
            valid_place = False
            while not valid_place:
                # 1.) create ship of the given length at a random (row,col)
                #     position either horizontal or vertical
                valid_index = False
                while not valid_index:
                    x_orig = randint(0, 9)
                    y_orig = randint(0, 9)
                    vert = choice([True, False])
                    if vert is True:
                        max_index = y_orig + ship_length
                    else:
                        max_index = x_orig + ship_length

                    if max_index < 9:
                        valid_index = True

                my_ship = ship.Ship(ship_length, y_orig, x_orig, vert)
                # 2.) check if this conflicts with any of the other ships by
                #     by making sure that every entry in _board_matrix is None
                valid = []
                for i in range(my_ship.length):
                    if my_ship.is_vertical is True:
                        if self._board_matrix[my_ship.row + i][my_ship.col] is None:
                            valid.append('Yes')
                        else:
                            valid.append('No')

                    else:
                        if self._board_matrix[my_ship.row][my_ship.col + i] is None:
                            valid.append('Yes')
                        else:
                            valid.append('No')
            # 2b.) If the ship is not valid, retry step 1
            # 3.) If the ship is valid set the appropriate elements _board_matrix array
            #     equal to the ship
            # Example: to place a vertical destroyer at C2:
            #    board_matrix[2][2] = my_ship
            #    board_matrix[3][2] = my_ship
                if 'No' not in valid:
                    for i in range(my_ship.length):
                        if my_ship.is_vertical is True:
                            self._board_matrix[my_ship.row + i][my_ship.col] = my_ship
                        if my_ship.is_vertical is False:
                            self._board_matrix[my_ship.row][my_ship.col + i] = my_ship

                    valid_place = True
                    self._my_ships.append(my_ship)

    def guess(self, row, col) -> Tuple[int, Optional[ship.Ship]]:
        """
        Tell the other player whether a row and column guess is a hit or miss.
        Record the (row,col) guess in either self._their_hits or self._their_misses

        If a space is guessed twice do not hit the ship twice. That's cheating :)

        Returns a tuple of (status, ship) where
            status = 0: miss
                   = 1: hit
                   = 2: sunk

            ship   = None if a hit or miss
                   = ship object if sunk

        """
        my_ship: ship.Ship = self._board_matrix[row][col]

        # if my_ship is None the guess is a miss, otherwise its a hit

        # --------- BEGIN YOUR CODE ----------

        # Hit logic:
        if my_ship is not None:
            # make sure this is a *new* hit (no double guesses)
            if [row, col] in self._their_hits:
                print('double hit')
                return 1, my_ship
            # add to _their_hits
            self._their_hits.append([row, col])
            # hit the ship
            my_ship.hit()
            # check if ship is sunk
            if my_ship.sunk is True:
                # return either (1,None) or (2,my_ship)
                return 2, my_ship
            else:
                return 1, my_ship

        # Miss logic:
        if my_ship is None:
            # add to _their_misses
            self._their_misses.append([row, col])
            # return (0, None)
            return 0, None

        # --------- END YOUR CODE ----------


    def take_turn(self, opponent, name):
        """
        Guess a new row,col space. This may be random or use a more sophisticated AI.
        Updates self._my_hits, self._my_misses, and self._sunk_ships
        """

        # --------- BEGIN YOUR CODE ----------

        # 1.) Guess a random space that has not been guessed (or be more clever!)
        valid_guess = False
        dummy = 0
        compass = ['north', 'south', 'east', 'west']
        x = [0, 3, 5, 7, 9, 10, 10, 10, 10, 10, 10]
        while valid_guess is False:
            if dummy in range(x[0], x[1]) and self._my_hits:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-1]
            elif dummy in range(x[1], x[2]) and len(self._my_hits) > 1:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-2]
            elif dummy in range(x[2], x[3]) and len(self._my_hits) > 2:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-3]
            elif dummy in range(x[3], x[4]) and len(self._my_hits) > 3:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-4]
            elif dummy in range(x[4], x[5]) and len(self._my_hits) > 4:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-5]
            elif dummy in range(x[5], x[6]) and len(self._my_hits) > 5:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-6]
            elif dummy in range(x[6], x[7]) and len(self._my_hits) > 6:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-7]
            elif dummy in range(x[7], x[8]) and len(self._my_hits) > 7:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-8]
            elif dummy in range(x[8], x[9]) and len(self._my_hits) > 8:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-9]
            elif dummy in range(x[9], x[10]) and len(self._my_hits) > 9:
                dir = compass[randint(0, 3)]
                old_hit = self._my_hits[-10]
            else:
                dir = 'blind'
                row = randint(0, 9)
                col = randint(0, 9)

            if dir is 'north':
                row = old_hit[0] - 1
                col = old_hit[1]
            if dir is 'east':
                row = old_hit[0]
                col = old_hit[1] + 1
            if dir is 'south':
                row = old_hit[0] + 1
                col = old_hit[1]
            if dir is 'west':
                row = old_hit[0]
                col = old_hit[1] - 1
            if [row, col] not in self._my_misses and [row, col] not in self._my_hits:
                if row in range(10) and col in range(10):
                    valid_guess = True
                    if name is 'USN':
                        print(name + "'s shot was " + dir + str(dummy))
            else:
                dummy += 1



        # Steps 2-4 are the same as Human.take_turn
        # 2.) Call opponent.guess() to check whether the guess is a hit or miss
        result = opponent.guess(row, col)

        # 3.) Update my_hits, my_misses, and sunk_ships accordingly
        if result[0] is 0:
            self._my_misses.append([row, col])

        elif result[0] is 1:
            self._my_hits.append([row, col])

        if result[0] is 2:
            self._my_hits.append([row, col])
            self._sunk_ships.append(result[1])

        # 4.) If the sunk_ships array has 5 ships in it set self.complete to True
        if len(self._sunk_ships) is 5:
            self.complete = True

        # --------- END YOUR CODE ----------

        # enforce a short delay to make the computer appear to "think" about its guess
        time.sleep(0.05)

    def print_board(self):
        """
        Print the player's board as text, useful for debugging
        """

        print("=" * 10)
        for row in self._board_matrix:
            for entry in row:
                if entry is None:
                    print("_", end="")
                else:
                    print(entry.length, end="")
            print("")
        print("=" * 10)

    def draw(self,
             my_board: game_board.GameBoard,
             their_board: game_board.GameBoard):

        """ Add sprites to the game board's to indicate
        ship positions, guesses, hits, etc """

        for my_ship in self._my_ships:
            my_ship.draw(my_board)
        for miss in self._their_misses:
            my_board.add_sprite(sprites.miss, miss)
        for hit in self._their_hits:
            my_board.add_sprite(sprites.hit, hit)

        # draw hit indicators on their board
        for miss in self._my_misses:
            their_board.add_sprite(sprites.miss, miss)
        for their_ship in self._sunk_ships:
            their_ship.draw(their_board)
        for hit in self._my_hits:
            their_board.add_sprite(sprites.hit, hit)

