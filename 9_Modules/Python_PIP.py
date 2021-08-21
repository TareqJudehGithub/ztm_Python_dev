"""
Python Package Index (PIP)

 - PIPs are packages developed by a 3rd-party developers.
 - The true power of Python comes from the community, where we are
   able to find ready packages(for web development, data science, and many other
   features) ready instead of writing that from scratch.
 - PIPs are free to use.
 - We can create our own PIPs.
 - $ python.exe -m pip install --upgrade pip
    - To upgrade pip to the lates version:
 - $ pip list
    - Display all installed packaged in my project.
"""

# Using pyjokes package
# pip install pyjockes
# pip install pyjockes==v.5.0 for installing a certain version

import pyjokes

joke = pyjokes.get_joke('en', 'neutral')
print(joke)