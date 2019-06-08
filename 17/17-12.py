class People:
    def __init__(self,name,id,lesson=[],tuition=[]):
        self.name = name
        self.id = id
        self.lesson = lesson
        self.tuition = tuition

    def addlesson(self, lesson, tuition):
        lessonlist = []
        tuitionlist = []
        lessonlist.append(lesson)
        tuitionlist.append(tuition)
        for l in lessonlist:
            for t in tuitionlist:
                print("""
                课程信息
                %s姓名：%s
                课程名称：%s
                课程价格：%s
                """ % (self.id,self.name,l,t))

class Teacher(People):
    pass

class Student(People):
    pass

tea1 = Teacher('Albert','老师')
tea1.addlesson('English',30)

stu1 = Student('Joy','学生')
stu1.addlesson('English',30)
