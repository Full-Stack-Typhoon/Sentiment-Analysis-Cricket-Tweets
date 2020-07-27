import sys
import json
import fnmatch
import os

data = []
for file in os.listdir('.'):
        if fnmatch.fnmatch(file, 'output*.json'):
                print file
                with open(file,'rb') as inJson:
                        json_data = json.load(inJson)
                for k in json_data:
                        data.append(k)
                        
with open("final.json",'w') as outJson:
        json.dump(data,outJson)	
