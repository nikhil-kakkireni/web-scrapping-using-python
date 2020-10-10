import requests
from bs4 import BeautifulSoup
#extracting data from a real estate website
r = requests.get("http://pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")# loading the page
c = r.content
print(c)
soup=BeautifulSoup(c,"html.parser")#setting the data in html way
print(soup.prettify())
#when we inspect the page, we see html tags, we go through inside html tags and we iterate through those html tags and
#then we find the sub tags(basically divisions,classes) for the data and we want to get the data from those tags
all = soup.findall("div",{"class":"propertyRow"})#returns set of items
#text method makes the item in the list as a simple text(a string datatype)
#replace method replaces the character in a string with other character(string functions)


#printing the extracted data
for item in all:
    print(item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ",""))#extracting the price
    print(item.find_all("span",{"class":"propAddressCollapse"})[0].text)#address line 1
    print(item.find_all("span",{"class":"propAddressCollapse"})[1].text)#address line 2
    try:
        print(item.find("span",{"class":"infoBed"}).find("b").text)#no of beds in the house, find(b) implies finding b tag
    except:
        print("None")
    try:
        print(item.find("span", {"class": "infoValueFullBath"}).find(
            "b").text)  # no of full baths in the house, find(b) implies finding b tag
    except:
        print("None")
    try:
        print(item.find("span", {"class": "infoValueHalfBath"}).find(
            "b").text)  # no of bathrooms in the house, find(b) implies finding b tag
    except:
        print("None")
    for column_group in item.find_all("div",{"class":"columnGroup"}):#some more sub columns in item
        print(column_group)

    print(" ")
l = []#creating a list for future use
#saving the extracted data in a csv file
#create a dictionary with key,value pairs
for item in all:
    d = {}
    d["Price"] = item.find("h4",{"class":"propPrice"}).text.replace("\n","").replace(" ","")
    d["Address"] = item.find_all("span",{"class":"propAddressCollapse"})[0].text
    d["Locality"] = item.find_all("span",{"class":"propAddressCollapse"})[1].text
    try:
        d["Beds"] = item.find("span",{"class":"infoBed"}).find("b").text
    except:
        d["Beds"] = "None"
    try:
        d["Bathrooms count"] = item.find("span", {"class": "infoValueFullBath"}).find(
            "b").text
    except:
        d["Bathrooms count"] = "None"
    try:
        d["Half Bath"] = item.find("span", {"class": "infoValueHalfBath"}).find(
            "b").text
    except:
        d["Half Bath"] = "None"
    for column_group in item.find_all("div",{"class":"columnGroup"}):#some more sub columns in item
        d["Column Group"] = column_group
    l.append(d)#appending all those dictionary to a list
#now we create a dataframe for storing those
import pandas
df = pandas.dataframe(l)
print(df) #boom data extracted!!!!!!!!!

#saving data frmae as a csv file
df.to_csv("output.csv")