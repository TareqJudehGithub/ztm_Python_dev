"""
Web Scraping
 - automated gathering of data from an online source usually from a website. 
 - Retreiving data from the web, cleaning and using it.
 - Why scrape websites?
  - data collection
  - information
  - news updates

 - To found out what we are allowed to scrape, we simply include
   /robots.txt at the end of a website url
   http://www.google.com/robots.txt

  
  Beautiful Soup
   Installation
   $  pip install beautifulsoup4
   
"""

# scrap stories with 100+ votes
import requests
from bs4 import BeautifulSoup

api_response = requests.get(url="https://news.ycombinator.com/newest")

if api_response.status_code == 200:
  soup = BeautifulSoup(api_response.text, "html.parser")

  # article selector
  links = soup.select(".storylink")

  # points(votes) selector
  votes = soup.select(".score")

else:
  print(api_response.status_code)

def create_custom_hn(links, votes):

  # hacker news list
  hn = list()
  
  # return articles titles
  for index, item in enumerate(links):
    
    title = links[index].getText()
    # .get() 2nd param is a default value in case the href link was broken.
    href = links[index].get("href", "Link is broken")
    hn.append({"title": title, "link": href})

    # points type is str, but we need to return only stories with
    # 100+ votes.. so first we need to convert points to int, and 
    # then build our if statement. 

    # but what about the " points" string? how can we sort that issue out?
    # for that we will use replace()
    points = votes[index].getText()
    # if " point" in points:
    #   points = int(votes[index].getText().replace(" point", ""))
    # elif " points" in points:
    #   points = int(votes[index].getText().replace(" points", ""))
    # else:
    #   points = int(votes[index].getText())

    # points = int(votes[index].getText())

    print(points)
    print(type(points))


  """
  - In case we needed to scrape a 2nd page, 3rd, or even more
    
    1. declare a new API response variable with adding string "p=#"
      api_response_p1 = requests.get(url="https://news.ycombinator.com/news?")
      api_response_p2 = requests.get(url="https://news.ycombinator.com/news?p=2")
    
    2. make clone variable of the selector and add them together in ur scraping
    function.
      soup_p1 = BeautifulSoup(ap_response_p1, "html.parser")
      soup_p2 = BeautifulSoup(ap_response_p2, "html.parser")

    # article selector
    links_p1 = soup_p1.select(".storylink")
    link_p2 = soup_p1.select(".storylink")

    # points(votes) selector
    subtext_p1 = soup_p1.select(".subtext")
    subtext_p2 = soup_p2.select(".subtext")

    all_links = links_p1 + link2_p2
    all_subtexts = subtext_p1 + subtext_p2

  
  def scrap_function():


  scrap_function(all_links, all_subtexts)
  """