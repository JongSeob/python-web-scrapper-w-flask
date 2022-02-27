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
from stackoverflow_scrapper import extract_stackoverflow_jobs
from weworkremotely_scrapper import extract_weworkremotely_jobs

# from flask import Flask, render_template, request

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

#========================================================================

#========================================================================

stackoverflow_jobs = extract_stackoverflow_jobs(urls["stackoverflow"], "python")
weworkremotely_jobs = extract_weworkremotely_jobs(urls["weworkremotely"], "python")

fake_db["python"] = stackoverflow_jobs
fake_db["python"] += weworkremotely_jobs

# app = Flask("JobScrapper")

# @app.route("/")
# def home():
#   return render_template("home.html")

# @app.route("/report") # potato.html <form>의 action 이름과 동일함.
# def report():
#   job = request.args.get('job')
#   return render_template("home.html", searchingBy=job)

# app.run(host="0.0.0.0")