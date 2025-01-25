import csv
import random
import pandas as pd

filepath = "teams.csv"

with open(filepath, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    teams = [row for row in reader]

# print(teams)

abbs = [team["Abbreviation"] for team in teams]
# print(abbs)

cols = ["Team", "W", "D", "L", "P"]
league_table = pd.DataFrame(columns=cols)
league_table["Team"] = abbs
league_table = league_table.fillna(0)

# print(league_table)

# non-weighted model
for home_team in abbs:
    for away_team in abbs:
        if home_team == away_team:
            continue
        result = random.choice(["H", "D", "A"])
        match result:
            case "H":
                league_table.loc[league_table["Team"] == home_team, "W"] += 1
                league_table.loc[league_table["Team"] == home_team, "P"] += 3
                league_table.loc[league_table["Team"] == away_team, "L"] += 1
            case "D":
                league_table.loc[league_table["Team"] == home_team, "D"] += 1
                league_table.loc[league_table["Team"] == home_team, "P"] += 1
                league_table.loc[league_table["Team"] == away_team, "D"] += 1
                league_table.loc[league_table["Team"] == away_team, "P"] += 1
            case "A":
                league_table.loc[league_table["Team"] == home_team, "L"] += 1
                league_table.loc[league_table["Team"] == away_team, "W"] += 1
                league_table.loc[league_table["Team"] == away_team, "P"] += 3
            
league_table = league_table.sort_values(by=["P",],ascending=False)
league_table = league_table.reindex()
print(league_table)

# tanh model


# poisson model

