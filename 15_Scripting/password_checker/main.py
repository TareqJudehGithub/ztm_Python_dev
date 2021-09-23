import requests, hashlib, sys


def request_api_data(query_char):
  """1. Check password vulnerability using API"""
  url = "http://api.pwnedpasswords.com/range/" + query_char
  
  res = requests.get(url=url)
  
  if res.status_code != 200:  
    raise RuntimeError(f"Error Fetching: {res.status_code}, check the api and try again.")

  else:
    return res


def get_password_leaks_count(hashes, hash_to_check):
  """3. check how many times my password has been hacked"""

  # separate first number of hacks from hashed
  hashes = (line.split(":") for line in hashes.text.splitlines())
  
  # count total hacks if found
  for h, count in hashes:

    # check if tail(hash) is equal to hash_to_check (how many times password
    # has been leaked):
    if h == hash_to_check:
      
      return count
    
  return 0



def pwn_api_check(password):
  """2. Hash plain password and check vulnerability"""
  # check password if it exists in API response

  # hash plain password
  sha1_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
  
  # split the first five characters from the rest in hashed password
  first_5, tail = sha1_password[:5], sha1_password[5:]
  
  # check first_5 in password API checker:
  response = request_api_data(first_5)
  
  return get_password_leaks_count(response, tail)
  

def main(args):
  """Check user password input here."""
  for password in args:
    # get leaked counts 
    count = pwn_api_check(password)

    if count:
      print(f"{password} was found {count} time.\n{password} is weak.", end="\n\n")


    else:
      print(f"{password} is strong! {count} hacks found.")

  return "Password check completed."

if __name__ == "__main__":
  # print(request_api_data("123"))
  # print(pwn_api_check("pass123"))
  print(sys.exit(main(sys.argv[1:])))

