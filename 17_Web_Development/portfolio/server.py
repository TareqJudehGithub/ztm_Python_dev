from flask import Flask, app, render_template, request
from markupsafe import escape
import csv

app = Flask(__name__)

# main page
@app.route("/")
def homepage():
  return render_template(escape("index.html"))

# change webpage dynamically
@app.route("/<string:page_name>")
def html_page(page_name):
  return render_template(page_name)

# contact me
@app.route("/submit_form", methods=["POST", "GET"])
def submit_form(name=None):
  if request.method == "POST":  # check with HTML form method attrib
   
    try:
      # request data submitted and save it as a dict
      data = request.form.to_dict()
      name = data["name"]
    
    except:
      return "Form submission failed!"
    
    else:
      # write_to_txt(data)
      write_to_csv(data)
      return render_template("/thankyou.html", name=name)

  else:
    return "Error submitting form!"
  


# submit data to a txt file
def write_to_txt(data):

  with open("./files/database.txt", mode="w") as database:
    name = data["name"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    return database.write(f"\n{name.title()}, {email}, {subject.capitalize()}, {message.capitalize()}\n")


# submit data to a csv file
def write_to_csv(data):

  with open('./files/db.csv', newline='', mode="a") as file:
    name = data["name"]
    email = data["email"]
    subject = data["subject"]
    message = data["message"]

    print(data)
    
  # csv writer object
    csv_writer = csv.writer(
      file, 
      delimiter=",", 
      quotechar='"',  
      quoting=csv.QUOTE_MINIMAL
      )

    # write sumbitted data to file
    return csv_writer.writerow(
      [name.title(), email, subject.capitalize(), message.capitalize()]
      )


if __name__ == "__main__":
  app.run()


  