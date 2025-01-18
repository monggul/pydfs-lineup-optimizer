from typing import Type
from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.rules import FanduelSingleGameMaxQBRule
from pydfs_lineup_optimizer.sites.yahoo.classic.importer import YahooCSVImporter, YahooMVPCSVImporter
from pydfs_lineup_optimizer.sites.yahoo.single_game.importer import build_yahoo_single_game_importer, \
    YahooSingleGameFooballCSVImporter
from pydfs_lineup_optimizer.lineup_exporter import YahooCSVLineupExporter


class YahooSingleGameSettings(BaseSettings):
    site = Site.YAHOO_SINGLE_GAME
    budget = 200
    max_from_one_team = 4
    csv_importer = YahooMVPCSVImporter  # type: Type[FanDuelCSVImporter]
    csv_exporter = YahooCSVLineupExporter


@SitesRegistry.register_settings
class YahooSingleGameFootballSettings(YahooSingleGameSettings):
    sport = Sport.FOOTBALL
    extra_rules = [FanduelSingleGameMaxQBRule]
    budget = 115
    positions = [
        LineupPosition('MVP', ('MVP', )),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K', 'DEF')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K', 'DEF')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K', 'DEF')),
        LineupPosition('FLEX', ('QB', 'WR', 'RB', 'TE', 'K', 'DEF')),
    ]

#
@SitesRegistry.register_settings
class FanDuelSingleGameBasketballSettings(YahooSingleGameSettings):
    sport = Sport.BASKETBALL
    budget = 150
    csv_importer = build_yahoo_single_game_importer(mvp=True, star=True, pro=True)
    positions = [
        LineupPosition('MVP', ('MVP', )),
        LineupPosition('STAR', ('STAR', )),
        LineupPosition('PRO', ('PRO', )),
        LineupPosition('UTIL', ('PG', 'SG', 'SF', 'PF', 'C')),
        LineupPosition('UTIL', ('PG', 'SG', 'SF', 'PF', 'C')),
    ]

#
@SitesRegistry.register_settings
class YahooSingleGameBaseballSettings(YahooSingleGameSettings):
    sport = Sport.BASEBALL
    budget = 75
    csv_importer = build_yahoo_single_game_importer(mvp=True, star=True, pro=False)
    positions = [
        LineupPosition('MVP', ('MVP', )),
        LineupPosition('STAR', ('STAR', )),
        LineupPosition('UTIL', ('1B', '2B', '3B', 'SS', 'OF', 'C')),
        LineupPosition('UTIL', ('1B', '2B', '3B', 'SS', 'OF', 'C')),
        LineupPosition('UTIL', ('1B', '2B', '3B', 'SS', 'OF', 'C')),
    ]

#
# @SitesRegistry.register_settings
# class FanDuelSingleGameHockeySettings(FanDuelSingleGameSettings):
#     sport = Sport.HOCKEY
#     csv_importer = FanDuelSingleGameHockeyCSVImporter
#     positions = [
#         LineupPosition('CAPTAIN', ('CAPTAIN', )),
#         LineupPosition('UTIL', ('C', 'W', 'D')),
#         LineupPosition('UTIL', ('C', 'W', 'D')),
#         LineupPosition('UTIL', ('C', 'W', 'D')),
#         LineupPosition('UTIL', ('C', 'W', 'D')),
#     ]
