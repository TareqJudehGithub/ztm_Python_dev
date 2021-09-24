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


"""