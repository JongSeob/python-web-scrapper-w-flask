import csv

def save_to_file(file_name, jobs):
  with open(file_name, mode="w") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "company", "link"])

    for job in jobs:
      writer.writerow(list(job.values()))