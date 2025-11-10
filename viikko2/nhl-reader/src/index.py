from PlayerReader import PlayerReader
from PlayerStats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print("Players from FIN:")

    for player in players:
        print(player)

main()
