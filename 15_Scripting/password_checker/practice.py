import requests, hashlib, sys


def request_api_data(query):
  """Pwned Password API response function"""
  
  response = requests.get(url="https://api.pwnedpasswords.com/range/"+ query)

  if response.status_code == 200:
    return response.text
  
  
def hash_password(password):
  """hash user password and query the first 5 characters in password API"""
  hashed_password = hashlib.sha1(
    string=password.encode("utf-8")
    ).hexdigest().upper()
  
  api_query = hashed_password[:5]
  tail = hashed_password[5:]

  # pass API response to pass_leak_count for vulnerability check:
  api_response = request_api_data(api_query)

  return pass_leak_count(api_response, tail)


def pass_leak_count(hashes, hashes_to_check):
  """check how many times my password has been hacked"""
  hashes = (line.split(":") for line in hashes.splitlines())
  
  for hashing, count in hashes:
    if hashing == hashes_to_check:
      return count
  
  return 0
  

def main_function():
  user_input= input("Enter a password: ")
  hack_counts = hash_password(user_input)

  if hack_counts:
    return "%s has been breached %s times" % (user_input, hack_counts)
  else:
    return "%s is a strong password. %s breaches!" % (user_input, hack_counts)

  
if __name__ == "__main__":
  print(sys.exit(main_function()))
  
