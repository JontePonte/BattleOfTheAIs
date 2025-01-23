import inspect

def khaled(game_info):
    """
    Hyperoptimerad AI som fokuserar på att vinna alla matcher genom dynamiska strategier och adaptivt beteende.
    """

    # Unpack game info
    my_health, my_moves = None, None
    opponent_health, opponent_moves = None, None

    for ai_name in game_info:
        if ai_name == inspect.currentframe().f_code.co_name:
            my_health = game_info[ai_name]['health']
            my_moves = game_info[ai_name]['moves']
        else:
            opponent_health = game_info[ai_name]['health']
            opponent_moves = game_info[ai_name]['moves']

    # Analysera motståndarens senaste och vanligaste drag
    most_common_move = None
    if opponent_moves:
        most_common_move = max(set(opponent_moves), key=opponent_moves.count)
        last_move = opponent_moves[-1]
    else:
        last_move = None

    # Dynamisk strategi baserad på hälsa och mönsterigenkänning
    if opponent_health <= 3:
        # Attackera direkt om motståndaren har mycket låg hälsa
        return "attack"

    if my_health <= 2:
        # Om min hälsa är mycket låg, prioritera att återhämta eller skydda
        if last_move == "attack":
            return "defend"
        return "rebuild"

    if my_health > opponent_health:
        # Om jag har mer hälsa, attackera direkt
        return "attack"

    if most_common_move == "attack":
        # Om motståndaren attackerar ofta, balansera mellan rebuild och defend
        if my_health < 4:
            return "rebuild"
        return "defend"

    if most_common_move == "rebuild":
        # Exploatera rebuild-strategi genom att attackera aggressivt
        return "attack"

    if most_common_move == "defend":
        # Bygg upp hälsa om motståndaren försvarar mycket, annars attackera
        if my_health < 6:
            return "rebuild"
        return "attack"

    if last_move in ["attack", "defend", "rebuild"] and most_common_move is None:
        # Om motståndaren spelar slumpmässigt, attackera smart men med viss säkerhet
        if my_health > 5:
            return "attack"
        return "rebuild"

    # Standarddrag: attackera som sista utväg
    return "attack"
