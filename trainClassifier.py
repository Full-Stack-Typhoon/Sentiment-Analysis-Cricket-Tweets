import sys
import re
import csv
import nltk
from nltk.corpus import stopwords
import string
import json
import team
import tweet_structure
import time
import pickle
import csv
from process_tweet import FeatureExtractor,Classifier,preProcessTweet
import pprint
import io

customstopwords = ['they', 'them']
# arg1 = trainingSet Json file
# arg2 = classifier pickle File name
def main(argv):
	trainingSet = argv[0]
	classifierFile = argv[1]
	wordlist,tweets = learnFromTrainingData(trainingSet)
	featureExtractor = FeatureExtractor(wordlist)
	training_set = nltk.classify.apply_features(featureExtractor.feature_extractor, tweets)
	# print training_set
	classifier = nltk.NaiveBayesClassifier.train(training_set)
	classifier.__class__ = Classifier
	classifier.set_feature_extractor(featureExtractor)

	with open(classifierFile, 'wb') as f:
				pickle.dump(classifier, f)
	print classifier.show_most_informative_features(n=10) 




def learnFromTrainingData(trainingSet):
	taggedSet = []
	tweets = []
	with io.open(trainingSet,encoding='ascii',errors='ignore') as jsonFile:
		jsonData = json.load(jsonFile)
        for tweet in jsonData:
                if tweet['sentiment']=='':
                        continue
                # if tweet['sentiment'] == -1:
                #        tweet['sentiment'] = 0    
                       
                tweetObjectArr = team.tagged_tweet(preProcessTweet(tweet['content'].encode('ascii',errors='replace')))
                for obj in tweetObjectArr:                        
                        taggedSet.append((obj.processed_tweet,tweet['sentiment'] ))
	for (word, sentiment) in taggedSet:
		word_filter = [i.lower().strip() for i in word.split()]
		tweets.append((word_filter, sentiment))
	wordlist = getwordfeatures(getwords(tweets))
	wordlist = [i for i in wordlist if not i in stopwords.words('english')]
	wordlist = [i for i in wordlist if not i in customstopwords]
	wordlist = [i.encode('ascii',errors='replace') for i in wordlist if len(i)>3 ]
	return wordlist,tweets

def getwords(tweets):
	allwords = []
	for (words, sentiment) in tweets:
		allwords.extend(words)
	return allwords

def getwordfeatures(listoftweets):
	wordfreq = nltk.FreqDist(listoftweets)
	words = wordfreq.keys()
	return words

if __name__ == "__main__":
	main(sys.argv[1:])
