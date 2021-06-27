"""
operator precedence
    operator precedence order:
    1. ()       brackets
    2.  **      power of
    3.  * and / multiplication and division
    4.  + and - addition and subtraction

"""
print(2 ** 4 - (3 * 4))     # >>> 16 - 8



# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)
print('Exercise Operator Precedence: Guess the output', end='\n')
print((5 + 4) * 10 / 2)
# >>> 45

print(((5 + 4) * 10) / 2)
# >>>  45

print((5 + 4) * (10 / 2))
# >>>  45

print(5 + (4 * 10) / 2)
# >>> 25

print(5 + 4 * 10 // 2)
# >>> 25