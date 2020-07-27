class tweets(object):
	def __init__(self,string):
		self.tweet=string
		self.teams=[]
		self.players=[]
		self.processed_tweet=""
                self.sentiment = 0
                self.timestamp = 0
	def add_team(self,team):
		self.teams.append(team)

	def add_player(self,player):
		self.players.append(player)

	def add_processed_tweet(self,string):
		self.processed_tweet=string
                
        def to_json(self):
                return vars(self)
