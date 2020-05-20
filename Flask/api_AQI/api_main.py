import requests

r = requests.get("https://opendata.epa.gov.tw/ws/Data/AQI/?$format=json", verify=False)
list_of_dicts = r.json()
print(type(r))
print(type(list_of_dicts))
for i in list_of_dicts:
    print(i["County"], i["SiteName"], i["PM2.5"])

    run()