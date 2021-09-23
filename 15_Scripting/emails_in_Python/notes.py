"""
Send emails in Python

email module
 - The email module in Python was update in Python 3.6
 - Python can send emails to people automatically, like birthdays, memos,..etc.

"""
 
# smtplib  allows us to create a mail server
# smtp (Simple Mail Transfer Protocol)

import smtplib
from email.message import EmailMessage



# Remember to define a new gmail_pass variable and add it to the Env Var.
# $ export gmail_pass=mygmailpass



"""
 email message content
 .set_content(
 html_template(
 substitute(
   {"$var in html file": "my string"},
    "html"
   )
 )  The 2nd param is the parser (parse html).
"""