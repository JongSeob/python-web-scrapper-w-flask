from bs4 import BeautifulSoup
import requests

def get_soup_from_url(url):
  try:
    resp = requests.get(url)
    if(resp.status_code == 200):
      # print(f"Access to {url} url is successful")
      pass
    else:
      raise Exception
  except:
    print(f"Failed to access to {url}. status_code is {resp.status_code}")
    return None
  
  soup = BeautifulSoup(resp.text, "html.parser")

  return soup