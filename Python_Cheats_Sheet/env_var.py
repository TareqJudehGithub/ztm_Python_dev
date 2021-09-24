"""
Saving sensitive data in Environment Variable
"""

import os

# In terminal, save your sensitive data to a variable using export
# $ export MY_PASSWORD=Pa$$123@

# define a new variable in Python, and save the newly created variable you
# created in terminal
my_pass = os.environ.get("MY_PASSWORD")

# Now you can use my_pass variable safely without others seeing your sensitive
# data like passwords, keys..etc.