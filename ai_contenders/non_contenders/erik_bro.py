import inspect

def erik_bro(game_info):
    my_health, my_moves = None, None
    opponent_health, opponent_moves = None, None

    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    last_opponent_move = opponent_moves[-1] if opponent_moves else None

    # Beslutslogik
    if my_health <= 2:
        action = "rebuild"
    elif opponent_health <= 2:
        action = "attack"
    elif last_opponent_move == "attack":
        action = "defend"
    elif my_health < 5:
        action = "rebuild"
    elif last_opponent_move == "rebuild":
        action = "attack"
    else:
        action = "defend"
    return action
