friends = ['foo', 'bar', 'baz']


def run():
    print_friends()
    friends.append('qux')
    print(friends[0:])


def print_friends():
    for friend in friends:
        print(friend)


if __name__ == '__main__':
    run()
