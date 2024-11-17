import random

def full_random(game_info):
    """ Random choise between attack and defend """

    # Unpack game info
    _player1_score = game_info['player1']['score']
    _player1_health = game_info['player1']['health']
    _player1_moves = game_info['player1']['moves']

    _player2_score = game_info['player2']['score']
    _player2_health = game_info['player2']['health']
    _player2_moves = game_info['player2']['moves']

    action = random.choice(["attack", "defend"])

    return action
