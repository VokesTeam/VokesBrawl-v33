class Device:
	AndroidID = None
	DeviveModel = None
	OpenUDID = None
	OSVersion = None
	isAndroid = False
	Language = None
	
	def __init__(self, socket):
		self.socket = socket