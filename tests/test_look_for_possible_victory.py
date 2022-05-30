from utils import look_for_possible_victory, VICTORY_COMBINATIONS


def test_look_for_possible_victory():

    # Test for an empty array
    list_of_plays = []
    assert look_for_possible_victory(list_of_plays) is None

    # Test for every possible combination
    for victory_combination in VICTORY_COMBINATIONS:
        assert look_for_possible_victory(victory_combination) == victory_combination

    # Test for some arrays without victory combinations
    list_of_plays = [11, 13, 31, 33]
    assert look_for_possible_victory(list_of_plays) is None
    list_of_plays = [31, 22, 33, 12]
    assert look_for_possible_victory(list_of_plays) is None
    list_of_plays = [11, 13, 21, 23, 32]
    assert look_for_possible_victory(list_of_plays) is None

    # Test for vitory hidden in list of plays
    list_of_plays = [11, 13, 21, 23, 32, 33]
    assert look_for_possible_victory(list_of_plays) in VICTORY_COMBINATIONS
    list_of_plays = [11, 13, 22, 23, 31, 32]
    assert look_for_possible_victory(list_of_plays) in VICTORY_COMBINATIONS
    list_of_plays = [12, 13, 21, 23, 32]
    assert look_for_possible_victory(list_of_plays) in VICTORY_COMBINATIONS
    list_of_plays = [32, 33, 11, 13, 31]
    assert look_for_possible_victory(list_of_plays) in VICTORY_COMBINATIONS
