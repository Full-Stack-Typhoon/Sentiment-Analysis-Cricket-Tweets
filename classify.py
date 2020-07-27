import pickle
import json
import sys
import trainClassifier
from process_tweet import preProcessTweet
import team
import time


# arg1 = classifier pickle File name
# arg2 = testSet Json file
# arg3 = output fileName
def main(args):
    classifierFile = args[0]
    inputFile = args[1]
    outputFile = args[2]

    with open(classifierFile,'rb') as f:
        classifier = pickle.load(f)

    with open(inputFile) as itReader:
        inputJsonTweet = json.load(itReader)
    count = 0
    data = []
    for line in inputJsonTweet:
        # if count > 1000:
        #     count = 0
        #     filename = "output_" + str(int(time.time()))
        #     with open(filename+".json",'w') as outJson:
        #         json.dump(data,outJson)
        #     outJson.close()
        #     data = []
        tweetString = preProcessTweet(line['content'])
        tweetObjectArr = team.tagged_tweet(tweetString)
        for tweetObject in tweetObjectArr:
            temp = tweetObject.processed_tweet
            temp = temp.lower()
            temp = temp.split()
            tweetObject.sentiment = classifier.classify(classifier.feature_extractor.feature_extractor(temp))
            tweetObject.timestamp = line['firstpost_date']
            data.append(vars(tweetObject))
            count += 1
    with open(outputFile,'w') as outJson:
        json.dump(data,outJson)        
if __name__ == "__main__":
    main(sys.argv[1:])
