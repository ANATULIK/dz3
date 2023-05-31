class Dryg:
    def __init__(self, name='Dryg'):
        self.name = name


class Gaming:
    def __init__(self, game):
        self.game = game
        self.players = []

    def add_players(self, *dryzia):
        self.players += dryzia

    def print_players(self):
        if self.players:
            print(f'Name of players in{self.game}:')
            for p in self.players:
                print(p.name)
        else:
            print(f'Nobody plays in{self.game}:')

dedlyParkurKilerDarkBrawlStarsAsasinStalkerSniper1988 = Dryg('dedlyParkurKilerDarkBrawlStarsAsasinStalkerSniper1988')
GIDROKSIMETILHINOKSILINDIOKSID = Dryg('GIDROKSIMETILHINOKSILINDIOKSID')
Anton = Dryg('Anton')
game = Gaming('Counter-Strike: Global Offensive')
game.add_players(dedlyParkurKilerDarkBrawlStarsAsasinStalkerSniper1988, GIDROKSIMETILHINOKSILINDIOKSID, Anton)
game.print_players()