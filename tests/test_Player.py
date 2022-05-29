from utils import Player


class TestPlayer():

    def test_get_attributes():
        """
            Tests that the Player object returns initial attributes correctly
        """
        my_player = Player('Arnaldo', 'X')
        assert my_player.get_name() == 'Arnaldo'
        assert my_player.get_symbol() == 'X'

    def test_plays_description_initial_state():
        """
            Tests that plays_desription gets created correctly
        """
        my_player = Player('Jhon', 'X')
        assert len(my_player.plays_description) == 9
        for n in range(9):
            assert my_player.plays_description[f'board_{n+1}'] == []
