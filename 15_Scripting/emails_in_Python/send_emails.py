import smtplib, os
from email.message import EmailMessage
from string import Template
from pathlib import Path
from email.mime.image import MIMEImage


# create a new email object
email = EmailMessage()

# read index.html files as text
html = Path("./html/index.html").read_text()

# turn html text into a template obj
html_template = Template(html)


# gmail password
gmail_pass = os.environ.get("GMAIL_PASS")

email["from"] = "Tareq Coding"
email["to"] = ["tareq.joudeh@gmail.com", "tareqmjoudeh@gmail.com"]
email["subject"] = "Join the fight today!"

# message content setup
email.set_content(
  html_template.substitute(
    {"name": "Peter", "year": 2021}
    ),"html"
  )


# setup a mail server
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:

  # open a secure connection
  smtp.ehlo()
  smtp.starttls()

  # gmail login credentials
  smtp.login(user="tj.coder1975@gmail.com", password=gmail_pass)
  
  # message
  smtp.send_message(email)
  print("All's good!")
 







