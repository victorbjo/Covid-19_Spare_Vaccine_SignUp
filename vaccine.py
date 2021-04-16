import requests
from bs4 import BeautifulSoup as bs

URL = 'https://skema.rn.dk/servlet/com.pls.morpheus.web.pages.CoreRespondentCollectLinkAnonymous'
myobj = {'initialposts':'initialposts',
         'c':'NNX2AGF6JK35',
         'media':'web-collect-normal'}
#print(myobj)
page = requests.post(URL, data=myobj)
#print(page.content)
soup = bs(page.content,'html.parser')
results=soup.find_all('label')
nonLocations = ["Ja","Nej","Ved ikke"]
chosenSpot = 0
print("Available locations for vaccination:")
for result in results:
    if (result.text not in nonLocations ):
        if result.text.find("9000") != -1:
            chosenSpot = result
        print(result.text)

print("\nSigning up for vaccination @ "+chosenSpot.text+"\n")
location = str(chosenSpot)
location = location[location.find('"')+1:location.find('>')-1]
location = location[location.find("-")+1:]

results = soup.find_all('input')
postIDs = ["questionnaireid","uuid","media","rid"]
postDataTemp = {"t337561910":"Victor+Bjørholm","n337561915":"21",
            "t337561922":"42803084","c337561929":location,
            "pageindex":"0", "fv":"no/", "next":"Næste",
            "media":"web-collect-normal", "c1601148219":"1601148222"}

for result in results:
        if result.attrs["name"] in postIDs:
            #print(vars(result))
            #print(result.attrs["name"]+" : "+result.attrs["value"])
            postDataTemp[result.attrs["name"]] = result.attrs["value"]

postData = {"questionnaireid":postDataTemp["questionnaireid"],"pageindex":postDataTemp["pageindex"],"fv":postDataTemp["fv"],
            "c1601148219":postDataTemp["c1601148219"],"t337561910":postDataTemp["t337561910"],"n337561915":postDataTemp["n337561915"],
            "t337561922":postDataTemp["t337561922"],"c337561929":postDataTemp["c337561929"],"next":postDataTemp["next"],
            "uuid":postDataTemp["uuid"],"media":postDataTemp["media"],"rid":postDataTemp["rid"]}
for x in postData:
    print(x+": "+postData[x] )
page = requests.post(URL, data=postData)
soup = bs(page.content,'html.parser')
result=soup.find('form')
print(result.text)
#print(postData)
