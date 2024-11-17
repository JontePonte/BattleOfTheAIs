
from play_round import play_round

def play_match(player1, player2):
    """" play a full match between two AI players """
    player1_name = player1.__name__
    player2_name = player2.__name__

    game_info = {
        player1_name: {
            "score": 0,
            "health": 5,
            "moves": []
        },
        player2_name: {
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

        player1_score = game_info[player1_name]['score']
        player1_health = game_info[player1_name]['health']

        player2_score = game_info[player2_name]['score']
        player2_health = game_info[player2_name]['health']

        if current_round == 10:
            match_active = False
            if player1_score > player2_score:
                winner = player1_name
            elif player2_score > player1_score:
                winner = player2_name
            else:
                winner = None

        if player1_health <= 0:
            match_active = False
            winner = player2_name

        if player2_health <= 0:
            match_active = False
            winner = player1_name

        if player1_health <= 0 and player2_health <= 0:
            winner = None

        current_round += 1

    return winner, game_info
