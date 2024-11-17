import inspect


def super_aggressor(game_info):
    """ AI that allways tries to attack """

    # Unpack game info
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_score = game_info[ai_name]['score']
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_score = game_info[ai_name]['score']
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    action = "attack"
    if my_health == 1:
        action = "defend"

    return action
