from pydfs_lineup_optimizer.settings import BaseSettings, LineupPosition
from pydfs_lineup_optimizer.constants import Sport, Site
from pydfs_lineup_optimizer.sites.sites_registry import SitesRegistry
from pydfs_lineup_optimizer.sites.draftkings.captain_mode.importer import DraftKingsCaptainModeCSVImporter


POSITIONS_WITH_FLEX = [
    LineupPosition('CPT', ('CPT',)),
    LineupPosition('FLEX', ('FLEX','F',)),
    LineupPosition('FLEX', ('FLEX','F',)),
    LineupPosition('FLEX', ('FLEX','F',)),
    LineupPosition('FLEX', ('FLEX','F',)),
    LineupPosition('FLEX', ('FLEX','F',)),
]


class DraftKingsCaptainModeSettings(BaseSettings):
    site = Site.DRAFTKINGS_CAPTAIN_MODE
    budget = 50000
    max_from_one_team = 5
    csv_importer = DraftKingsCaptainModeCSVImporter
    positions = [
        LineupPosition('CPT', ('CPT',)),
        LineupPosition('UTIL', ('UTIL',)),
        LineupPosition('UTIL', ('UTIL',)),
        LineupPosition('UTIL', ('UTIL',)),
        LineupPosition('UTIL', ('UTIL',)),
        LineupPosition('UTIL', ('UTIL',)),
    ]


@SitesRegistry.register_settings
class DraftKingsCaptainModeFootballSettings(DraftKingsCaptainModeSettings):
    sport = Sport.FOOTBALL
    positions = POSITIONS_WITH_FLEX[:]


@SitesRegistry.register_settings
class DraftKingsCaptainModeBasketballSettings(DraftKingsCaptainModeSettings):
    sport = Sport.BASKETBALL


@SitesRegistry.register_settings
class DraftKingsLOLSettings(DraftKingsCaptainModeSettings):
    sport = Sport.LEAGUE_OF_LEGENDS
    max_from_one_team = 4
    min_games = 2
    positions = [
        LineupPosition('CPT', ('CPT', )),
        LineupPosition('TOP', ('TOP', )),
        LineupPosition('JNG', ('JNG', )),
        LineupPosition('MID', ('MID', )),
        LineupPosition('ADC', ('ADC', )),
        LineupPosition('SUP', ('SUP', )),
        LineupPosition('TEAM', ('TEAM', )),
    ]

@SitesRegistry.register_settings
class DraftKingsCaptainModeLOLSettings(DraftKingsCaptainModeSettings):
    sport = Sport.LEAGUE_OF_LEGENDS_SINGLE
    max_from_one_team = 2
    positions = [
        LineupPosition('CPT', ('CPT','ADC','MID',)),
        LineupPosition('CPT', ('CPT','ADC','MID','JNG','TOP',)),
        LineupPosition('FLEX', ('FLEX','ADC','MID','JNG','TOP','TEAM','SUP',)),
        LineupPosition('FLEX', ('FLEX','ADC','MID','JNG','TOP','TEAM','SUP',)),
    ]


@SitesRegistry.register_settings
class DraftKingsCaptainModeBaseballSettings(DraftKingsCaptainModeSettings):
    sport = Sport.BASEBALL


@SitesRegistry.register_settings
class DraftKingsCaptainModeWNBASettings(DraftKingsCaptainModeSettings):
    sport = Sport.WNBA


@SitesRegistry.register_settings
class DraftKingsCaptainModeSoccerSettings(DraftKingsCaptainModeSettings):
    sport = Sport.SOCCER
    positions = POSITIONS_WITH_FLEX[:]


@SitesRegistry.register_settings
class DraftKingsCaptainModeNHLSettings(DraftKingsCaptainModeSettings):
    sport = Sport.HOCKEY
    positions = POSITIONS_WITH_FLEX[:]

@SitesRegistry.register_settings
class DraftKingsCaptainModeMMASettings(DraftKingsCaptainModeSettings):
    sport = Sport.MMA
    max_from_one_team = None
    positions = POSITIONS_WITH_FLEX[:]

@SitesRegistry.register_settings
class DraftKingsCaptainModeGolfSettings(DraftKingsCaptainModeSettings):
    sport = Sport.GOLF
    max_from_one_team = None
    positions = [
        LineupPosition('CPT', ('CPT',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
        LineupPosition('G', ('G',)),
    ]
@SitesRegistry.register_settings
class DraftKingsCaptainModeF1Settings(DraftKingsCaptainModeSettings):
    sport = Sport.F1
    max_from_one_team = 2
    positions = [
        LineupPosition('CPT', ('CPT', )),
        LineupPosition('D', ('D', )),
        LineupPosition('D', ('D', )),
        LineupPosition('D', ('D', )),
        LineupPosition('D', ('D', )),
        LineupPosition('CNSTR', ('CNSTR', )),
    ]

@SitesRegistry.register_settings
class DraftKingsCaptainModeCBBSettings(DraftKingsCaptainModeSettings):
    sport = Sport.CBB
