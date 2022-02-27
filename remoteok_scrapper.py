from soup_dipper import get_soup_from_url

def extract_remoteok_jobs(url, search_keyword):
  postfix = f"/remote-dev+{search_keyword}-jobs"

  soup = get_soup_from_url(url + postfix)

  job_infos = []
  try:
    job_table = soup.find("table", {"id":"jobsboard"})

    if not job_table:
      raise Exception()

    trs = job_table.find_all("tr", {"class": "job"})

    for tr in trs:
      job_info = {}
      job_info["title"]   = tr.find("h2", {"itemprop":"title"}).text.replace("\n", "")
      job_info["company"] = tr.find("h3", {"itemprop":"name"}).text.replace("\n", "")
      job_info["url"]     = url + tr.find("a", {"itemprop":"url"}).get("href")

      job_infos.append(job_info)
  except:
    print("failed extract remoteok jobs")
    return None

  return job_infos