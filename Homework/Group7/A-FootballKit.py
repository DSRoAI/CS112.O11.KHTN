# Input number of team
number_team = int(input())
team_kits = []
for _ in range(number_team):
    # Input number of home kit and away kit
    x_i, y_i = map(int, input().split())
    team_kits.append((x_i, y_i))

home_kit_count = [0] * 10**6
# Create list of number of each type of kit
for home_kit, _ in team_kits:
    home_kit_count[home_kit] += 1
    
for _ , away_kit in team_kits:
    home_count = number_team + home_kit_count[away_kit] - 1
    away_count = number_team - home_kit_count[away_kit] - 1
    print(home_count, away_count)