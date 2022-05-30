import os
from colorama import Style, Fore


# CONSTANTS


VALID_COORDINATES = ('11', '12', '13', '21', '22', '23', '31', '32', '33')
VICTORY_COMBINATIONS = [
    ('11', '12', '13'),
    ('21', '22', '23'),
    ('31', '32', '33'),
    ('11', '21', '31'),
    ('12', '22', '32'),
    ('13', '23', '33'),
    ('11', '22', '33'),
    ('13', '22', '31'),
]


# CLASSES


class Player:
    def __init__(self, name, symbol):

        self.name = name
        self.symbol = symbol
        self.current_won_boards = []

        self.plays_description = {}

        for i in range(9):
            self.plays_description[f'board_{i+1}'] = []

    def get_symbol(self):
        return self.symbol

    def get_name(self):
        return self.name

    def assing_won_board(self, board_coordinate):
        self.current_won_boards.append(board_coordinate)

    def assing_play_to_board(self, board_number, play_coordinate):
        self.plays_description[f'board_{board_number}'].append(play_coordinate)


class OuterBoard:
    def __init__(self):

        my_outer_board = []

        for coordinate in VALID_COORDINATES:
            inner_board = InnerBoard(coordinate)
            my_outer_board.append(inner_board)

        self.board = my_outer_board
        self.current_o_coordinates = []
        self.current_x_coordinates = []

    def get_order_of_symbols(self):
        symbols = ''
        for inner_board in self.board:
            for coordinate in VALID_COORDINATES:
                symbols += inner_board.return_symbol(coordinate)
        return symbols

    def get_inner_board(self, number):
        return self.board[number]


class InnerBoard:
    def __init__(self, board_coordinate):
        self.board = create_board(' ')
        self.board_coordinate = board_coordinate
        self.current_o_coordinates = []
        self.current_x_coordinates = []

    def add_o_coordinate(self, coordinate):
        self.current_o_coordinates.append(coordinate)
        self.board[int(coordinate[0])-1][int(coordinate[1])-1] = 'O'

    def add_x_coordinate(self, coordinate):
        self.current_x_coordinates.append(coordinate)
        self.board[int(coordinate[0])-1][int(coordinate[1])-1] = 'X'

    # def fill_board(self):
    #     for coordinate in self.current_o_coordinates:
    #         self.board[int(coordinate[0])-1][int(coordinate[1])-1] = 'O'
    #     for coordinate in self.current_x_coordinates:
    #         self.board[int(coordinate[0])-1][int(coordinate[1])-1] = 'X'

    def return_symbol(self, coordinate):
        return self.board[int(coordinate[0])-1][int(coordinate[1])-1]

    def clear_board(self):
        self.current_o_coordinates = []
        self.current_x_coordinates = []


# DISPLAY METHODS


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def stand_by():
    _ = input()


def l(n):
    for _ in range(n):
        print('')


def display_guide_board():
    print("""    Follow this guide

         7||8||9
         4||5||6
         1||2||3""")


