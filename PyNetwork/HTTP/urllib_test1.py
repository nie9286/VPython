from urllib.request import urlopen
import json

response = urlopen('http://www.baidu.com',timeout=30)

json_response = json.loads(response.read())

