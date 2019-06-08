#4、使用模块
#其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
class Singleton(object):
    def foo(self):
        pass
singleton = Singleton()
#将上面的代码保存在文件 mysingleton.py 中，使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象

from a import singleton
