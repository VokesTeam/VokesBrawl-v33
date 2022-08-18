import json
class Players:
	try:
		settings = json.loads(open("src/config.json", 'r').read())
	except:
		settings = json.loads(open("config.json", 'r').read())

	name = settings["Name"]
	nameset = True

	profileIcon = settings["ProfileIcon"]
	nameColor = settings["NameColor"]

	trophyRoad = 200
	expPoints = 99999

	trophies = settings["Trophies"]
	highestTrophies = settings["HighestTrophies"]

	gems = settings["Gems"]
	gold = settings["Gold"]
	star = settings["Star"]

	homeBrawler = settings["HomeBrawler"]

	starPower = 76

	tutorialState = 2
	def __init__(self, device):
		self.device = device