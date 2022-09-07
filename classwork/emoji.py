from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import json
import unicodedata as ud

def getHTML(url):
    response = requests.get(url)
    return response.text



@dataclass
class Category:
    name: str

@dataclass
class Group:
    name: str
    category : Category

@dataclass
class Emoji:
    name: str
    category : Category
    group : Group
    htmlcode : list
    unicode : list

    def prettyPrint(self):
        length = 90
        spacer = '=' * length
        emoji_properties = f"Emoji: {self.name : <30} | Group: {self.group.name: <30} | Category: {self.category.name: <30}"
        return spacer  + "\n" + emoji_properties + "\n" + spacer

    def printEmoji(self):
        emoji = self.unicode[0].replace("+", "000")
        u = emoji 
        i = int(u[1:], 16)
        c = chr(i)
        n = ud.name(c)
        return c,n 

html = getHTML("https://emojihub.herokuapp.com/api/all")


list_dict = html[1:len(html)-1].split(",{")

list_of_dicts = []
count = 0
for i in range(len(list_dict)):
    if(i == 0): 
        d = json.loads(list_dict[i])
    else:
        d = json.loads("{"+list_dict[i])
    list_of_dicts.append(d)

emoji_list = []

for dict in list_of_dicts:
    c_i = Category(dict["category"])
    g_i = Group(dict["group"], c_i)
    e_i = Emoji(dict["name"], c_i, g_i, dict["htmlCode"],  dict["unicode"])
    emoji_list.append(e_i)

print(emoji_list[100].printEmoji())