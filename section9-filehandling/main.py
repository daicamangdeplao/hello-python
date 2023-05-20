friends = ['foo', 'bar', 'baz']


def read_file():
    employee_file = open('../resource/friends.txt', 'r')
    print(employee_file.readable())
    for employee in employee_file.readlines():
        print(employee)
    employee_file.close()


def write_file():
    employee_file = open('../resource/friends.txt', 'a')
    employee_file.writelines('qux\n')
    employee_file.close()


def restore():
    employee_file = open('../resource/friends.txt', 'w')
    for friend in friends:
        employee_file.write(friend + '\n')
    employee_file.close()


print('Before')
read_file()
write_file()
print('\nAfter')
read_file()
restore()
