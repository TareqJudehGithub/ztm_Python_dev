import requests, pprint
from bs4 import BeautifulSoup


api_response_p1 = requests.get(url="https://news.ycombinator.com/news")

if api_response_p1.status_code == 200:
  soup = BeautifulSoup(api_response_p1.text, "html.parser")
 
  # article selector
  links = soup.select(".storylink")

  # points(votes) selector
  subtext = soup.select(".subtext")

else:
  print(api_response_p1.status_code)


def sort_stories(hn_list):
  """sort stories by points"""
  # sort stories by points in a descending order
  return sorted(hn_list, key=lambda k: k["points"], reverse=True)


def create_custom_hn(links, subtext):
  """Scrap stories from HackerNews function"""

  hacker_news = list()  # hacker news list
  points_list= list()   # stories points list
  
  # iterate over link and extract stories title, link, and points
  for index, item in enumerate(links):

    # each link (article) title text using .GetText()
    title = item.getText()
    # each link (article) using "href" attrib. .get() has a default param
    href = item.get("href", "https://news.ycombinator.com/news")
    # points for each articles: sub-select class "score" from "subtext" selector
    point = subtext[index].select(".score")
  
    if len(point):  # make sure each story has points
    # iterate over each point, clean it and convert it to int 
      points_text = point[0].getText()
      
    if points_text.endswith(" point"):
      point_int =  points_text.replace(" point", "")
      points_list.append(point_int[0])
    else:
      points_int =  points_text.replace(" points", "")
      points_list.append(points_int)
    
  # add each int point(s) to point_list
  for index, item in enumerate(points_list):
    points_list[index] = int(item)
  
  # add title, link, and points to the hacker news(hn) list created above

  for points in points_list:
    # return only stories(news) with 100+ points
    if points >= 100:
      hacker_news.append({
        "title": title,
        "link": href,
        "points": points
      })

  return sort_stories(hacker_news)

  


if __name__ == "__main__":
  # print(create_custom_hn(links=links, subtext=subtext))
  pprint.pprint(create_custom_hn(links=links, subtext=subtext))  
