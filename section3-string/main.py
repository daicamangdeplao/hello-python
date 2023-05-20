message = 'Hello, World'
messages = ['Hello', 'World']


def run():
    # POINT-1: Check the length
    print(f"[{message}] has the length of {message.__len__()}")
    # POINT-2: Manipulate element in a string
    print(f"The lower case of [{message}] is [{message.lower()}]")
    # POINT-3: Compare two strings
    print(message.__eq__('Hello, World'))
    # POINT-4: Access a character in a string
    print(f"The first two characters in [{message}] is [{message[0:2]}]")
    # POINT-5: Concatenate two strings
    print(str.join(' ', messages).replace(' ', ', '))


if __name__ == '__main__':
    run()
