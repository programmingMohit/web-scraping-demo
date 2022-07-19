from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline    

def scrape(request):

    URL = "https://astronomy.com/news"
    page = requests.get(URL)
    soup = BSoup(page.content, "html.parser")
    results = soup.find("div", class_="latestNews")
    news_items = results.find_all("div", class_="dataItem")


    for news_element in news_items:
        title_element = news_element.find("div", class_="content").find("h2").find("a")
        image_element = news_element.find("div", class_="thumbnail").find("a").find("img")['src']
        snippet_element = news_element.find("div", class_="content").find("div", class_="snippet")
        title_text = str(title_element.text)
        image_text = str(image_element)
        snippet_text = str(snippet_element.text)

        #Code for stoing into database
        Headline.objects.create(title=title_text, image=image_text, snippet=snippet_text)
    return redirect("../")

def news_list(request):
    return render(request, "home.html")
