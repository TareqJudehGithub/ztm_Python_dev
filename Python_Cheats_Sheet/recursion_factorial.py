"""
Recursion is the ability of a function to call it self.
"""

# Factorial problem

# 1. Using recursion
def fact(n):
  if n == 1:
    return 1
  else:
    return n * fact(n - 1)

# 2. Using for loop
def fact2(n2):
  factorial = 1

  for i in range(1, n2 + 1):
    factorial *= i

  return "factorial = %s" % factorial


if __name__ == '__main__':
  print("Using recursion")
  n = int(input("Enter a number: "))
  print("The factorial of {} = {}\n".format(n, fact(n)))

  print("Using for loop")
  n2 = int(input("Enter a number: "))
  print(fact2(n2))
  



  