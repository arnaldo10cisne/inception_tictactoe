from utils import Player, OuterBoard
from utils import player_turn, clear, l


def run():
    clear()
    l(1)
    print('Welcome to INCEPTION TIC TAC TOE')
    l(1)
    outer_board = OuterBoard()
    p1_name = input('Name for player 1 (X): ')
    p1 = Player(p1_name, 'X')
    l(1)
    p2_name = input('Name for player 2 (O): ')
    p2 = Player(p2_name, 'O')
    player_list = [p1, p2]

    player_turn(outer_board, player_list, 0, None)


if __name__ == "__main__":
    run()
