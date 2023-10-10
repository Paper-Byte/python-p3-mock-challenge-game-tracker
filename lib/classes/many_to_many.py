from typing import Any


class Game:

    all = []

    def __init__(self, title):
        if ((isinstance(title, str)) and (len(title) > 0)):
            self._title = title
            Game.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (not hasattr(self, self.title)):
            if ((isinstance(title, str)) and (len(title) > 0)):
                self._title = title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(set(result.player for result in Result.all if result.game is self))

    def average_score(self, player):
        scores = [
            result.score for result in Result.all if result.game is self and result.player == player]
        average = 0
        for score in scores:
            average += score
        return float(average / len(scores))


class Player:

    all = []

    def __init__(self, username):
        if ((isinstance(username, str)) and (2 < len(username) < 16)):
            self._username = username
            Player.all.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if ((isinstance(username, str)) and (2 < len(username) < 16)):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(set([result.game for result in Result.all if result.player is self]))

    def played_game(self, game):
        return (game in self.games_played())

    def num_times_played(self, game):
        return len([result.game for result in Result.all if result.player is self and result.game == game])


class Result:

    all = []

    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if (isinstance(player, Player)):
            self._player = player

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if (isinstance(game, Game)):
            self._game = game

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if (not hasattr(self, str(self.score))):
            if (isinstance(score, int) and (1 < score < 5000)):
                self._score = score
