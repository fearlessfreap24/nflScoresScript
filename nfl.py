import xml.etree.ElementTree as ET
import requests

x = requests.get("http://www.nfl.com/liveupdate/scorestrip/ss.xml")

tree = ET.fromstring(x.text)

gms = tree[0]

for g in gms:
#     print(g.tag)
    print("Home: {:<20} Away: {:<20} Score: {:<2} - {:<2}".format(g.attrib['hnn'].capitalize(),
        g.attrib['vnn'].capitalize(), g.attrib['hs'], g.attrib['vs']), end="")
    if g.attrib['q'] == "F":
        print(" -- Final")
    else:
        print(" quarter: {}".format(g.attrib['q']))

