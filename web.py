import webbrowser
import requests
res=requests.get('http://192.168.23.72:8080/apk')
print(res.status_code==requests.code.ok)
#webbrowser.open('http://baidu.com')