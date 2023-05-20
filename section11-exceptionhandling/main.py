friends = ['foo', 'bar', 'baz']

try:
    friends.index('qux')
except ValueError as err:
    print(err)
