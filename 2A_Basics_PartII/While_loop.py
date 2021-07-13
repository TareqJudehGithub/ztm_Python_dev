"""
while loop
- while causes the the code to remain running while a condition is true.
- break keyword breaks the loop ignoring lines below it.
- continue keyword restarts/repeats the loop ignoring lines below 'continue'.
- pass keyword  passes the interpreter to the next code.
- while loop vs for loop
    - Use for iterating over objects, we use for loop.
    - while a condition is still true, use while loop.
"""
counter = 10
while counter > 0:
    print('keep looping!')
    counter -= 1

else:
    print('\nDone looping. Thank you <3')

print('')
while True:
    question = input('continue loop? ')
    if question.lower() == 'y':
        continue
    else:
        print('Good buy!')
        break
