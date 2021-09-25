import requests
from bs4 import BeautifulSoup

# web scrapping Hacker News website

response = requests.get(url="https://news.ycombinator.com/newest")

if response.status_code == 200:

  # create a soup object
  soup = BeautifulSoup(response.text, "html.parser") 

  print("title")
  # return webpage title 
  title = soup.title
  print(title, end="\n\n")
  # >>> <title>New Links | Hacker News</title>

  # list all contents in a clean html format
  # print(soup.body.contents, end="\n\n")

  print("find_all()")
  # return all objects with <li> element
  # div_element = soup.find_all("div")
  # print(div_element, end="\n\n")

  
  print("find()")
  # return first object only 
  a_element = soup.find("a")
  print(a_element, end="\n\n")

  print("get votes for article")
  # return image
  votes = soup.find(id="score_28645190")
  print(votes)

  print("") 
  # soup.select()   
  # CSS selector allows us to select elements inside.
  
  # select all storylink class
  print("link") 
  # get me the website url for the first story (article)
  link = soup.select(".storylink")[0].get("href")
  print(link)

  print("") 
  print("score") 
  # get me total points for the 2nd story
  votes = soup.select(".score")[1]
  print(votes, end="\n\n")

  # get points(votes) numbers (text not html tag) for the first article
  print('points')
  points_1 = soup.select(".score")[0].getText()
  print(points_1)
  print(type(points_1))

  # get id of the 2nd article 
  points_art2 = soup.select(".score")[1].get("id")
  print(points_art2)

  # return the tag name
  points_art3 = soup.select(".score")[2].name
  print(points_art3)

  # return tag attributes
  points_art4 = soup.select(".score")[3].attrs
  print(points_art4)

  # return html text as a list item
  points_art5 = soup.select(".score")[2].contents
  print(points_art5)
  print(type(points_art5))
  
  print("")
  all_points = soup.select(".score")
  points_list = list()
  # iterate over all votes
  for index, point in enumerate(all_points):
    str_points = all_points[index].getText()
   
    if " point" in str_points:
      point = all_points[index].getText().replace(" point", "")
      points_list.append(point[0])

    else:
      points = all_points[index].getText().replace(" points", "")
      points_list.append(points)
  print(points_list)
  for index, point in enumerate(points_list):
      points_list[index] = int(point)
  #   point[index] = int(point)
  
  print(points_list)


    # int_points = int(all_points[index].getText().replace(" point", ""))
    # print(f"index: {index}\npoint(s): {int_points}")
    



  

