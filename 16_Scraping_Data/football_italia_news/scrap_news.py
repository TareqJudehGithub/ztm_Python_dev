from bs4 import BeautifulSoup
import requests, pprint

response_api = requests.get(
  url="https://football-italia.net/milan-minute-by-minute-news/")


if response_api.status_code == 200:
  
  soup = BeautifulSoup(response_api.text, "html.parser")
  
  stories = soup.select(".entry-title")
  anchor = soup.select("a", href=True)
  date_published = soup.select(".published")

  
  def scrap_news(stories, story_date):
    fi_news = list()

    for story in stories:
      title = story.getText()

      anchor_tag = story.select("a", href=True)
      for el in anchor_tag:

        for date in story_date:

          fi_news.append({
            "title": title,
            "title_link": el["href"],
            "date": date.getText()
          })
   
    return fi_news
      
else:
  print("Football Italia News website is offline.")


if __name__ == "__main__":
  pprint.pprint(scrap_news(stories, date_published))
  
