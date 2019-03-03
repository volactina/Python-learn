'''
用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
新用户可以用与现有系统帐号不冲突的用户名创建帐号，
已存在的老用户则可以用用户名和密码登陆重返系统。
建议基本框架为：

'''

userinfo={}

def newusers():
    username=input('create your user name:')
    if username in userinfo:
        print('name has been used, try another!')
    else:
        password=input('type your password:')
        userinfo.update({username:password})
        print("Congratulations %s! Your account has been created!"%(username))


def oldusers():
    username=input('type your username:')
    password=input('type your password:')
    if username in userinfo and password == userinfo[username]:
        print(username, 'welcome back ')
    else:
        print('login incorrect')

def login():
    while(True):
        option = input('''
                         (N)ew User Login 
                         (O)ld User Login
                         (E)xit
                         Please choose an option:
                                ''')
        if option=='N':
            newusers()
        elif option=='O':
            oldusers()
        elif option=='E':
            print('bye')
            return

if __name__ == '__main__':
    login()