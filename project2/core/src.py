#/core/src.py

from conf import settings
from lib import common
import time

logger=common.get_logger(__name__)

current_user={'user':None,'login_time':None,'timeout':int(settings.LOGIN_TIMEOUT)}

def auth(func):
    def wrapper(*args,**kwargs):
        if current_user['user']:
            interval=time.time()-current_user['login_time']
            if interval<current_user['timeout']:
                return func(*args,**kwargs)
        name=input('name>>:')
        db=common.conn_db()
        if db.get(name):    # 已注册用户的登录流程
            if db.get(name).get('locked'):
                logger.warning('该用户已被锁定')
                print('该用户已被锁定')
            else:
                logging_error_times=0
                while True:
                    if logging_error_times>=3:
                        logger.warning('密码输入错误3次，该用户已被锁定')
                        db[name]['locked']=1
                        common.save_db(db)
                        break
                    password=input('password>>:')
                    if password==db.get(name).get('password'):
                        logger.info('登录成功')
                        print('登录成功')
                        current_user['user']=name
                        current_user['login_time']=time.time()
                        return func(*args,**kwargs)
                    else:
                        logger.warning('密码错误')
                        logging_error_times+=1
            
        else:           # 注册
            is_register=input('是否注册？ (Y/N) ')
            if is_register in ['Y','y']:
                password=input('password>>')
                db[name]={'password':password,'money':0,'locked':0}
                logger.info('登录成功')
                print('登录成功')
                current_user['user']=name
                current_user['login_time']=time.time()
                common.save_db(db)
                return func(*args,**kwargs)
            else:
                logger.info('用户不注册')
    return wrapper

@auth
def buy():
    db=common.conn_db()
    money=db.get(current_user['user']).get('money')
    print('目前账户有%d元' %money)
    items_dict={'item1':1,'item2':2}
    print(items_dict.keys())
    items_bought_dic={}
    while True:
        item_buy=input('buy which(Q退出)?>>').strip()
        item_buy_split=item_buy.split(' ')
        # print(item_buy_split[0],item_buy_split[1])
        if item_buy_split[0] in ['q','Q']:
            db[current_user['user']]['money']=money
            common.save_db(db)
            print('你买了:',items_bought_dic)
            print('你买了:',money)
            break
        elif item_buy_split[0] in items_dict:
            item,item_num=item_buy_split[0],item_buy_split[1]
            item_price=items_dict[item]*int(item_num)
            print(item,':'item_num,'共花了%d'%item_price)
            if item_price<=money:
                money-=item_price
                print('购买成功，还有%d元'%money)
                if item in items_bought_dic:
                    items_bought_dic[item]+=item_num
                else:
                    items_bought_dic[item]=item_num
            else:
                print('余额不足')
        else:
            print('请输入【商品名称】【商品数量】')

@auth
def withdraw():
    db=common.conn_db()
    money=db.get(current_user['user']).get('money')
    print('账户余额%d元' %money)
    withdraw_num=int(input('取多少钱?'))
    if withdraw_num<=money:
        money-=withdraw_num
        db[current_user['user']]['money']=money
        common.save_db(db)
        print('取现成功，账户余额%d元:',%money)
    else:
        print('账户余额不足')
    
@auth
def repay():
    db=common.conn_db()
    money=db.get(current_user['user']).get('money')
    print('账户余额%d元' %money)
    repay_num=int(input('还款数量?'))
    money+=repay_num
    db[current_user['user']]['money']=money
    common.save_db(db)
    print('还款成功，目前账户余额%d元:',%money)

@auth
def run():
    print('''
1.取现
2.还款
3.消费
Q.退出
    ''')
    while True:
        choice=input('>>:').strip()
        if not choice:continue
        elif choice=='1':
            withdraw()
        elif choice=='2':
            repay()
        elif choice=='3':
            buy()
        elif choice in ['Q','q']:
            quit()
    
