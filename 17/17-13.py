import abc
class Pet(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @abc.abstractmethod
    def eat(self):
        pass

class Cat(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        print('修改'.center(50, '='))
        self.__type = x

    # @type.deleter
    # def type(self):
    #     print('删除'.center(50, '='))
    #     del self.__type

    def eat(self):
        print('%s正在吃猫粮' % self.name)


class Dog(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        print('修改'.center(50, '='))
        self.__type = x

    def eat(self):
        print('%s正在吃狗粮' % self.name)


class Pig(Pet):
    def __init__(self, name, type):
        super().__init__(name)
        self.__type = type

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, x):
        print('修改'.center(50, '='))
        self.__type = x

    def eat(self):
        print('%s正在吃猪粮' % self.name)


class Master:
    def __init__(self,name,pet):
        self.__name = name
        self.__pet = pet

    @property
    def name(self):
        return self.__name

    @property
    def pet(self):
        return self.__pet

    def feed(self):
        pettype = self
        print('''
        %s主人准备好宠物粮食
        %s品种的%s来进食      
        ''' % (self.name,self.pet.type,self.pet.name))
        self.pet.eat()

pet1 = Pig('pipi','minipig')
master1 = Master('Anny',pet1)
master1.feed()

pet2 = Cat('nini','Siamese')
master2 = Master('Bob',pet2)
master2.feed()

pet3 = Dog('lala','Husky')
master3 = Master('Candy',pet3)
master3.feed()
