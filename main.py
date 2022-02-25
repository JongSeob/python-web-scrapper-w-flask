"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import csv
import re
from soup_dipper import get_soup_from_url
from bs4 import BeautifulSoup
import requests

db = {}

urls = {
  "stackoverflow": "https://stackoverflow.com/jobs?r=true&q=python",         
  "weworkremotely": "https://weworkremotely.com/remote-jobs/search?term=python", 
  "remoteok": "https://remoteok.io/remote-dev+python-jobs"
}

def save_jobs(file_name, jobs_info):
    if(".csv" not in file_name):
      file_name += ".csv"

    # substitute unusable character for filename to whitespace
    file_name = re.sub(r'[/\\?%*:|"<>"]', ' ', file_name)
  
    with open (file_name, mode="w") as csv_file:
      csv_writer = csv.writer(csv_file)

      for info in jobs_info:
        csv_writer.writerow(str(info["href"]))



# stack overflow ------------------------------------------------------
def get_stackoverflow_pagination(soup):
  pagination = soup.find("div", {"class": "s-pagination"})

  anchors = pagination.find_all("a")

  anchor_list = []
  for anchor in anchors:
    anchor_list.append(anchor)

  # remove the last one that directs the next page
  anchor_list = anchor_list[:-1]

  pagination = []
  for anchor in anchor_list:
    pagination.append(anchor["href"])

  return pagination

#------------------------------------------------------

def extract_stackoverflow_python_jobs(url):
  soup = get_soup_from_url(url)

  pagination = get_stackoverflow_pagination(soup)

  print (pagination)
  

extract_stackoverflow_python_jobs(urls["stackoverflow"])