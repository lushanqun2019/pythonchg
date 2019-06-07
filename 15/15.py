'''
1.根据姓名查看学生所有成绩
2.查看所有人的某学科成绩
3.查看总平均分
4.查看某人的某学科成绩
5.根据姓名删除学生信息
'''
class student:
    school='deepshare'
    def __init__(self,name,grade,maths,chinese):
        self.name=name
        self.grade=grade
        self.maths=maths
        self.chinese=chinese

    def get_name(self):
        return self.name
    
    def get_grade(self):
        return self.grade
    
    def get_maths(self):
        return self.maths
    
    def get_chinese(self):
        return self.chinese
    
    def print_all_score(self):
        print('%s的数学成绩：%3d,语文成绩：%3d'%(self.name,
                                      self.maths,self.chinese))
    def print_one_score(self,subject):
        if subject=='maths':
            print('%s的数学成绩：%3d'%(self.name,self.maths))
        elif subject=='chinese':
            print('%s的语文成绩：%3d'%(self.name,self.chinese))

    def delete(self):
        print("删除%s的成绩".center(50,'=')%(self.name))
        if self.chinese:
            del self.chinese
        if self.maths:
            del self.maths

stu1=student('张三',1,100,90)
stu2=student('李四',2,90,100)
stu={stu1,stu2}
#print(type(stu))
#print(stu1)

#查看所有成绩
for astu in stu:
    astu.print_all_score()
print('='*40)

# 查看所有人的某学科成绩
for astu in stu:
    astu.print_one_score('maths')
print('='*40)

for astu in stu:
    astu.print_one_score('chinese')
print('='*40)

# 计算总平均分
total=0
num=0
for astu in stu:
    total+=(astu.get_maths()+astu.get_chinese())
    num+=2
print('总平均分',total/num)
print('='*40)

#4.查看某人的某学科成绩
name='张三'
subj='maths'
for astu in stu:
    if name == astu.get_name():
        astu.print_one_score(subj)
    
#5.根据姓名删除学生信息
stu1.delete()

name='张三'
subj='maths'
for astu in stu:
    if name == astu.get_name():
        astu.print_one_score(subj)
