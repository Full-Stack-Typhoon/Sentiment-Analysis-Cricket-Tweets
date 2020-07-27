class tweets(object):
	def __init__(self):
		self.count=0
		self.tweets=[]
		self.names=[]

	def add_tweet(self,tweet):
		self.tweets.append(tweet)
		self.count+=1

	def add_names(self,team_names):
		for name in team_names:
			self.names.append(name)
		