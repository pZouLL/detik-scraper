import requests 
from bs4 import BeautifulSoup
import pandas as pd
import os 
import time

day_li , date_li , time_li , category_li , title_li , link_li = [] , [] , [] , [] , [] , []
days = ["Senin" , "Selasa" , "Rabu" , "Kamis" , "Jumat" , "Sabtu" , "Minggu"]


search = input("What do you want to search today? : ")

url = requests.get(f"https://www.detik.com/search/searchall?query={search}")


soup = BeautifulSoup(url.text , "lxml")

berita_news = soup.find("div" , class_ = "list media_rows list-berita")
eacharticle = berita_news.find_all("article")
for x in eacharticle:
    link = x.find("a")
    link_final = link["href"]
    date_category = x.find("span" , class_ = "date").text

    li1 = date_category.split(",")
    li = [i for i in li1[0]]
    count = 0 
    for index , i in enumerate(li):
        if i.isupper() == True:
            if count == 1:
                day_index = index
                break
            count += 1

    day = ""
    for i in range(day_index,len(li)):
        day += li[i]
    
    category = ""
    for i in range(0 , day_index):
        category += li[i]
    

    title = x.find("h2" , class_ = "title").text

    li2 = date_category.split(",")
    li3 = li2[1].split(" ")
    li3 = li3[1:]

    date = "".join(li3[0:3])
    time1 = "".join(li3[3:5])

    day_li.append(str(day))
    date_li.append(str(date))
    time_li.append(str(time1))
    category_li.append(str(category))
    title_li.append(str(title))
    link_li.append(str(link_final))


df = pd.DataFrame({"Day" : day_li , "Date" : date_li , "Time" : time_li , "Category" : category_li , "Title" : title_li , "Link" : link_li})

df.to_excel("newstoday.xlsx")
print("Scraping....")
time.sleep(1)
print("Scraping Succesfull!")
time.sleep(1)
print("Opening File....")
os.system("newstoday.xlsx")