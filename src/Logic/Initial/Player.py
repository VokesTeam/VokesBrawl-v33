class Players:

	name = "Player"
	nameset = True

	profileIcon = 0
	nameColor = 0

	trophyRoad = 200
	expPoints = 99999

	trophies = 99999
	highestTrophies = 99999

	gems = 99999
	gold = 99999
	star = 99999

	homeBrawler = 44

	tutorialState = 2
	def __init__(self, device):
		self.device = device