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
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


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


def display_current_board(current_outer_board, i_b = None):

    y = Fore.YELLOW
    b = Style.BRIGHT
    r = Style.RESET_ALL
    x = Fore.RED
    o = Fore.BLUE

    s = current_outer_board.get_order_of_symbols()

    print(f"""{b}       ||       ||
 {s[0]}{y if i_b == 1 else r}|{r}{s[1]}{y if i_b == 1 else r}|{r}{s[2]} || {s[9]}{y if i_b == 2 else r}|{r}{s[10]}{y if i_b == 2 else r}|{r}{s[11]} || {s[18]}{y if i_b == 3 else r}|{r}{s[19]}{y if i_b == 3 else r}|{r}{s[20]}
 {s[3]}{y if i_b == 1 else r}|{r}{s[4]}{y if i_b == 1 else r}|{r}{s[5]} || {s[12]}{y if i_b == 2 else r}|{r}{s[13]}{y if i_b == 2 else r}|{r}{s[14]} || {s[21]}{y if i_b == 3 else r}|{r}{s[22]}{y if i_b == 3 else r}|{r}{s[23]}
 {s[6]}{y if i_b == 1 else r}|{r}{s[7]}{y if i_b == 1 else r}|{r}{s[8]} || {s[15]}{y if i_b == 2 else r}|{r}{s[16]}{y if i_b == 2 else r}|{r}{s[17]} || {s[24]}{y if i_b == 3 else r}|{r}{s[25]}{y if i_b == 3 else r}|{r}{s[26]}
_______||_______||_______
       ||       ||
 {s[27]}{y if i_b == 4 else r}|{r}{s[28]}{y if i_b == 4 else r}|{r}{s[29]} || {s[36]}{y if i_b == 5 else r}|{r}{s[37]}{y if i_b == 5 else r}|{r}{s[38]} || {s[45]}{y if i_b == 6 else r}|{r}{s[46]}{y if i_b == 6 else r}|{r}{s[47]}
 {s[30]}{y if i_b == 4 else r}|{r}{s[31]}{y if i_b == 4 else r}|{r}{s[32]} || {s[39]}{y if i_b == 5 else r}|{r}{s[40]}{y if i_b == 5 else r}|{r}{s[41]} || {s[48]}{y if i_b == 6 else r}|{r}{s[49]}{y if i_b == 6 else r}|{r}{s[50]}
 {s[33]}{y if i_b == 4 else r}|{r}{s[34]}{y if i_b == 4 else r}|{r}{s[35]} || {s[42]}{y if i_b == 5 else r}|{r}{s[43]}{y if i_b == 5 else r}|{r}{s[44]} || {s[51]}{y if i_b == 6 else r}|{r}{s[52]}{y if i_b == 6 else r}|{r}{s[53]}
_______||_______||_______
       ||       ||
 {s[54]}{y if i_b == 7 else r}|{r}{s[55]}{y if i_b == 7 else r}|{r}{s[56]} || {s[63]}{y if i_b == 8 else r}|{r}{s[64]}{y if i_b == 8 else r}|{r}{s[65]} || {s[72]}{y if i_b == 9 else r}|{r}{s[73]}{y if i_b == 9 else r}|{r}{s[74]}
 {s[57]}{y if i_b == 7 else r}|{r}{s[58]}{y if i_b == 7 else r}|{r}{s[59]} || {s[66]}{y if i_b == 8 else r}|{r}{s[67]}{y if i_b == 8 else r}|{r}{s[68]} || {s[75]}{y if i_b == 9 else r}|{r}{s[76]}{y if i_b == 9 else r}|{r}{s[77]}
 {s[60]}{y if i_b == 7 else r}|{r}{s[61]}{y if i_b == 7 else r}|{r}{s[62]} || {s[69]}{y if i_b == 8 else r}|{r}{s[70]}{y if i_b == 8 else r}|{r}{s[71]} || {s[78]}{y if i_b == 9 else r}|{r}{s[79]}{y if i_b == 9 else r}|{r}{s[80]}
       ||       ||{r}""")


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

    print(f"It's {current_player.get_name()}'s turn ({current_player.get_symbol()})")
    l(1)
    display_guide_board()
    l(1)
    display_current_board(outer_board, inner_board)
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
        print(f'You will play on board {inner_board}')

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
            display_current_board(outer_board)
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
