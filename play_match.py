
from play_round import play_round

def play_match(player1, player2):
    """" play a full match between two AI players """
    game_info = {
        "player1": {
            "score": 0,
            "health": 5,
            "moves": []
        },
        "player2": {
            "score": 0,
            "health": 5,
            "moves": []
        }
    }

    current_round = 1
    match_active = True
    winner = None

    while match_active:

        player1_move = player1(game_info)
        player2_move = player2(game_info)

        game_info = play_round(player1_move, player2_move, game_info)

        player1_score = game_info['player1']['score']
        player1_health = game_info['player1']['health']

        player2_score = game_info['player2']['score']
        player2_health = game_info['player2']['health']

        if current_round == 10:
            match_active = False
            if player1_score > player2_score:
                winner = "player1"
            elif player2_score > player1_score:
                winner = "player2"
            else:
                winner = None

        if player1_health <= 0:
            match_active = False
            winner = "player2"

        if player2_health <= 0:
            match_active = False
            winner = "player1"

        if player1_health <= 0 and player2_health <= 0:
            winner = None

        current_round += 1

    return winner, game_info
