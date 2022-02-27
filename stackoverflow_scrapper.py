from soup_dipper import get_soup_from_url

def get_stackoverflow_pagination(soup, url):
  
  pagination = soup.find("div", {"class": "s-pagination"})

  anchors = pagination.find_all("a")

  anchor_list = []
  for anchor in anchors:
    anchor_list.append(anchor)

  # remove the last one that directs the next page
  anchor_list = anchor_list[:-1]

  pagination = []
  for anchor in anchor_list:
    pagination.append(url + anchor["href"])

  return pagination

def extract_stackoverflow_job_title_company_url(pagination, base_url):

  job_titles = []
  job_companies = []
  job_urls  = []
  
  for page in pagination:
    soup = get_soup_from_url(page)

    job_divs = soup.find("div", {"class": "listResults"}).find_all("div")

    for div in job_divs:
      h2 = div.find("h2")

      if(h2 == None):
        continue

      anchor = h2.find("a")

      title = anchor.get("title")
      href  = base_url + anchor.get("href")

      if(len(job_titles) > 0 and title == job_titles[-1]):
        continue
      
      job_titles.append(title)
      job_urls.append(href)

      h3 = div.find("h3")

      company = h3.find("span").text

      job_companies.append(company)
      
    
  return (job_titles, job_companies, job_urls)

def extract_stackoverflow_jobs(url, search_keyword):
  postfix = "/jobs?r=true&q=" + search_keyword
  
  soup = get_soup_from_url(url + postfix)

  pagination = get_stackoverflow_pagination(soup, url)

  (job_titles, job_companies, job_urls) = extract_stackoverflow_job_title_company_url(pagination, url)

  jobs = []

  for i in range(len(job_titles)):
    jobs.append({"title": job_titles[i], "company": job_companies[i],"url": job_urls[i]})

  return jobs