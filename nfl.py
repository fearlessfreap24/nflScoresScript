from flask import Flask
import xml.etree.ElementTree as ET
import requests

app = Flask(__name__)

x = requests.get("http://www.nfl.com/liveupdate/scorestrip/ss.xml")

tree = ET.fromstring(x.text)

gms = tree[0]

ret = '''<table><tr><th>Home Team</th><th>Away Team</th><th>Score</th><th>Quarter</th></tr>'''

for g in gms:
#     print(g.tag)
    ret = ret + "<tr><td>Home: {:<20}</td><td>Away: {:<20}</td><td>Score: {:<2} - {:<2}</td><td>".format(g.attrib['hnn'].capitalize(),
        g.attrib['vnn'].capitalize(), g.attrib['hs'], g.attrib['vs'])
    if g.attrib['q'] == "F":
        ret = ret + " -- Final</td></tr>"
    elif g.attrib['q'] == "FO":
        ret = ret + " -- Final - Overtime</td></tr>"
    elif g.attrib['q'] == 'H':
        ret = ret + " -- Haftime</td></tr>"
    elif g.attrib['q'] == '1' or g.attrib['q'] == '2' or g.attrib['q'] == '3' or g.attrib['q'] == '4':
        ret = ret + " quarter: {} - {}</td></tr>".format(g.attrib['q'], g.attrib['k'])
    else:
        ret = ret + " quarter: {}</td></tr>".format(g.attrib['q'])

ret = ret + "</table>"

@app.route('/nfl')
def nfl():
    return ret

