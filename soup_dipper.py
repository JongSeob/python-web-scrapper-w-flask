from bs4 import BeautifulSoup
import requests

def get_soup_from_url(url):
  try:
    resp = requests.get(url)
    if(resp.status_code == 200):
      # print(f"Access to {url} url is successful")
      pass
  except:
    print(f"Failed to access to {url}")
  
  soup = BeautifulSoup(resp.text, "html.parser")

  return soup