def run():
    user_input = input('Enter something: ')
    print(user_input)
    if user_input.isdigit():
        print('User has input a numeric')
    else:
        print('User has input a string')


if __name__ == '__main__':
    run()
