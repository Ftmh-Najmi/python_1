cr = [
    {
        'title':'Python',
        'time':'80h'
    },
    {
        'title':'HTML',
        'title':'6h'
    },
    {
        'title':'PHP',
        'time':'none'
    }
]


class User:  #person
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname= lastname

    def fullname(self):
        print(f'my fullname is {self.fname} {self.lname}')


class Student(User):   #child
    def __init__(self, firstname, lastname, email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []

    def printcourses(self):
        if self.courses:
            for course in self.courses:
                print(course['title'])
        else:
            print('This user has no course')

    def fullname(self):
        print('Im an student')
        return super().fullname()
    

class Teacher(User):
    def __init__(self, firstname, lastname, code):
        super().__init__(firstname, lastname)
        self.code = code 

    

s1 = Student('fatemeh','najmi','ftmhnjmi@gmail.com')
s1.fullname()
        