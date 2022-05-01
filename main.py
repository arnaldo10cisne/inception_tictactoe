import os


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


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


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


def display_current_board(current_outer_board):

    clear()

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


def run():
    print('Welcome to INCEPTION TIC TAC TOE')
    my_outer_board = OuterBoard()
    for i in range(81):
        display_current_board(my_outer_board)
        InBo = input('Select an inner board (1-9): ')
        coordinate = input('Select a coordinate: ')
        if (i % 2 == 0):
            my_outer_board.get_inner_board(int(InBo)-1).add_x_coordinate(coordinate)
        else:
            my_outer_board.get_inner_board(int(InBo)-1).add_o_coordinate(coordinate)


if __name__ == "__main__":
    run()
