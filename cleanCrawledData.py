import json
import sys

# args1 input file name
# args2 output file name
def main(args):    
    data = []
    with open(args[0]) as inJson:
        jsonData = json.load(inJson)
    for j in jsonData:
        temp = {}
        temp['sentiment'] = j['sentiment']
        temp['content'] = j['content']
        temp['firstpost_date'] = j['firstpost_date']
        data.append(temp)
    with open(args[1],'w') as outJson:
        json.dump(data,outJson)    


if __name__ == "__main__":
    main(sys.argv[1:])
