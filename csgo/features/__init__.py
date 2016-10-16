from csgo.features.match import Match
from csgo.features.player import Player
from csgo.features.items import Items

class FeatureBase(Match, Player, Items):
    """
    This object is used to all high level functionality to CSGOClient.
    The features are seperated into submodules with a single class.
    """
    pass
