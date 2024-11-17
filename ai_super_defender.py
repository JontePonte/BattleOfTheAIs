import inspect


def super_defender(game_info):
    """ AI that allways defend """

    # Unpack game info
    my_score, my_health, my_moves = None, None, None
    opponent_score, opponent_health, opponent_moves = None, None, None
    
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_score = game_info[ai_name]['score']
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_score = game_info[ai_name]['score']
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    action = "defend"

    return action
