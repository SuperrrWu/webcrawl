import requests
from bs4 import BeautifulSoup
import re
import random
response = requests.get("https://so.gushiwen.org/gushi/tangshi.aspx")
soup = BeautifulSoup(response.text,"lxml")
file_path="C:/Users/Oliver/Desktop/RNN/唐诗"
for i in soup.find_all("span"):
    j=i.find_all("a")
    for k in j:
        href=k.get("href")#soup寻找href链接

    '''href=re.findall("href=...........................",str(i))
    href=href[0][6:40]'''#re正则表达式寻找href链接

    path="https://so.gushiwen.org"+href
    response=requests.get(url=path)
    soup=BeautifulSoup(response.text,"lxml")
    data=soup.find_all("div",attrs={"class":"contson"})
    for j in data:
        line=j.get_text()[1:40]
        a=random.randint(1,10000)
        file_path_new=file_path+"/"+str(a)+".txt"
        f=open(file_path_new,"w")
        f.write(line)
        f.close()
