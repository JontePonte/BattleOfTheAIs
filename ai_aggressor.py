

def aggressor(game_info):
    """ AI that allways tries to attack """

    # Unpack game info
    _player1_score = game_info['player1']['score']
    player1_health = game_info['player1']['health']
    _player1_moves = game_info['player1']['moves']

    _player2_score = game_info['player2']['score']
    _player2_health = game_info['player2']['health']
    _player2_moves = game_info['player2']['moves']

    action = "attack"
    if player1_health <= 3:
        action = "defend"

    return action
