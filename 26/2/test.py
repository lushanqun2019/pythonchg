from lib import common
from db import db_handler

user_1 = common.User('Albert', '123456', ('127.0.0.1', 8081), ['Bob'], {'1': ['Bob', 'Mary']})
user_2 = common.User('Bob', '123456', ('127.0.0.1', 8082), ['Albert'], {'1': ['Albert', 'Mary']})
user_3 = common.User('Mary', '123456', ('127.0.0.1', 8083), ['Albert'], {'1': ['Albert', 'Bob']})
db_handler.create_user(user_1)
db_handler.create_user(user_2)
db_handler.create_user(user_3)
