import re
import nltk
import csv
import string
emoticons = {}
acronyms = {}

def buildEmoticonStore():
	with open('emoticons.csv','rb') as csvFile:
		emReader = csv.reader(csvFile, delimiter = ' ')
		for row in emReader:
			emoticons[row[0]] = row[1]



def buildAcronymStore():
	with open('acronym.csv','rb') as csvFile:
		acReader = csv.reader(csvFile,delimiter=',')
		for row in acReader:
			acronyms[row[0]] = row[1]

buildAcronymStore()
buildEmoticonStore()

def preProcessTweet(tweet):
    tweet = tweet.lower()
    res = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '||u||', tweet)
    for key in emoticons:
        if key in res.split():
            rep = ""
            if emoticons[key] > 0 :
                rep = "||pe||"
            elif emoticons[key] < 0:
                rep = "||ne||"
            else:
                rep = "||nue||"
            res = string.replace(res,key,rep)
    for key in acronyms:
        res = res.replace(" "+key+" "," "+acronyms[key]+" ")
    punctuations = string.punctuation
    valid_punctuations = '#!'
    token_punctuations = '!'
    for punctuation in valid_punctuations:
        punctuations = punctuations.replace( punctuation,'')

    for punctuation in punctuations:
        res = res.replace(punctuation,' ')

    for punctuation in token_punctuations:
        res = res.replace(punctuation, ' ' + punctuation + ' ' )
    return res

class FeatureExtractor:
        def __init__(self,wordset):
                self.wordset = wordset

	def feature_extractor(self,doc):
		docwords = set(doc)
		features = {}                
		for i in self.wordset:
			features['contains(%s)' % i] = (i in docwords)
		return features

class Classifier(nltk.NaiveBayesClassifier):

    def set_feature_extractor(self, feature_extractor):
        self.feature_extractor = feature_extractor
