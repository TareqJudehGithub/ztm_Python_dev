import smtplib, os

# setup Gmail email account
def sending_emails():

  # Gmail credentials:
  gmail_user = os.environ.get("GMAIL_USER")
  gmail_pass = os.environ.get("GMAIL_PASS")

  msg_content = """
  Hello Tareq,
  I hope all's well.
  I'm testing sending emails using Python.
  I'd really appreciate it if you'de be so kind and try and
  reply to this message. That will help me improve my testing 
  further more.

  Best regards,

  Tareq
  """
  try:
    # setup gmail server
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as mail_server:
      mail_server.ehlo()
      mail_server.starttls()

      mail_server.login(
        user=gmail_user,
        password=gmail_pass
      )
      mail_server.sendmail(
        from_addr="Tareq Coding Python",
        to_addrs=["tareq.joudeh@gmail.com", "tareqmjoudeh@gmail.com"],
        msg=f"Subject: Testing sending email via Python\n\n{msg_content}"
      )
      

  except os.error:
    return os.error
  
  else:
    return "Email sent! Thank you."


if __name__ == "__main__":
  print(sending_emails())