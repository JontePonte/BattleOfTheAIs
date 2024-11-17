"""
Tournament Simulation for AI Players

This module simulates a tournament where AI players compete against each other in pairwise matches.
Each AI is represented by a function that decides whether to "attack" or "defend" based on game state.
[cue DOOM music]
"""

import pandas as pd


from play_match import play_match
from registry import ai_registry

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
winner, game_info = None, None

for player1_id, player1_data in players.items():
    for player2_id, player2_data in players.items():
        if player1_id < player2_id:  # Avoid double matches and self matches
            winner, game_info = play_match(player1_data["AI"], player2_data["AI"])

            if winner == player1_data["name"]:
                player1_data["wins"] += 1
                player2_data["loses"] += 1
                results[player1_id][player2_id] = "W"  # Win för player1
                results[player2_id][player1_id] = "L"  # Loss för player2
            elif winner == player2_data["name"]:
                player1_data["loses"] += 1
                player2_data["wins"] += 1
                results[player1_id][player2_id] = "L"  # Loss för player1
                results[player2_id][player1_id] = "W"  # Win för player2
            else:  # Draw
                player1_data["draws"] += 1
                player2_data["draws"] += 1
                results[player1_id][player2_id] = "D"  # Draw
                results[player2_id][player1_id] = "D"  # Draw


for player_id, stats in players.items():
    print(f"Player {player_id} ({stats['AI'].__name__}): Wins: {stats['wins']}, \
Losses: {stats['loses']}, Draws: {stats['draws']}")

# Find the maximum number of wins
max_wins = max(player["wins"] for player in players.values())
# Find all AIs with the maximum wins (in case of a tie)
total_winners = [player["name"] for player in players.values() if player["wins"] == max_wins]

# Print the total winners
if len(total_winners) > 1:
    print(f"\nTotal Tournament Winners (tied): {', '.join(total_winners)} with {max_wins} wins each")
else:
    print(f"\nTotal Tournament Winner: {total_winners[0]} with {max_wins} wins")


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
