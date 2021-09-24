"""
ord() function
 inbuilt function return an integer representing the Unicode code
"""
# Enter key
print(ord("\r"), end="\n\n")


def check_unicode():
 
  user_input = input("Enter a char: ")
  return f"char {user_input} unicode value is {ord(user_input)}"
  

def check_char():
  user_input = int(input("Enter a value: "))
  return f"{user_input} value is {chr(user_input)}"

if __name__ == "__main__":
  print(check_unicode())
  print(" ")
  print(check_char())
  

