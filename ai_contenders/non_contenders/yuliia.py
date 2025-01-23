import inspect

def Yuliias_AI(game_info):

    # Unpack game info
    my_health, my_moves = None, []
    opponent_health, opponent_moves = None, []
    
    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    # Analyze opponent's recent behavior
    recent_opponent_moves = opponent_moves[-4:] if opponent_moves else []
    opponent_last_move = opponent_moves[-1] if opponent_moves else None

    # Counter strategies
    if my_health <= 2:
        # Prioritize survival
        return "defend" if opponent_last_move == "attack" else "rebuild"
    elif opponent_health <= 2:
        # Finish them off
        return "attack"
    elif recent_opponent_moves.count("defend") >= 2:
        # Exploit over-defensiveness
        return "rebuild"
    elif recent_opponent_moves.count("rebuild") >= 2:
        # Punish rebuilding
        return "attack"
    elif opponent_last_move == "attack":
        # React aggressively if they've attacked
        if my_health > 2:
            return "attack"
        else:
            return "defend"
    elif opponent_last_move == "defend":
        # Rebuild when opponent defends excessively
        return "rebuild"
    elif opponent_last_move == "rebuild":
        # Attack during rebuilding
        return "attack"
    else:
        # Balanced fallback strategy
        if my_health > opponent_health + 1:
            return "attack"
        elif my_health <= opponent_health:
            return "defend"
        else:
            return "rebuild"
