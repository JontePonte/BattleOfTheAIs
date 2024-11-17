
import pandas as pd
from play_match import play_match

from ai_full_random import full_random
from ai_aggressor import aggressor
from ai_super_aggressor import super_aggressor
from ai_super_defender import super_defender


# All condenders are added here
ai_registry = {
    "full_random": full_random,
    "aggressor": aggressor,
    "super_aggressor": super_aggressor,
    "super_defender": super_defender,
}

# Infomation 
players = {}
for idx, (name, ai_function) in enumerate(ai_registry.items(), start=1):
    players[idx] = {
        "AI": ai_function,
        "name": name,
        "wins": 0,
        "loses": 0,
        "draws": 0,
    }



# Initialize result matrix
results = {p1: {p2: None for p2 in players} for p1 in players}

for player1_id, player1_data in players.items():
    for player2_id, player2_data in players.items():
        if player1_id < player2_id:  # Avoid double matches and self matches
            winner, game_info = play_match(player1_data["AI"], player2_data["AI"])

            if winner == player1_data["name"]:
                players[player1_id]["wins"] += 1
                players[player2_id]["loses"] += 1
                results[player1_id][player2_id] = "W"  # Win för player1
                results[player2_id][player1_id] = "L"  # Loss för player2
            elif winner == player2_data["name"]:
                players[player2_id]["wins"] += 1
                players[player1_id]["loses"] += 1
                results[player1_id][player2_id] = "L"  # Loss för player1
                results[player2_id][player1_id] = "W"  # Win för player2
            else:  # Draw
                players[player1_id]["draws"] += 1
                players[player2_id]["draws"] += 1
                results[player1_id][player2_id] = "D"  # Draw
                results[player2_id][player1_id] = "D"  # Draw


for player_id, stats in players.items():
    print(f"Player {player_id} ({stats['AI'].__name__}): Wins: {stats['wins']}, Losses: {stats['loses']}, Draws: {stats['draws']}")


# Create a DataFrame for resultat
player_names = [player_data["name"] for player_data in players.values()]
result_matrix = [[results[p1][p2] if p1 != p2 else "-" for p2 in players] for p1 in players]

# Pandas DataFrame
df_results = pd.DataFrame(result_matrix, index=player_names, columns=player_names)

# Print the table
print("\nMatch Results Table:")
print(df_results)

# Export table to csv and html
df_results.to_csv("match_results.csv", index=True)
df_results.to_html("match_results.html")
