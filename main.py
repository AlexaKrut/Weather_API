import requests

res = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Russia?unitGroup=us&key=ZEPZLUFVE9T2QQTCU4VYBS7RG&contentType=json")
data = res.json()

print(data)