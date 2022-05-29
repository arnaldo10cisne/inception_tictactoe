from utils import Player
from utils import player_turn


def run():
    print('Welcome to INCEPTION TIC TAC TOE')
    # my_outer_board = OuterBoard()
    # for i in range(81):
    #     display_current_board(my_outer_board)
    #     InBo = input('Select an inner board (1-9): ')
    #     coordinate = input('Select a coordinate: ')
    #     if (i % 2 == 0):
    #         my_outer_board.get_inner_board(int(InBo)-1).add_x_coordinate(coordinate)
    #     else:
    #         my_outer_board.get_inner_board(int(InBo)-1).add_o_coordinate(coordinate)

    p1_name = input('Name for player 1: ')
    p1 = Player(p1_name, 'X')
    p2_name = input('Name for player 1: ')
    p2 = Player(p2_name, 'O')
    player_list = [p1, p2]

    player_turn(player_list, 0)


if __name__ == "__main__":
    run()
