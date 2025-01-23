import random
import inspect

def Herman(game_info):
    my_health = None
    opponent_health = None
    my_moves = []
    opponent_moves = []
    
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]["health"]
            my_moves = game_info[ai_name]["moves"]
        else:
            opponent_health = game_info[ai_name]["health"]
            opponent_moves = game_info[ai_name]["moves"]

    if not opponent_moves:
        return "defend"

    last_opponent_move = opponent_moves[-1]
    if len(opponent_moves) >= 3 and opponent_moves[-3:] == ["defend", "defend", "defend"]:
        return "rebuild"
    elif len(opponent_moves) >= 2 and opponent_moves[-2:] == ["rebuild", "rebuild"]:
        return "attack"
    elif last_opponent_move == "attack":
        return "defend"
    elif last_opponent_move == "defend":
        return "defend"
    elif last_opponent_move == "rebuild":
        return "attack"

   
    return random.choice(["attack", "defend", "rebuild"])
