import pandas as pd

# Exempeldata: Resultat från matcher
results = {
    1: {1: "-", 2: "W", 3: "L"},
    2: {1: "L", 2: "-", 3: "W"},
    3: {1: "W", 2: "L", 3: "-"}
}

# Exempeldata: Spelarnamn
players = {
    1: {"name": "first"},
    2: {"name": "aggressor"},
    3: {"name": "super_aggressor"},
}

# Förbered data för tabellen
player_names = [players[p]["name"] for p in players]
table_data = [[results[row][col] for col in results[row]] for row in results]

# Skapa en DataFrame
df = pd.DataFrame(table_data, index=player_names, columns=player_names)

# Visa tabellen
print("Match Results:")
print(df)
