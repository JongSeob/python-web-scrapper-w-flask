from soup_dipper import get_soup_from_url

def get_remoteok_pagination(soup, url):
  table = soup.find("table", {"id": "jobsboard"})#.find("tbody")

  print (table)

def extract_remoteok_jobs(url, search_keyword):
  # postfix = "/remote-dev+" + search_keyword + "-jobs"
  postfix = ""

  soup = get_soup_from_url(url + postfix)

  print(url + postfix)

  print (soup)