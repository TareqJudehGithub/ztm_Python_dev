"""
modules used

- sys

- requests
    $ pip install requests

- hashlib
    built in Python module

    import hashlib
    sha1_password = hashlib.sha1(string=password.encode("utf-8")).hexdigest().upper()

- Pwned PasswordsAPI 
    url = https://api.pwnedpasswords.com/range/{first 5 hash chars}
    - When a password hash with the same first 5 characters is found in the 
      Pwned Passwords repository, the API will respond with an HTTP 200.
    - more info on https://haveibeenpwned.com/API/v2


1. built Pwned Passwords API response function.
2. built a function to hash user plain password input.
3. extracted the first 5 digits from the hashed password, and used them
   as a query for Pwned Passwords API func.
3. built a function that compare the API response with hashed password for
   vulnerabilities.
4. built a main func, where users get to input their password for checking.
   If vulnerabilities were found, the program return a message for the user
   with the total number of breaches found on his/her password entered.
"""

