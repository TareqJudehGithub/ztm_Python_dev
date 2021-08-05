# Create an @authenticated decorator that only allows the function to run if user1
# has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

# def authenticated(fn):
#   # code here
#
#
# @authenticated
# def message_friends(user):
#     print('message has been sent')
#
# message_friends(user1)


def authenticated(func):
    def wrapper(*args):
        if args[0]['valid']:
            return func(args[0]['name'])
        else:
            print('Access denied!')
    return wrapper


@authenticated
def message_friends(user):
    print(f'Hello, {user}!')


message_friends(user1)