def display_current_board(current_outer_board, list_of_players, i_b=None):

    y = Fore.YELLOW
    x = Fore.RED
    o = Fore.BLUE
    b = Style.BRIGHT

    r = Fore.RESET
    rr = Style.RESET_ALL

    def bc(inner_board_position):
        """
            returns the color of a board
            x -> board won by Player 1
            o -> board won by Player 2
            y -> current board to play in
            r -> board not being play, nor won by any player
        """
        if number_to_coordinates(inner_board_position) in list_of_players[0].current_won_boards:
            return x
        elif number_to_coordinates(inner_board_position) in list_of_players[1].current_won_boards:
            return o
        elif i_b == inner_board_position:
            return y
        return r

    s = current_outer_board.get_order_of_symbols()

    print(f"""{b}       ||       ||
 {x if s[0] == 'X' else o}{s[0]}{bc(1)}|{r}{x if s[1] == 'X' else o}{s[1]}{bc(1)}|{r}{x if s[2] == 'X' else o}{s[2]} {r}|| {x if s[9] == 'X' else o}{s[9]}{bc(2)}|{r}{x if s[10] == 'X' else o}{s[10]}{bc(2)}|{r}{x if s[11] == 'X' else o}{s[11]} {r}|| {x if s[18] == 'X' else o}{s[18]}{bc(3)}|{r}{x if s[19] == 'X' else o}{s[19]}{bc(3)}|{r}{x if s[20] == 'X' else o}{s[20]}
 {x if s[3] == 'X' else o}{s[3]}{bc(1)}|{r}{x if s[4] == 'X' else o}{s[4]}{bc(1)}|{r}{x if s[5] == 'X' else o}{s[5]} {r}|| {x if s[12] == 'X' else o}{s[12]}{bc(2)}|{r}{x if s[13] == 'X' else o}{s[13]}{bc(2)}|{r}{x if s[14] == 'X' else o}{s[14]} {r}|| {x if s[21] == 'X' else o}{s[21]}{bc(3)}|{r}{x if s[22] == 'X' else o}{s[22]}{bc(3)}|{r}{x if s[23] == 'X' else o}{s[23]}
 {x if s[6] == 'X' else o}{s[6]}{bc(1)}|{r}{x if s[7] == 'X' else o}{s[7]}{bc(1)}|{r}{x if s[8] == 'X' else o}{s[8]} {r}|| {x if s[15] == 'X' else o}{s[15]}{bc(2)}|{r}{x if s[16] == 'X' else o}{s[16]}{bc(2)}|{r}{x if s[17] == 'X' else o}{s[17]} {r}|| {x if s[24] == 'X' else o}{s[24]}{bc(3)}|{r}{x if s[25] == 'X' else o}{s[25]}{bc(3)}|{r}{x if s[26] == 'X' else o}{s[26]}
{r}_______||_______||_______
       {r}||       ||
 {x if s[27] == 'X' else o}{s[27]}{bc(4)}|{r}{x if s[28] == 'X' else o}{s[28]}{bc(4)}|{r}{x if s[29] == 'X' else o}{s[29]} {r}|| {x if s[36] == 'X' else o}{s[36]}{bc(5)}|{r}{x if s[37] == 'X' else o}{s[37]}{bc(5)}|{r}{x if s[38] == 'X' else o}{s[38]} {r}|| {x if s[45] == 'X' else o}{s[45]}{bc(6)}|{r}{x if s[46] == 'X' else o}{s[46]}{bc(6)}|{r}{x if s[47] == 'X' else o}{s[47]}
 {x if s[30] == 'X' else o}{s[30]}{bc(4)}|{r}{x if s[31] == 'X' else o}{s[31]}{bc(4)}|{r}{x if s[32] == 'X' else o}{s[32]} {r}|| {x if s[39] == 'X' else o}{s[39]}{bc(5)}|{r}{x if s[40] == 'X' else o}{s[40]}{bc(5)}|{r}{x if s[41] == 'X' else o}{s[41]} {r}|| {x if s[48] == 'X' else o}{s[48]}{bc(6)}|{r}{x if s[49] == 'X' else o}{s[49]}{bc(6)}|{r}{x if s[50] == 'X' else o}{s[50]}
 {x if s[33] == 'X' else o}{s[33]}{bc(4)}|{r}{x if s[34] == 'X' else o}{s[34]}{bc(4)}|{r}{x if s[35] == 'X' else o}{s[35]} {r}|| {x if s[42] == 'X' else o}{s[42]}{bc(5)}|{r}{x if s[43] == 'X' else o}{s[43]}{bc(5)}|{r}{x if s[44] == 'X' else o}{s[44]} {r}|| {x if s[51] == 'X' else o}{s[51]}{bc(6)}|{r}{x if s[52] == 'X' else o}{s[52]}{bc(6)}|{r}{x if s[53] == 'X' else o}{s[53]}
{r}_______||_______||_______
       {r}||       ||
 {x if s[54] == 'X' else o}{s[54]}{bc(7)}|{r}{x if s[55] == 'X' else o}{s[55]}{bc(7)}|{r}{x if s[56] == 'X' else o}{s[56]} {r}|| {x if s[63] == 'X' else o}{s[63]}{bc(8)}|{r}{x if s[64] == 'X' else o}{s[64]}{bc(8)}|{r}{x if s[65] == 'X' else o}{s[65]} {r}|| {x if s[72] == 'X' else o}{s[72]}{bc(9)}|{r}{x if s[73] == 'X' else o}{s[73]}{bc(9)}|{r}{x if s[74] == 'X' else o}{s[74]}
 {x if s[57] == 'X' else o}{s[57]}{bc(7)}|{r}{x if s[58] == 'X' else o}{s[58]}{bc(7)}|{r}{x if s[59] == 'X' else o}{s[59]} {r}|| {x if s[66] == 'X' else o}{s[66]}{bc(8)}|{r}{x if s[67] == 'X' else o}{s[67]}{bc(8)}|{r}{x if s[68] == 'X' else o}{s[68]} {r}|| {x if s[75] == 'X' else o}{s[75]}{bc(9)}|{r}{x if s[76] == 'X' else o}{s[76]}{bc(9)}|{r}{x if s[77] == 'X' else o}{s[77]}
 {x if s[60] == 'X' else o}{s[60]}{bc(7)}|{r}{x if s[61] == 'X' else o}{s[61]}{bc(7)}|{r}{x if s[62] == 'X' else o}{s[62]} {r}|| {x if s[69] == 'X' else o}{s[69]}{bc(8)}|{r}{x if s[70] == 'X' else o}{s[70]}{bc(8)}|{r}{x if s[71] == 'X' else o}{s[71]} {r}|| {x if s[78] == 'X' else o}{s[78]}{bc(9)}|{r}{x if s[79] == 'X' else o}{s[79]}{bc(9)}|{r}{x if s[80] == 'X' else o}{s[80]}
       {r}||       ||{rr}""")


