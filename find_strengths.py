import csv

filepath = "goal_stats.csv"

with open(filepath, mode="r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    teams = [row for row in reader]

for team in teams:
    team["Home offense strength"] = round(float(team["Home goals"])/float(teams[-1]["Home goals"]), 2)
    team["Home defense strength"] = round(float(team["Home conceded"])/float(teams[-1]["Home conceded"]), 2)
    team["Away offense strength"] = round(float(team["Away goals"])/float(teams[-1]["Away goals"]), 2)
    team["Away defense strength"] = round(float(team["Away conceded"])/float(teams[-1]["Away conceded"]), 2)

print(teams)

with open(filepath, mode="w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=teams[0].keys(), lineterminator="\n")
    writer.writeheader()
    writer.writerows(teams)