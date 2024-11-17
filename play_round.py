


def play_round(player1_move, player2_move, game_info):
    """Play one round between player 1 and player 2"""

    player1_name = list(game_info.keys())[0]
    player2_name = list(game_info.keys())[1]

    # Unpack game info
    player1_score = game_info[player1_name]['score']
    player1_health = game_info[player1_name]['health']
    player1_moves = game_info[player1_name]['moves']

    player2_score = game_info[player2_name]['score']
    player2_health = game_info[player2_name]['health']
    player2_moves = game_info[player2_name]['moves']


    # Attack vs Attack
    if player1_move == "attack" and player2_move == "attack":
        player1_score += 1
        player1_health -= 1
        player1_moves.append("attack")

        player2_score += 1
        player2_health -= 1
        player2_moves.append("attack")


    # Attack vs Defend
    elif player1_move == "attack" and player2_move == "defend":
        player1_score += 1
        player1_health -= 2
        player1_moves.append("attack")

        player2_score += 0
        player2_health += 0
        player2_moves.append("defend")


    elif player1_move == "defend" and player2_move == "attack":
        player1_score += 0
        player1_health += 0
        player1_moves.append("defend")

        player2_score += 1
        player2_health -= 2
        player2_moves.append("attack")



    # Defend vs Defend
    elif player1_move == "defend" and player2_move == "defend":
        player1_score += 0
        player1_health += 1
        player1_moves.append("defend")

        player2_score += 0
        player2_health += 1
        player2_moves.append("defend")


    # Store new game info
    new_game_info = {
        player1_name: {
            "score": player1_score,
            "health": player1_health,
            "moves": player1_moves
        },
        player2_name: {
            "score": player2_score,
            "health": player2_health,
            "moves": player2_moves
        }
    }

    return new_game_info

