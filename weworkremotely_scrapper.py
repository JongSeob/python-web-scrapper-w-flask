from soup_dipper import get_soup_from_url

def get_weworkremotely_sectios(soup):
  div = soup.find("div", {"class": "jobs-container"})

  if(div == None):
    print (f"[Failed] div is None")

  sections = div.find_all("section", {"class": "jobs"})
  
  return sections

def extract_job_infos_from_section(section, base_url):

  jobs_ul = section.find("ul")

  jobs_li = jobs_ul.find_all("li")

  job_infos = []
  
  for li in jobs_li:
    attr_class = li.get('class')
    
    if(attr_class == ['feature'] or attr_class == []):
      job_info = {}
      anchor = li.find_all("a")[1]

      job_info["title"]   = anchor.find("span", {"class": "title"}).text      
      job_info["company"] = anchor.find("span", {"class": "company"}).text
      job_info["url"]     = base_url + anchor.get("href")

      job_infos.append(job_info)

  return job_infos

def extract_weworkremotely_jobs(url, search_keyword):  
  postfix = "/remote-jobs/search?term=" + search_keyword

  soup = get_soup_from_url(url + postfix)

  sections = get_weworkremotely_sectios(soup)

  job_infos = []
  for section in sections:
    job_infos += (extract_job_infos_from_section(section, url))
          
  return job_infos