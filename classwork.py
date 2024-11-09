import requests
from bs4 import BeautifulSoup
import pandas as pd



url = "https://realpython.github.io/fake-jobs/"
webpage = requests.get(url)

parsed_webpage = BeautifulSoup(webpage.content, "html.parser")


informations = parsed_webpage.find_all("div", class_ = "column is-half")

all_titles = []
all_subtitles = []
all_locations = []
all_dates = []



for information in informations:
    title = information.find("h2", class_ = "title is-5").text
    all_titles.append(title)

    subtitle = information.find("h3").text
    all_subtitles.append(subtitle)

    location = information.find("p", class_ = "location").text
    all_locations.append(location)

    date = information.find("p", class_ = "is-small has-text-grey").text
    all_dates.append(date)

    print(f"JobTitle: {title} ==> Subtitle: {subtitle} ==> Location: {location} ==> date: {date}")

dataset = {"JobTitles": all_titles, "Jobsubtitles": all_titles, "JobLocation": all_locations, "Jobdate": all_dates}

df = pd.DataFrame(dataset)

df.to_csv("JobListing.csv", index=False)
