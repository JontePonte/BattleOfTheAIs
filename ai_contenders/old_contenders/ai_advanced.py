import inspect

def advanced(game_info):
    """Advanced AI that adjusts its strategy based on game state and opponent behavior"""
    
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
    
    # Förinställning av action till en standard
    action = None

    # Strategi baserad på hälsa och poängdifferens
    if my_health <= 2:
        action = "defend"  # Skydda sig om AI:n har låg hälsa
    elif opponent_health <= 1:
        action = "attack"  # Försök avsluta spelet om motståndaren har låg hälsa
    elif my_score > opponent_score and my_health > opponent_health:
        action = "attack"  # Håll ledningen genom att fortsätta attackera
    elif my_health < opponent_health:
        action = "defend"  # Om motståndaren har bättre hälsa, spela försiktigt
    
    # Analysera motståndarens senaste drag
    if len(opponent_moves) >= 2:
        if opponent_moves[-1] == "attack" and opponent_moves[-2] == "attack":
            action = "defend"  # Försvara om motståndaren har visat sig vara aggressiv
        elif opponent_moves[-1] == "defend" and opponent_moves[-2] == "defend":
            action = "attack"  # Utnyttja om motståndaren spelar defensivt
    
    # Standardåtgärd om ingen av de andra villkoren uppfylls
    if action is None:
        action = "attack" if len(my_moves) % 2 == 0 else "defend"  # Växla drag som backup-strategi
    
    return action
