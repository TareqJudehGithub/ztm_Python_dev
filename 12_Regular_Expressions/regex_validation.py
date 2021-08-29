import re

"""
Email Validation

 - From https://emailregex.com/, scroll down and copy/paste the Python link.
   r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
"""

r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
"""
- ^[a-zA-Z0-9_.+-]
- +  + plus is an identifier, meaning we can have as many char as we want.
    - At the start, it can be a char, a numeric value, an underscore _, ., + or -
- @
    - Must include @ after the first set.
- [a-zA-Z0-9-]
    - Another set of char and numeric values.
- \.
    - Match the character dot (.)
- [a-zA-Z0-9-.]
    - The final set, mix of char and numeric values.
  
- $
    - End of the line.
    
- password validator
    r'^([a-zA-Z0-9@#$%]{8,12}\d$)'
        - ^([a-zA-Z0-9@#$%] => set: start with any char, digit, or @#$%
        - {8,12} min 8 char long, but max 12 char long.  no spacing after ,
        - \d ends with a digit.
        - $ don't forget this one to include it at the end.
"""


# Email address validator using REGEX
def email_validator(email):
    validator = re.compile(r'(^[a-z0-9_.-]+@[a-z]+\.[a-z]+$)')

    if validator.fullmatch(email):
        return True

    else:
        return 'Invalid email address!'


check_email = email_validator(email='tareq.joudeh@gmail.com')
print(check_email)

print('\n')

print('Password checker')
# Password checker
# 8 char long at least, 12 max, can contain any sort of letters, numbers, and $%@#
# challenge: has to end with a digit


# ^([a-zA-Z0-9@#$%]{8,12}$)
def pass_validator():

    try:
        # validator for password:
        validator = re.compile(r'^([a-zA-Z0-9@#$%]{8,12}\d$)')

    except AttributeError as err:
        return err
        # check if user password is valid, comparing it to the validator above:

    except KeyboardInterrupt:
        return 'User aborted.'

    else:
        while True:
            password = input('Enter a password: ')

            if validator.fullmatch(password):
                return True
            else:
                print('Invalid password!')
                continue


if __name__ == '__main__':
    print(pass_validator())
