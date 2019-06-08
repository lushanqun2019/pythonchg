# 1、__new__方法实现

class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            # 第一次调用__instance是空走这个分支，创建一个obj
            obj = super(Singleton,cls)
            # 把obj赋值给类属性__instance
            cls._instance = obj.__new__(cls,*args,**kwargs)
         # 第二次调用类属性__instance有值，走这个分支，直接返回第一次调用的属性值
        return cls._instance

class Create(Singleton):
    s = 1

a = Create()
b = Create()
a.s = 3
print(a is b,b.s)

# 输出
# True 3
