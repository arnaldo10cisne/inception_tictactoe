from utils import look_for_possible_victory, VICTORY_COMBINATIONS


def test_look_for_possible_victory():

    list_of_plays = []
    assert look_for_possible_victory(list_of_plays) is None

    for victory_combination in VICTORY_COMBINATIONS:
        assert look_for_possible_victory(victory_combination) == victory_combination

    list_of_plays = [11, 13, 31, 33]
    assert look_for_possible_victory(list_of_plays) is None
