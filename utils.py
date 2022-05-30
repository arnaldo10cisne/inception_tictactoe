import os


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

         1||2||3
         4||5||6
         7||8||9""")


def display_current_board(current_outer_board):

    symbols = current_outer_board.get_order_of_symbols()

    print(f"""       ||       ||
 {symbols[0]}|{symbols[1]}|{symbols[2]} || {symbols[9]}|{symbols[10]}|{symbols[11]} || {symbols[18]}|{symbols[19]}|{symbols[20]}
 {symbols[3]}|{symbols[4]}|{symbols[5]} || {symbols[12]}|{symbols[13]}|{symbols[14]} || {symbols[21]}|{symbols[22]}|{symbols[23]}
 {symbols[6]}|{symbols[7]}|{symbols[8]} || {symbols[15]}|{symbols[16]}|{symbols[17]} || {symbols[24]}|{symbols[25]}|{symbols[26]}
_______||_______||_______
       ||       ||
 {symbols[27]}|{symbols[28]}|{symbols[29]} || {symbols[36]}|{symbols[37]}|{symbols[38]} || {symbols[45]}|{symbols[46]}|{symbols[47]}
 {symbols[30]}|{symbols[31]}|{symbols[32]} || {symbols[39]}|{symbols[40]}|{symbols[41]} || {symbols[48]}|{symbols[49]}|{symbols[50]}
 {symbols[33]}|{symbols[34]}|{symbols[35]} || {symbols[42]}|{symbols[43]}|{symbols[44]} || {symbols[51]}|{symbols[52]}|{symbols[53]}
_______||_______||_______
       ||       ||
 {symbols[54]}|{symbols[55]}|{symbols[56]} || {symbols[63]}|{symbols[64]}|{symbols[65]} || {symbols[72]}|{symbols[73]}|{symbols[74]}
 {symbols[57]}|{symbols[58]}|{symbols[59]} || {symbols[66]}|{symbols[67]}|{symbols[68]} || {symbols[75]}|{symbols[76]}|{symbols[77]}
 {symbols[60]}|{symbols[61]}|{symbols[62]} || {symbols[69]}|{symbols[70]}|{symbols[71]} || {symbols[78]}|{symbols[79]}|{symbols[80]}
       ||       ||""")


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
    display_current_board(outer_board)
    l(1)

    if inner_board is None:
        while True:
            l(1)
            inner_board = int(input('Select an inner board (1-9): '))
            if board_is_won(inner_board, list_of_players):
                print('WARNING: This board is not available, please choose another')
            else:
                break
    else:
        print(f'You will play on board {inner_board}')

    while True:
        l(1)
        coordinate = int(input('Select a tile number for your play: '))
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
