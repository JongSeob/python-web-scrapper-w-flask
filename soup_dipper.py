from bs4 import BeautifulSoup
import requests

# headers is added for access to remoteok.com
# refer to "https://data-platypus.tistory.com/47?category=957112"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

def get_soup_from_url(url):
  try:
    resp = requests.get(url, headers=headers)
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