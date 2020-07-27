from django.http import HttpResponse
import urllib2
# from BeautifulSoup import *     
from urlparse import urljoin
import urllib
import time
import json
import socket
import thread

socket.setdefaulttimeout(15)

myList=["kxipvskkr","kxipvscsk","kxipvsmi","kxipvsrr","kxipvssrh","kxipvsrcb","kxipvsdd","kkrvskxip","kkrvscsk","kkrvsmi","kkrvsrr",
"kkrvssrh","kkrvsrcb","kkrvsdd","cskvskxip","cskvskkr","cskvsmi","cskvsrr","cskvssrh","cskvsrcb","cskvsdd","mivskxip","mivskkr",
"mivscsk","mivsrr","mivssrh","mivsrcb","mivsdd","rrvskxip","rrvskkr","rrvscsk","rrvsmi","rrvssrh","rrvsrcb","rrvsdd","srhvskxip",
"srhvskkr","srhvscsk","srhvsmi","srhvsrr","srhvsrcb","srhvsdd","rcbvskxip","rcbvskkr","rcbvscsk","rcbvsmi","rcbvsrr","rcbvssrh",
"rcbvsdd","ddvskxip","ddvskkr","ddvscsk","ddvsmi","ddvsrr","ddvssrh","ddvsrcb"]
urlInit = 'http://otter.topsy.com/search.js?q=%23'
k=0
mintime=1397737815
maxtime=1397824215
finalMaxtime = 1401625833
interval = 172800
urlInter='&offset='
urlFinalInter1= '&perpage=100&mintime='
urlFinalInter2='&maxtime='
urlFinalInter3='&call_timestamp=1414670323865&apikey=09C43A9B270A470B8EB8F2946A9369F3&_=1414670325449'

def crawl(urlFinal,file_suffix):
    j = 0
    res = []
    while(j<56):
        print "j number " + str(j)
        offset = 0
        while (offset < 1000):
                newUrl = urlInit + myList[j]+urlInter+str(offset) + urlFinal    
                print "crawling for links :" + newUrl
                flag=0                
                while (flag==0):
                    try:
                        print "Download Starting"
                        content = urllib2.urlopen(newUrl)
                        response = json.load(content)
                        print "Download Complete"
                        flag = 1
                    except:
                        time.sleep(1)
                i = 0
                if int(response['response']['total'])<offset:
                    break
                for i in response['response']['list']:
                    i['sentiment'] = 0
                res = res  + response['response']['list']            
                offset = offset + 100            
        j=j+1

    filename='output_'+file_suffix
    filename=filename+'.json'
    print res
    with open(filename,'w') as output:
        json.dump(res,output)
    output.close()


while(maxtime<finalMaxtime):
    k=k+1
    mintime=mintime+interval
    maxtime=maxtime+interval
    urlfinal=urlFinalInter1+str(mintime)+urlFinalInter2+str(maxtime)+urlFinalInter3
    thread.start_new_thread(crawl,(urlfinal,str(mintime) + "_" + str(maxtime)))    


while 1:
    pass