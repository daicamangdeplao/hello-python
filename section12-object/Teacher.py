import Student


class Teacher:
    def __init__(self, name: str = '', students: [Student] = None):
        if students is None:
            students = []
        self.name = name
        self.students = students

    def __str__(self):
        return f'Teacher={{name={self.name}, students={self.students}}}'
