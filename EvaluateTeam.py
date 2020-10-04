# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EvaluateTeam.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

selected=[]

class Ui_EvaluateTeam(object):
    def setupUi(self, EvaluateTeam):
        EvaluateTeam.setObjectName("EvaluateTeam")
        EvaluateTeam.resize(436, 360)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EvaluateTeam.sizePolicy().hasHeightForWidth())
        EvaluateTeam.setSizePolicy(sizePolicy)
        EvaluateTeam.setMinimumSize(QtCore.QSize(436, 360))
        EvaluateTeam.setMaximumSize(QtCore.QSize(436, 360))
        EvaluateTeam.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(EvaluateTeam)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(EvaluateTeam)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox1 = QtWidgets.QComboBox(EvaluateTeam)
        self.comboBox1.setObjectName("comboBox1")
        self.horizontalLayout.addWidget(self.comboBox1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox2 = QtWidgets.QComboBox(EvaluateTeam)
        self.comboBox2.setObjectName("comboBox2")
        self.horizontalLayout.addWidget(self.comboBox2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label1 = QtWidgets.QLabel(EvaluateTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label1.setObjectName("label1")
        self.horizontalLayout_4.addWidget(self.label1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.label2 = QtWidgets.QLabel(EvaluateTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.horizontalLayout_4.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(EvaluateTeam)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.horizontalLayout_4.addWidget(self.label3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget1 = QtWidgets.QListWidget(EvaluateTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget1.setFont(font)
        self.listWidget1.setObjectName("listWidget1")
        self.horizontalLayout_2.addWidget(self.listWidget1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.listWidget2 = QtWidgets.QListWidget(EvaluateTeam)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget2.setFont(font)
        self.listWidget2.setObjectName("listWidget2")
        self.horizontalLayout_2.addWidget(self.listWidget2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.pushButton = QtWidgets.QPushButton(EvaluateTeam)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(EvaluateTeam)
        QtCore.QMetaObject.connectSlotsByName(EvaluateTeam)

        self.combobox()

        self.comboBox1.currentTextChanged.connect(self.Qlist1)

        self.pushButton.clicked.connect(self.Qlist2)

    def retranslateUi(self, EvaluateTeam):
        _translate = QtCore.QCoreApplication.translate
        EvaluateTeam.setWindowTitle(_translate("EvaluateTeam", "EvaluateTeam"))
        self.label.setText(_translate("EvaluateTeam", "Evalute The Performance Of Your Fantasy Team"))
        self.label1.setText(_translate("EvaluateTeam", "Players"))
        self.label2.setText(_translate("EvaluateTeam", "Points"))
        self.pushButton.setText(_translate("EvaluateTeam", "Calculate Score"))


    def combobox(self):
        self.comboBox1.addItem('Select Team')
        self.comboBox2.addItem('Select Match')        
        teams=[]
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        sql='SELECT Name from teams;'
        xc.execute(sql)
        while True:
            record=xc.fetchone()
            if record==None:
                break
            if record[0] not in teams:
                teams.append(str(record[0]))
        teams.sort()
        self.comboBox1.addItems(teams)

        self.comboBox2.addItem('match')

        self.Qlist1()
    def Qlist1(self):
        self.listWidget1.clear()
        self.listWidget2.clear()
        self.label3.setText('')
        if self.comboBox1.currentText()=='Select Team':
            return
        global selected
        selected=[]
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        sql1="SELECT Players from teams WHERE Name='"+self.comboBox1.currentText()+"' "
        xc.execute(sql1)
        while True:
            record=xc.fetchone()
            if record==None:
                break
            selected.append(str(record[0]))
        for a in selected:
            self.listWidget1.addItem(a)
        print(selected)
        
    def Qlist2(self):
        self.listWidget2.clear()
        if self.comboBox2.currentText()=='Select Match':
            return
        global selected
        pointslist=[]
        total=0
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        #sql="SELECT * from '"+self.comboBox2.currentText()+"' WHERE Player='"+a+"';"
        for a in selected:
            xc.execute("SELECT * from '"+self.comboBox2.currentText()+"' WHERE Player='"+a+"';")
            while True:
                
                record=xc.fetchone()
                #print(record)
                if record==None:
                    break
                scored=record[1]
                faced=record[2]
                fours=record[3]
                sixes=record[4]
                bowled=record[5]
                maiden=record[6]
                given=record[7]
                wkts=record[8]
                catches=record[9]
                stumping=record[10]
                ro=record[11]
                #points calculation
                points=scored/2
                if scored>=50:
                    points+=5
                if scored>=100:
                    points+=10
                if scored>0:
                    sr=(scored/faced)*100
                    if sr>=80 and sr<100:
                        points+=2
                    if sr>=100:
                        points+=4
                points+=fours
                points+=sixes*2

                points+=wkts*10
                if wkts>=3:
                    points+=5
                if wkts>=5:
                    points+=10
                if bowled>0:
                    er=given/(bowled/6)
                    if er<=2:
                        ponys+=10
                    if er>2 and er<=3.5:
                        points+=7
                    if er>3.5 and er<=4.5:
                        points+=4
                points+=catches*10
                points+=stumping*10
                points+=ro*10
                points=int(points)
                points=str(points)
                pointslist.append(points)

        for a in pointslist:
            self.listWidget2.addItem(a)
            total+=int(a)
        print(pointslist)
        self.label3.setText(str(total))
        
                
                    
                     
                

        
        
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateTeam = QtWidgets.QDialog()
    ui = Ui_EvaluateTeam()
    ui.setupUi(EvaluateTeam)
    EvaluateTeam.show()
    sys.exit(app.exec_())
