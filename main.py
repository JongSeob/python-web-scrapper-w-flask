"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
import os
from stackoverflow_scrapper import extract_stackoverflow_jobs
from weworkremotely_scrapper import extract_weworkremotely_jobs
from remoteok_scrapper import extract_remoteok_jobs

from exporter import save_to_file
from flask import Flask, render_template, request, redirect, send_file

os.system("clear")

fake_db = {}

urls = {
  "stackoverflow": "https://stackoverflow.com",         
  "weworkremotely": "https://weworkremotely.com", 
  "remoteok": "https://remoteok.com"
}

#========================================================================

# stackoverflow_jobs = extract_stackoverflow_jobs(urls["stackoverflow"], "python")
# weworkremotely_jobs = extract_weworkremotely_jobs(urls["weworkremotely"], "python")
# remoteok_jobs = extract_remoteok_jobs(urls["remoteok"], "python")

# fake_db["python"] = stackoverflow_jobs
# fake_db["python"] += weworkremotely_jobs
# fake_db["python"] += remoteok_jobs

# Flask Part ============================================================
app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/report") # potato.html <form>의 action 이름과 동일함.
def report():
  word = request.args.get('word')

  jobs = []

  try:  
    word = word.lower()
    
    if not word:
      raise Exception()
      
    fromDB = fake_db.get(word)
    
    if (fromDB):
      jobs = fromDB
    else:
      jobs  = extract_stackoverflow_jobs(urls["stackoverflow"], word)
      jobs += extract_weworkremotely_jobs(urls["weworkremotely"], word)
      jobs += extract_remoteok_jobs(urls["remoteok"], word)
      fake_db[word] = jobs
  except:
    return redirect("/")
    
  return render_template("report.html", 
    resultsNumber=len(jobs),
    searchingBy=word,
    jobs=jobs # jobs is the array of dicts
  )

@app.route("/export")
def export():
  try:
    word = request.args.get('word')
    if not word:
      raise Exception()
    word = word.lower()

    jobs = fake_db.get(word)
    if not jobs:
      raise Exception()

    save_to_file("jobs.csv", jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")

app.run(host="0.0.0.0")
#=========================================================================