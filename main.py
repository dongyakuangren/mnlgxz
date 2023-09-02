
from lib.share import SI
import requests
from PySide2.QtWidgets import QApplication,QMessageBox
from PySide2.QtUiTools import QUiLoader

class win_login:
    def __init__(self):
        self.ui = QUiLoader().load('load.ui')
        self.ui.loadbtn.clicked.connect(self.onlogin)
        self.ui.zcbtn.clicked.connect(self.enroll)

    #登录功能
    def onlogin(self):
        self.username = self.ui.usernameedt.text()
        self.password = self.ui.passwordedt.text()
        self.url = 'http://127.0.0.1:8520/api/load'
        self.logintext = requests.get(url=self.url, params={
            'username' : self.username,     #'superadmin',
            'password' : self.password #'e0f2664fdd43e28087081f6ab6e05fad'
        })
        self.loninsin = self.logintext.json()['data']
        print(self.logintext.json()['data'])
        if str(self.loninsin) == '[]':
            print('登录失败！')
        else:
            print('登录成功！')


    #注册功能
    def enroll(self):
        print('aa')
        SI.mainwin= Enroll()
        SI.mainwin.ui.show()



class Enroll:
    def __init__(self):
        self.ui = QUiLoader().load('enroll.ui')





if __name__ == '__main__':
    app = QApplication([])
    SI.loadwin = win_login()
    SI.loadwin.ui.show()
    app.exec_()