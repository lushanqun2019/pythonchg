#2、使用__metaclass__

class Singleton2(type):
    def __init__(cls, name, bases, dict):
        super(Singleton2, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)
        return cls._instance


class Create2(metaclass=Singleton2):
    s = 1


a = Create2()
b = Create2()
b.s = 3
print(a is b, a.s)
# 输出
#True 3
