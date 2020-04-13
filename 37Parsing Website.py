import urllib.request
import urllib.parse
import re

url='https://pythonprogramming.net'
values= {'q':'basic'}

data=urllib.parse.urlencode(values)
data= data.encode('utf-8')
req=urllib.request.Request(url,data)

resp=urllib.request.urlopen(req)
respData=resp.read()

paragraph=re.findall(r'<p>(.*?)</p>',str(respData))
print(paragraph)
 
for eachp in paragraph:
    print(paragraph)
    # saveFile=open('withp.txt','w')
    # saveFile.write(str(paragraph))

input("Press any key to exit!")
