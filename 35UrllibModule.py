import urllib.request
import urllib.parse
# x=urllib.request.urlopen('https://www.google.com')
# print(x.read())
'''
url='https://pythonprogramming.net'
values= {'q':'basic'}

data=urllib.parse.urlencode(values)
data= data.encode('utf-8')
req=urllib.request.Request(url,data)

resp=urllib.request.urlopen(req)
print(resp.read())
'''

# try:
#     x = urllib.request.urlopen('https://www.google.com/search?q=test')
#     print(x.read())

# except Exception as e:
#     print(str(e))

try:
    url='https://www.google.com/search?q=test'
    
    header={}
    header['User-Agent']='	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    req=urllib.request.Request(url,headers=header)
    resp=urllib.request.urlopen(req)

    respData=resp.read()
    print(respData)

    # saveFile=open('withHeaders.txt','w')
    # saveFile.write(str(respData))

except Exception as e:
    print(str(e))