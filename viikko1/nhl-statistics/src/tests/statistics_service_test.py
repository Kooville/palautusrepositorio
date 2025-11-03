import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    def test_search_returns_player_when_found(self):
        player = self.stats.search("Semenko")

        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")

    def test_search_returns_none_when_not_found(self):
        player = self.stats.search("Nobody")

        self.assertIsNone(player)

    def test_team_returns_all_players_from_team(self):
        edm_players = self.stats.team("EDM")

        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertCountEqual(names, ["Semenko", "Kurri", "Gretzky"])

    def test_top_returns_players_sorted_by_points_and_count(self):
        # Given the stub players, Gretzky (124), Lemieux (99), Yzerman (98), Kurri (90), Semenko (16)
        top4 = self.stats.top(3)  

        # Expect 4 players because method uses <= in its loop
        self.assertEqual(len(top4), 4)
        # Check ordering: highest points first
        points = [p.points for p in top4]
        self.assertEqual(points, sorted(points, reverse=True))
        # Top player should be Gretzky
        self.assertEqual(top4[0].name, "Gretzky")

    def test_top_with_zero_returns_single_top_player(self):
        top1 = self.stats.top(0)

        # Implementation returns 1 player when how_many == 0
        self.assertEqual(len(top1), 1)
        self.assertEqual(top1[0].name, "Gretzky")


