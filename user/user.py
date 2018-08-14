print('正在创建模块类')
import time
time.sleep(2)

with open (user.py,'a+',encoding ='utf-8)as f:
    code = '''
    class user(object)
        def __init__(self,name,age):
            self.name = name
            self.age = age
    '''
    f.write(code) 
