import Teacher


class Student:
    def __init__(self, name: str = '', major: str = None, gpa: float = None, teachers: [Teacher] = None):
        if teachers is None:
            teachers = []
        self.name = name
        self.major = major
        self.gpa = gpa
        self.teachers = teachers

    def __str__(self):
        return f"Student={{name={self.name}, major={self.major}, gpa={self.gpa}, teachers={self.teachers}}}"
