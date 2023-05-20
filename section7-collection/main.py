from typing import Callable, Any

list_friends = ['foo', 'bar', 'baz']
dictionary_friends = {
    '1': 'foo',
    '2': 'bar',
    '3': 'baz'
}


def run_on_list():
    # POINT-1: Add
    list_friends.append('foe')
    print(list_friends)
    # POINT-2: Delete
    remove_a_friend: Callable[[Any], None] = lambda x: list_friends.remove(x)
    for friend in list_friends:
        if friend.__eq__('foe'):
            remove_a_friend(friend)
    print(list_friends[0:])
    # POINT-3: Edit
    list_friends[list_friends.index('baz')] = 'qux'
    print(list_friends[0:])


def run_on_dictionary():
    # POINT-4: Add
    dictionary_friends.update({'4': 'foe'})
    print(dictionary_friends)
    print(dictionary_friends['4'])
    # POINT-5: Delete
    del dictionary_friends[get_deleted_index()]
    print(dictionary_friends)
    # POINT-6: Edit
    dictionary_friends.update({get_updated_index(): 'qux'})
    print(dictionary_friends)


def get_deleted_index():
    for item in dictionary_friends.items():
        if item[1].__eq__('foe'):
            return item[0]
    return ''


def get_updated_index():
    for item in dictionary_friends.items():
        if item[1].__eq__('baz'):
            return item[0]
    return ''


if __name__ == '__main__':
    run_on_list()
    run_on_dictionary()
