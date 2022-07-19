from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline    

def scrape(request):
    return redirect("../")

def news_list(request):
    
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    soup = BSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_results = results.find_all("div", class_="card-content")
    job_dict = {
        "title": "",
        "company": "",
        "location": "",
    }

    job_arr = []

    for job_element in job_results:
        job_dict = {}
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        """job_dict["title"] = str(title_element.text)
        job_dict["company"] = str(company_element.text)
        job_dict["location"] = str(location_element.text)
        job_arr.append(job_dict)"""
        title_text = str(title_element.text)
        company_text = str(company_element.text)
        location_text = str(location_element.text)

        #Code for stoing into database
        Headline.objects.create(title=title_text, company=company_text, location=location_text)

    context = {
        "job_arr": job_arr,
    }
    return render(request, "home.html", context)
