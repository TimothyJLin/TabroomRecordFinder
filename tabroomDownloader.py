import sys
from bs4 import BeautifulSoup
import requests
#downloads the tournament records from tabroom in order to query
def start():
    updatedURL=""
    url="https://www.tabroom.com/index/results/team_results.mhtml?id1=1"
    for i in range (1, 1516497):
        #check if user exists
        #i=1143532
        updatedURL="https://www.tabroom.com/index/results/team_results.mhtml?id1="+str(i)
        page=requests.get(updatedURL)
        soup=BeautifulSoup(page.text, 'html')
        soupElements=soup.find_all("h6")
        if len(soupElements)>1:
            if soupElements[1].get_text().find("No student found for id")>-1:
                #print("none at: "+updatedURL)
                continue
        else:
            continue
        name=extractValue("name", soup)
        school=extractValue("school", soup)
        #print("name: "+name)
        if (hasValidCharacters(name) and hasValidCharacters(school)):
            writeToFile(name, school, updatedURL)
        else:
            print("name"+name+" "+str(i))
            

def extractValue(type, soup):
    if type=="name":
        divTag = soup.find("h3")
        nameExtracted=divTag.extract()    
        name=removeTags(str(nameExtracted))
        return name.strip()
    elif type=="school":
        divTag = soup.find_all("h6")
        if (len(divTag)>1):
            correctSchool=divTag[1]
            nameExtracted=correctSchool.extract()
        else:
            nameExtracted=""

        name=removeTags(str(nameExtracted))
        return name.strip()
    
def removeTags(extractedName):
    name=""
    toDelete=True
    for character in extractedName:
        if character == "<":
            toDelete=True
        elif character == ">":
            toDelete=False
        if toDelete==True:
            pass
        else:
            name+=character
    name=name[1:-1]    
    return name

def writeToFile(name, school, url):
    f = open("dataScraped.txt", "a")
    f.write("name:"+str(name)+"|school:"+str(school)+"|url:"+url+"\n")
    #print("name:"+name+"|school:"+school+"|url:"+url+"\n")
    f.close()
#open and read the file after the appending:
#f = open("demofile2.txt", "r")
#print(f.read())
#removeTags("<asidfj;asdfs>hi<ajosidfjaosiasjd>")

def hasValidCharacters(word):
    isValid=True
    word=word.lower()
    for char in word:
        if (char=='a' or char=='b' or char=='c' or char=='d' or char=='e' or char=='f' or char=='g' or char=='h' or char=='i' or char=='j' or char=='k' or char=='l' or char=='m' or char=='n' or char=='o' or char=='p' or char=='q' or char=='r' or char=='s' or char=='t' or char=='u' or char=='v' or char=='w' or char=='x' or char=='y' or char=='z' or char=='\'' or char=='-' or char==' ' or char=='.' or char=='(' or char==')' or char==',' or char=='*' or char=='1' or char=='2' or char=='3' or char=='4' or char=='5' or char=='6' or char=='7' or char=='8' or char=='9' or char=='0' or char=='_' or char=='-' or char=='/' or char=='&'):
            continue
        else:
            return False
    return True
        

start()