class Interger:
    @classmethod
    def input(cls):
        error_tag=0
        input_num=input('请输入一个整数:')
        if not input_num.isdigit():
            error_tag=1
            print('Invalid literal for init() with base 10:%s'%input_num)
            raise ValueError('Invalid literal for init() with base 10:%s'%input_num)
        if int(input_num)<-2147483648 or int(input_num)>2147483647:
            error_tag=1
            print('Error Msg: :%s -越界'%input_num)
            raise SlopOverError('Error Msg: :%s -越界'%input_num)
        return int(input_num) if error_tag==0 else cls.input()

class SlopOverError(BaseException):
    def __init__(self,number,message):
        self.number=number
        self.message=message

    def __str__(self):
        return '<'+self.message+str(self,number)+'>'

Interger.input()
