import sys
import re
import json

filename = "output_1398256215_1398342615.json"
with open(filename,'rb') as inJson:
	jsonData = json.load(inJson)

count = 0
i = 0
data = []
for k in jsonData:
	if(count>100):
		count = 0
		i+=1
		with open(filename.split('.')[0] + "_"+ str(i) + ".json",'w') as outJson:
			json.dump(data,outJson)
		outJson.close()
		data = []
	data.append(k)
	count+=1

