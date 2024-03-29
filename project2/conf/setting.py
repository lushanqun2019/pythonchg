#/conf/setting.py

import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH=os.path.join(BASE_DIR,'db','db.json')
LOG_PATH=os.path.join(BASE_DIR,'log','access.log')
LOGIN_TIMEOUT=3

'''
logging配置
'''
# 定义三种日志输出格式
standard_format='[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'\
                '[%(levelname)s][%(message)s]' # 其中name为getlogger指定的名字
simple_format='[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
id_simple_format='[%(levelname)s][%(asctime)s]%(message)s'

# log配置字典
LOGGING_DIC={
    'version':1,
    'disable_existing_loggers':False,
    'formatters':{
        'standard':{
            'format':standard_format
        },
        'simple':{
            'format':simple_format
        },
    },
    'filters':{},
    'handlers':{
        # 打印到终端的日志
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',    # 打印到屏幕
            'formatter':'simple'
        },
        # 打印到文件的日志,收集info及以上的日志
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler', # 保存到文件
            'formatter':'standard',
            'filename':LOG_PATH,    # 日志文件
            'maxBytes':1024*1024*5, # 日志大小：5M
            'backupCount':5,
            'encoding':'utf-8',     # 日志文件的编码，防止出现中文乱码
        },
    },
    'loggers':{
        # logging.getLogger(__name__)拿到的logger配置
        '':{
             'handlers':['default','console'],  # log数据既写入文件又打印到屏幕
             'level':'DEBUG',
             'propagate':True,  # 向上（更高level的logger）传递
        },
    },
}
       
 
