"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import csv
import os
import re
from bs4 import BeautifulSoup
import requests

from soup_dipper import get_soup_from_url
from stackoverflow_scrapper import *

os.system("clear")

fake_db = {}

urls = {
  "stackoverflow": "https://stackoverflow.com",         
  "weworkremotely": "https://weworkremotely.com", 
  "remoteok": "https://remoteok.com"
}
"/jobs?q=python&r=true&so_source=JobSearch&so_medium=Internal&pg=1"

def save_jobs(file_name, jobs_info):
    if(".csv" not in file_name):
      file_name += ".csv"

    # substitute unusable character for filename to whitespace
    file_name = re.sub(r'[/\\?%*:|"<>"]', ' ', file_name)
  
    with open (file_name, mode="w") as csv_file:
      csv_writer = csv.writer(csv_file)

      for info in jobs_info:
        csv_writer.writerow(info)


def get_weworkremotely_section_urls(soup, base_url):
  div = soup.find("div", {"class": "jobs-container"})

  if(div == None):
    print (f"[Failed] div is None")

  sections = div.find_all("section")

  section_urls = []
  for section in sections:
    li = section.find("li", {"class": "view-all"})

    if(li == None):
      continue

    section_urls.append(base_url + li.find("a").get("href"))
  
  return section_urls

def extract_weworkremotely_jobs(url, search_keyword):  
  postfix = "/remote-jobs/search?term=" + search_keyword

  soup = get_soup_from_url(url + postfix)

  section_urls = get_weworkremotely_section_urls(soup, url)

  for section_url in section_urls:
    soup = get_soup_from_url(section_url)

    jobs_ul = soup.find("section", {"class": "jobs"}).find("ul")

    jobs_li = jobs_ul.find_all("li")
    
    for li in jobs_li:
      li_class = li.get('class')

      if(li_class == ['feature'] or li_class == []):
        pass
#========================================================================

# extract_weworkremotely_jobs(urls["weworkremotely"], "python")

stackoverflow_jobs = extract_stackoverflow_jobs(urls["stackoverflow"], "python")

for job in stackoverflow_jobs:
  print(f"title: {job['title']}, company: {job['company']}")

# fake_db["python"] = stackoverflow_jobs