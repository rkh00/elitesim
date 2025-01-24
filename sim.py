import csv

filepath = "teams.csv"

with open(filepath, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    teams = [row for row in reader]

print(teams)

# non-weighted model

# tanh model

# poisson model