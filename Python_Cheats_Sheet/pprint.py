""" 
pprint
The pprint module provides a capability to “pretty-print” arbitrary Python 
data structures in a form which can be used as input to the interpreter.
- pprint display output in a json-like format.
"""

import pprint


student_scores = {
  "Ali": 95,
  "Sarah": 86,
  "Waleed": 91
}

# pprint.pprint(student_scores)

pprint.pprint([10, 55, 77, 88])



