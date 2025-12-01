class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1
        else:
            raise ValueError("Unknown player name")

    def _score_name(self, score):
        return self.SCORE_NAMES.get(score, "")

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._get_tied_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._get_deuce_or_advantage_score()
        else:
            return self._get_regular_score()

    def _get_tied_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def _get_deuce_or_advantage_score(self):
        score_diff = self.m_score1 - self.m_score2
        if score_diff == 1:
            return "Advantage player1"
        elif score_diff == -1:
            return "Advantage player2"
        elif score_diff >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_regular_score(self):
        return f"{self._score_name(self.m_score1)}-{self._score_name(self.m_score2)}"
