'''Rounding in Python
 Round numerical values up and down in Python
When we round values, we go from a numerical value with decimal places to a whole number. With this process we do lose some precision, but the rounded value is often much easier to read and interpret.

Python has three ways to turn a floating-point value into a whole (integer) number:

The built-in round() function rounds values up and down.
The math.floor() function rounds down to the next full integer.
The math.ceil() function rounds up to the next full integer.

.2f  rounds to 2 decimals
print(format(10.541546, '.2f')) >>> 10.54
//

More on:
    https://kodify.net/python/math/round-integers/
    
'''

score = 10.541546
score_round = round(score, 2)
score_format = format(score, "0.2f")
print(score_format)
score_f_string = f"{score:.2f}"
print(score_f_string)

print(type(score_round), type(score_format), type(score_f_string))



