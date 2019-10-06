'''
代码设计的UI
'''

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class UIMainWindow(QWidget):
    def __init__(self):
        super(UIMainWindow,self).__init__()
        self.setWindowTitle('抢票软件')
        self.resize(1200,600)
        self.setMaximumHeight(700)
        self.setMaximumWidth(1200)
        self.setMinimumWidth(1200)
        self.initUI()
        self.center()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        startLaber = QLabel('出发',self)
        startLaber.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(startLaber,0,0,1,1)
        self.startCombobox = QComboBox()
        layout.addWidget(self.startCombobox,0,1,1,2)
        pointLaber = QLabel('<->')
        pointLaber.setAlignment(Qt.AlignCenter)
        #layout.addWidget(pointLaber, 1, 4, 1, 1)
        endLaber = QLabel('目的', self)
        endLaber.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(endLaber, 0, 3, 1, 1)
        self.endCombobox = QComboBox()
        layout.addWidget(self.endCombobox, 0, 4, 1, 2)
        dateLaber = QLabel('日期', self)
        dateLaber.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(dateLaber, 0, 6, 1, 1)
        self.dateselect = QDateEdit(QDate.currentDate())
        self.dateselect.setMinimumDate(QDate.currentDate())
        self.dateselect.setCalendarPopup(True)
        layout.addWidget(self.dateselect, 0, 7, 1, 2)

        self.loginBtn = QPushButton('登陆',self)
        layout.addWidget(self.loginBtn,0,9,1,1)

        self.querybtn = QPushButton('查询')
        #self.querybtn.setGeometry()
        layout.addWidget(self.querybtn,0,10,2,5)

        carLaber = QLabel('车型', self)
        layout.addWidget(carLaber, 1, 0, 1, 1)
        self.allcheckbox = QCheckBox('全部')
        layout.addWidget(self.allcheckbox,1,1,1,1)
        self.allcheckbox.stateChanged.connect(self.allcar)

        self.Gcheckbox = QCheckBox('G/C-高铁/城际')
        layout.addWidget(self.Gcheckbox, 1, 2, 1, 1)
        self.Dcheckbox = QCheckBox('D-动车')
        layout.addWidget(self.Dcheckbox, 1, 3, 1, 1)
        self.Zcheckbox = QCheckBox('Z-直达')
        layout.addWidget(self.Zcheckbox, 1, 4, 1, 1)
        self.Tcheckbox = QCheckBox('T-特快')
        layout.addWidget(self.Tcheckbox, 1, 5, 1, 1)
        self.Kcheckbox = QCheckBox('K-快速')
        layout.addWidget(self.Kcheckbox, 1, 6, 1, 1)
        self.Lcheckbox = QCheckBox('L-临客')
        layout.addWidget(self.Lcheckbox, 1, 7, 1, 1)
        self.Pcheckbox = QCheckBox('普快')
        layout.addWidget(self.Pcheckbox, 1, 8, 1, 1)


        self.tableshow = QTableWidget()
        self.tableshow.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableshow.setColumnCount(13)
        self.tableshow.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableshow.setHorizontalHeaderLabels(['车次','出发地\n目的地','出发时间\n到达时间','历时','商务座\n特等座','一等座','二等座','软卧',\
                                                  '硬卧','软座','硬座','无座','操作'])
        layout.addWidget(self.tableshow,2,0,6,40)

        passengerLaber = QLabel('*选择乘客', self)
        layout.addWidget(passengerLaber, 8, 0, 1, 2)
        seatLaber = QLabel('*选择席别', self)
        layout.addWidget(seatLaber, 8, 2, 1, 2)
        trainLaber = QLabel('*选择车次', self)
        layout.addWidget(trainLaber, 8, 4, 1, 2)
        timeLaber = QLabel('*选择时间', self)
        layout.addWidget(timeLaber, 8, 6, 1, 2)
        noticeLaber = QLabel('*通知设置', self)
        layout.addWidget(noticeLaber, 8, 9, 1, 4)
        orderLaber = QLabel('*下单设置', self)
        layout.addWidget(orderLaber, 8, 17, 1, 4)
        grabeLaber = QLabel('*抢票设置', self)
        layout.addWidget(grabeLaber, 8, 23, 1, 4)

        self.passengerlist = QListWidget(self)
        layout.addWidget(self.passengerlist, 9, 0, 2, 2)
        self.seatlist = QListWidget(self)
        layout.addWidget(self.seatlist, 9, 2, 2, 2)
        self.trainlist = QListWidget(self)
        layout.addWidget(self.trainlist, 9, 4, 2, 2)
        self.timelist = QListWidget(self)
        layout.addWidget(self.timelist, 9, 6, 2, 2)
        #设置提醒参数
        self.noticeWidget = QWidget()
        noticelayout = QFormLayout()
        maillabel = QLabel('接收邮箱')
        self.mail = QLineEdit()
        notimailabel = QLabel('发送邮箱')
        self.notimail = QLineEdit()
        userlab = QLabel('用户名')
        self.mailuser = QLineEdit()
        passwdlab = QLabel('密码')
        self.mailpass = QLineEdit()
        hostlab = QLabel('邮件服务器')
        self.mailhost = QLineEdit()
        noticelayout.addRow(maillabel,self.mail)
        noticelayout.addRow(notimailabel, self.notimail)
        noticelayout.addRow(userlab, self.mailuser)
        noticelayout.addRow(passwdlab, self.mailpass)
        noticelayout.addRow(hostlab, self.mailhost)
        self.noticeWidget.setLayout(noticelayout)
        layout.addWidget(self.noticeWidget,9,8,2,8)
        #设置下单模式
        self.orderWidget = QWidget()
        orderlayout = QVBoxLayout()
        self.orderWidget.setLayout(orderlayout)

        self.cdnbtn = QCheckBox('开启cdn')
        orderlayout.addWidget(self.cdnbtn,1,Qt.AlignCenter | Qt.AlignTop)

        self.placetypeWidget = QWidget()
        placelayout = QHBoxLayout()
        self.placetype1 = QRadioButton('网页下单')
        self.placetype2 = QRadioButton('按钮下单')
        placelayout.addWidget(self.placetype1)
        placelayout.addWidget(self.placetype2)
        self.placetypeWidget.setLayout(placelayout)
        orderlayout.addWidget(self.placetypeWidget,1,Qt.AlignCenter | Qt.AlignTop)

        self.selltimeLaber = QLabel('预售时间')
        self.selltimeLaber.setAlignment(Qt.AlignCenter)
        self.selltimeLaber.setHidden(True)
        orderlayout.addWidget(self.selltimeLaber)
        self.selltime = QDateTimeEdit(QDateTime.currentDateTime())
        self.selltime.setCalendarPopup(True)
        self.selltime.setHidden(True)
        self.selltime.setDisplayFormat('yyyy-MM-dd HH:mm:ss')
        orderlayout.addWidget(self.selltime)

        self.ordertypeWidget = QWidget()
        typelayout = QHBoxLayout()
        self.ordertype1 = QRadioButton('预售')
        self.ordertype1.toggled.connect(self.showselltime)
        self.ordertype2 = QRadioButton('捡漏')
        self.ordertype2.setChecked(True)
        typelayout.addWidget(self.ordertype1)
        typelayout.addWidget(self.ordertype2)
        self.ordertypeWidget.setLayout(typelayout)
        orderlayout.addWidget(self.ordertypeWidget,1,Qt.AlignCenter | Qt.AlignTop)

        layout.addWidget(self.orderWidget, 9, 16, 2, 4)



    def allcar(self):
        if self.allcheckbox.isChecked():
            self.Gcheckbox.setChecked(True)
            self.Dcheckbox.setChecked(True)
            self.Zcheckbox.setChecked(True)
            self.Tcheckbox.setChecked(True)
            self.Kcheckbox.setChecked(True)
            self.Lcheckbox.setChecked(True)
            self.Pcheckbox.setChecked(True)
        else:
            self.Gcheckbox.setChecked(False)
            self.Dcheckbox.setChecked(False)
            self.Zcheckbox.setChecked(False)
            self.Tcheckbox.setChecked(False)
            self.Kcheckbox.setChecked(False)
            self.Lcheckbox.setChecked(False)
            self.Pcheckbox.setChecked(False)

    def showselltime(self):
        if self.ordertype1.isChecked():
            self.selltimeLaber.setHidden(False)
            self.selltime.setHidden(False)
        else:
            self.selltimeLaber.setHidden(True)
            self.selltime.setHidden(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = UIMainWindow()
    main.show()
    sys.exit(app.exec_())