import requests
from bs4 import BeautifulSoup

# scrap stories with 100+ votes

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
  points_list= list()
  
  
  for index, item in enumerate(links):

    # articles titles text
    title = links[index].getText()
    # articles link
    href = links[index].get("href", "Link is broken")
    # add articles title and link to the hacker news list created above
    hn.append({"title": title, "link": href})

    # articles votes count
    # iterate over each point, clean it and convert it to int 
    for index, item in enumerate(votes):
  
      if item.getText().endswith(" point"):
        item_point = item.getText().replace(" point", "")
        points_list.append(item_point[0])
      else:
        item_points = item.getText().replace(" points", "")
        points_list.append(item_points)

  for index, item in enumerate(points_list):
    points_list[index] = int(item)

   
  return hn


if __name__ == "__main__":
  create_custom_hn(links=links, votes=votes)