def create_board(content):
    return [[content, content, content],
            [content, content, content],
            [content, content, content]]


# GAME METHODS


def player_turn(outer_board, list_of_players, player_index, inner_board):

    clear()

    if (
        number_to_coordinates(inner_board) in list_of_players[0].current_won_boards or
        number_to_coordinates(inner_board) in list_of_players[1].current_won_boards
    ):
        inner_board = None

    current_player = list_of_players[player_index % 2]

    print(f"{Fore.RED if player_index % 2 == 0 else Fore.BLUE}It's {current_player.get_name()}'s turn ({current_player.get_symbol()}){Fore.RESET}")
    l(1)
    display_guide_board()
    l(1)
    display_current_board(outer_board, list_of_players, inner_board)
    l(1)

    if inner_board is None:
        while True:
            l(1)
            inner_board = refactor_number(int(input('Select an inner board (1-9): ')))
            if board_is_won(inner_board, list_of_players):
                print('WARNING: This board is not available, please choose another')
            else:
                break
    else:
        print(f'You will play on {Fore.YELLOW}board {inner_board}{Fore.RESET}')

    while True:
        l(1)
        coordinate = refactor_number(int(input('Select a tile number for your play (1-9): ')))
        if coordinate_is_free(coordinate, outer_board.get_inner_board(inner_board-1)):
            break
        else:
            print('WARNING: This tile is not available, please choose another')

    coordinate = number_to_coordinates(coordinate)

    if current_player.get_symbol() == 'X':
        outer_board.get_inner_board(inner_board-1).add_x_coordinate(coordinate)
    if current_player.get_symbol() == 'O':
        outer_board.get_inner_board(inner_board-1).add_o_coordinate(coordinate)
    current_player.assing_play_to_board(inner_board, coordinate)

    if look_for_possible_victory(current_player.plays_description[f'board_{inner_board}']) is not None:
        l(1)
        print(f'Inner board {inner_board} won by {current_player.get_name()}')
        current_player.assing_won_board(number_to_coordinates(inner_board))
        stand_by()
        if look_for_possible_victory(current_player.current_won_boards) is not None:
            clear()
            l(1)
            print(f'Game won by {current_player.get_name()}')
            l(1)
            display_current_board(outer_board, list_of_players, None)
            l(1)
            print('Thank you for playing')
            stand_by()
        else:
            player_turn(
                outer_board,
                list_of_players,
                player_index+1,
                coordinate_to_number(coordinate)
            )
    else:
        player_turn(
            outer_board,
            list_of_players,
            player_index+1,
            coordinate_to_number(coordinate)
        )


def coordinate_is_free(coordinate, board):

    coordinate = number_to_coordinates(coordinate)

    if (
        coordinate in board.current_o_coordinates or
        coordinate in board.current_x_coordinates
    ):
        return False

    return True


def board_is_won(coordinate, list_of_players):

    coordinate = number_to_coordinates(coordinate)

    if (
        coordinate in list_of_players[0].current_won_boards or
        coordinate in list_of_players[1].current_won_boards
    ):
        return True

    return False


def coordinate_to_number(coordinate):
    for i in VALID_COORDINATES:
        if i == coordinate:
            return VALID_COORDINATES.index(i) + 1


def number_to_coordinates(number):
    if number is None:
        return None
    return VALID_COORDINATES[number-1]


def refactor_number(n):
    if n == 1 or n == 2 or n == 3:
        return n + 6
    if n == 7 or n == 8 or n == 9:
        return n - 6
    return n


def look_for_possible_victory(list_of_plays):
    """
        returns winning combination if found
        returns None if no victory is found
    """
    for combination in VICTORY_COMBINATIONS:
        for victory_position in combination:
            if victory_position in list_of_plays:
                if combination.index(victory_position) == 2:
                    return combination
            else:
                break
    return None
