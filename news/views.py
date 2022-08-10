from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline    

def scrape(request):

    URL = ["https://astronomy.com/news", "https://skyandtelescope.org/astronomy-news/", "https://www.space.com/science-astronomy"]
    pages = []
    soups = []

    # Stores the request objects in the pages array for each URL
    for url_items in URL:
        pages.append(requests.get(url_items))

    #Stores the BSoup object for each URL in the soups array
    for page in pages:
        soups.append(BSoup(page.content, "html.parser"))
    
    # Scraper Function calls for specific websites
    
    #sky_and_telescope(soups[1])
    space_com(soups[2])
    astronomy_com(soups[0])

    return redirect("news")

def news_list(request):
    headlines = Headline.objects.all()[::-1]
    context = {
        'object_list': headlines,
    }
    return render(request, "news.html", context)

# Scraper Functions

def astronomy_com(soup):
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

def sky_and_telescope(soup):
    results = soup.find("div", class_="listing-items")
    news_items = results.find_all("div", class_="media-block")


    for news_element in news_items:
        title_element = news_element.find("div", class_="media-block__content").find("h2").find("a")
        image_element = news_element.find("a", class_="media-block__figure").find("img")['src']
        snippet_element = news_element.find("div", class_="media-block__content").find("p", class_="brief")
        title_text = str(title_element.text)
        image_text = str(image_element)
        snippet_text = str(snippet_element.text)

        #Code for stoing into database
        Headline.objects.create(title=title_text, image=image_text, snippet=snippet_text)

def space_com(soup):
    results = soup.find("div", class_="listingResults")
    news_items = results.find_all("div", class_="listingResult")


    for news_element in news_items:

        if(not news_element.find("div", class_="sponsored-post")):
            title_element = news_element.find("a", class_="article-link").find("article").find("div", class_="content").find("header").find("h3", class_="article-name")
            image_element = news_element.find("a", class_="article-link").find("article").find("figure").find("div", class_="image-remove-flow-width-setter").find("div", class_="landscape").find("picture").find("img")['src']
            snippet_element = news_element.find("a", class_="article-link").find("article").find("div", class_="content").find("p", class_="synopsis")
            title_text = str(title_element.text)
            image_text = str(image_element)
            snippet_text = str(snippet_element.text)

            #Code for stoing into database
            Headline.objects.create(title=title_text, image=image_text, snippet=snippet_text)
