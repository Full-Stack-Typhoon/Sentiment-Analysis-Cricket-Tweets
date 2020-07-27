import tweets_structure
import tweet_structure
import tweet_to_player

mi=tweets_structure.tweets()
kkr=tweets_structure.tweets()
csk=tweets_structure.tweets()
kxip=tweets_structure.tweets()
rr=tweets_structure.tweets()
srh=tweets_structure.tweets()
dd=tweets_structure.tweets()
rcb=tweets_structure.tweets()


teams=[mi,kkr,csk,kxip,rr,srh,dd,rcb]
mi.add_names(["MI","mumbai"])
kkr.add_names(["KKR","kolkata","knight riders"])
csk.add_names(["CSK","chennai","super kings"])
kxip.add_names(["KXIP","punjab","kingsx","kings11","kings xi"])
rr.add_names(["RR","rajasthan","royals"])
srh.add_names(["SRH","hyderabad","sunrisers"])
dd.add_names(["DD","delhi","daredevils"])
rcb.add_names(["RCB","bangalore","royal challengers"])
#l=raw_input("")
conflicts=["rr","mi","dd"]
def tagged_tweet(l):
	tt=[]
	counts=[]
	dic_team_indices={}
	tweet_instances=[]
	remove_words=[]
	for i in range(1,9):
		counts.append(0)

	#f=open("Tweets.txt","r")
	#for l in f:
	tweet_instance=tweet_structure.tweets(l)
	"""for i in range(0,8):
		counts[i]=0"""
	words=l.split()
	#print words
	lowercase_tweet=l.lower()
	for team in teams:
		name=team.names[-1]
		if name in lowercase_tweet and len(name.split(" "))>1:
			#print name 
			counts[teams.index(team)]+=1
	for team in teams:
		#print team.names[0]+"sssss"
		#if counts[teams.index(team)]!=0:
			#continue
		flag=len(team.names)
		#i=0
		if len(team.names[-1].split(" "))>1:
			flag=-1
		#print flag
		name_indices=[]
		for name in team.names[:flag]:
			#print name
			i=0
			for word in words:
				if name is  word:
					print name
					counts[teams.index(team)]+=1
					remove_words.append(name)
					name_indices.append(i)
				else:
					nam=name.lower()
					word=word.lower()
					#print nam
					if (nam in word and "vs" in word) :
						#print nam
						counts[teams.index(team)]+=1
						remove_words.append(word)
					if nam==word:
						counts[teams.index(team)]+=1
						remove_words.append(word)
						name_indices.append(i)

					elif nam in word and nam not in conflicts and "vs" not in word: 
						counts[teams.index(team)]+=1
						remove_words.append(word)
						name_indices.append(i)

				i+=1
		#print name_indices
		if name_indices:
			dic_team_indices[team.names[0]]=name_indices
			#print dic_team_indices[team.names[0]]
	maximum=max(counts)
	count=0
	if maximum!=0:
		for team in teams:
			if counts[teams.index(team)]==maximum:
				#team.add_tweet(l)
				count+=1
				tweet_instance.add_team(team.names[0])
			if counts[teams.index(team)]>=1:
				tt.append(team.names[0])
	flag=0
	if count==2:
		for key in dic_team_indices:
			for key1 in dic_team_indices:
				a=dic_team_indices[key]
				b=dic_team_indices[key1]
				if dic_team_indices[key1][0]>dic_team_indices[key][0]:	
					j=0
					flag=1
					while(a[0]+1>b[j]):
						j+=1
				if flag==1:
					break
			if flag==1:
				break		
	if flag==1:
		string1=""
		string2=""
		i=0
		for p in range((a[0]+b[j])/2+1):
			#print p
			string1+=" "+words[p]
		p=(a[i]+b[j])/2+1
		while p<len(words):
			string2+=" "+words[p]
			p+=1
		#print string1
		#print string2
		tweet_instance1=tweet_structure.tweets(string1)
		tweet_instance2=tweet_structure.tweets(string2)
		tweet_instance1.add_team(key)
		tweet_instance2.add_team(key1)
		instance1,string1=tweet_to_player.player_tagging(string1,tweet_instance1.teams)
		instance2,string2=tweet_to_player.player_tagging(string2,tweet_instance2.teams)
		for word in remove_words:
			string1=string1.replace(word,"")
			string2=string2.replace(word,"")
		for i in instance1.players:
			tweet_instance1.add_player(i.names)	
		for i in instance2.players:
			tweet_instance2.add_player(i.names)	
		tweet_instance1.add_processed_tweet(string1)	
		tweet_instance1.add_processed_tweet(string2)

		return [tweet_instance1,tweet_instance2]

	else:
		
		if not tt:
			for team in teams:
				tt.append(team.names[0]) 
		#print "******"
		#print tweet_instance.teams
		#print "****"
		#print tt
		instance,l=tweet_to_player.player_tagging(l,tt)
	for word in remove_words:
		l=l.replace(word,"")
	for i in instance.players:
		tweet_instance.add_player(i.names)	
	tweet_instance.add_processed_tweet(l)	
	return [tweet_instance]
