import inspect
import random

def Erik_Borg(game_info):
    # Unpack game info
    my_health, opponent_health = None, None

    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
        else:
            opponent_health = game_info[ai_name]['health']


    if my_health > opponent_health:
        action = random.choice(["attack", "defend"])
    elif my_health < opponent_health:
        action = "attack"
    else:
        action = random.choice(["rebuild", "defend"])
    return action
