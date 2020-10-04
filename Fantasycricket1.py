# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fantasycricket1.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QMessageBox

bats=[]
bowls=[]
wktkeepers=[]
allrndrs=[]

bats1=[]
bowls1=[]
wktkeepers1=[]
allrndrs1=[]

selected=[]

count1=1
count2=1
count3=1
count4=1

txt=''

class Ui_MainWindow(object):

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(713, 527)
    
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label15 = QtWidgets.QLabel(self.centralwidget)
        self.label15.setObjectName("label15")
        self.verticalLayout.addWidget(self.label15)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.horizontalLayout.addWidget(self.label3)
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("label4")
        self.horizontalLayout.addWidget(self.label4)
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label5.setFont(font)
        self.label5.setObjectName("label5")
        self.horizontalLayout.addWidget(self.label5)
        self.label6 = QtWidgets.QLabel(self.centralwidget)
        self.label6.setObjectName("label6")
        self.horizontalLayout.addWidget(self.label6)
        self.label7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label7.setFont(font)
        self.label7.setObjectName("label7")
        self.horizontalLayout.addWidget(self.label7)
        self.label8 = QtWidgets.QLabel(self.centralwidget)
        self.label8.setObjectName("label8")
        self.horizontalLayout.addWidget(self.label8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label9.setFont(font)
        self.label9.setObjectName("label9")
        self.horizontalLayout_2.addWidget(self.label9)
        self.label10 = QtWidgets.QLabel(self.centralwidget)
        self.label10.setObjectName("label10")
        self.horizontalLayout_2.addWidget(self.label10)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label11.setFont(font)
        self.label11.setObjectName("label11")
        self.horizontalLayout_2.addWidget(self.label11)
        self.label12 = QtWidgets.QLabel(self.centralwidget)
        self.label12.setObjectName("label12")
        self.horizontalLayout_2.addWidget(self.label12)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.BAT = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BAT.setFont(font)
        self.BAT.setObjectName("BAT")
        self.horizontalLayout_4.addWidget(self.BAT)
        self.BOW = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.BOW.setFont(font)
        self.BOW.setObjectName("BOW")
        self.horizontalLayout_4.addWidget(self.BOW)
        self.AR = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.AR.setFont(font)
        self.AR.setObjectName("AR")
        self.horizontalLayout_4.addWidget(self.AR)
        self.WK = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.WK.setFont(font)
        self.WK.setObjectName("WK")
        self.horizontalLayout_4.addWidget(self.WK)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label13 = QtWidgets.QLabel(self.centralwidget)
        self.label13.setObjectName("label13")
        self.horizontalLayout_4.addWidget(self.label13)
        self.label14 = QtWidgets.QLabel(self.centralwidget)
        self.label14.setText("")
        self.label14.setObjectName("label14")
        self.horizontalLayout_4.addWidget(self.label14)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.listWidget1 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget1.setObjectName("listWidget1")
        self.horizontalLayout_3.addWidget(self.listWidget1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.listWidget2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget2.setObjectName("listWidget2")
        self.horizontalLayout_3.addWidget(self.listWidget2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 21))
        self.menubar.setObjectName("menubar")
        self.menuManageTeams = QtWidgets.QMenu(self.menubar)
        self.menuManageTeams.setObjectName("menuManageTeams")
        MainWindow.setMenuBar(self.menubar)
        self.menuManageTeams.triggered[QtWidgets.QAction].connect(self.menu)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")

        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")

        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")

        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")

        self.menuManageTeams.addAction(self.actionNEW_Team)
        self.menuManageTeams.addAction(self.actionOPEN_Team)
        self.menuManageTeams.addAction(self.actionSAVE_Team)
        self.menuManageTeams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManageTeams.menuAction())


        self.BAT.toggled.connect(self.rbtns)
        self.BOW.toggled.connect(self.rbtns)
        self.AR.toggled.connect(self.rbtns)
        self.WK.toggled.connect(self.rbtns)
        

        self.listWidget1.itemDoubleClicked.connect(self.removelist1)
        self.listWidget2.itemDoubleClicked.connect(self.removelist2)

        self.bat=0
        self.bowl=0
        self.wkt=0
        self.ar=0
        self.pointsavl=1000
        self.pointsused=0
        
        



        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Your Selections</span></p></body></html>"))
        self.label1.setText(_translate("MainWindow", "Batsmen(BAT)"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#55aa7f;\">##</span></p></body></html>"))
        self.label3.setText(_translate("MainWindow", "Bowlers(BOW)"))
        self.label4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#55aa7f;\">##</span></p></body></html>"))
        self.label5.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#55aa7f;\">##</span></p></body></html>"))
        self.label7.setText(_translate("MainWindow", "Wicket-keeper(WK)"))
        self.label8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; color:#55aa7f;\">##</span></p></body></html>"))
        self.label9.setText(_translate("MainWindow", "<html><head/><body><p>Points Available</p></body></html>"))
        self.label10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600; color:#55aa7f;\">####</span></p></body></html>"))
        self.label11.setText(_translate("MainWindow", "<html><head/><body><p>Points Used</p></body></html>"))
        self.label12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#55aa7f;\">####</span></p></body></html>"))
        self.BAT.setText(_translate("MainWindow", "BAT"))
        self.BOW.setText(_translate("MainWindow", "BOW"))
        self.AR.setText(_translate("MainWindow", "AR"))
        self.WK.setText(_translate("MainWindow", "WK"))
        self.label13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Team Name</span></p></body></html>"))
        self.menuManageTeams.setTitle(_translate("MainWindow", "ManageTeams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


    def menu(self,action):
        global txt
        txt=(action.text())

        if txt=='NEW Team':
            global count1,count2,count3,count4
            count1=1
            count2=1
            count3=1
            count4=1

            self.listWidget2.clear()
            self.bat=0
            self.bowl=0
            self.wkt=0
            self.ar=0
            self.pointsavl=1000
            self.pointsused=0
        
            
            text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")

            if text=='' and ok:
                msg=QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Name cannot be empty! Please your Team Name")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()


            elif ok:
                self.label14.setText(str(text))
                self.initialize()
                global bats1,bowls1,allrndrs1,wktkeepers1,bats,bowls,allrndrs,wktkeepers

                bats=[]
                bowls=[]
                wktkeepers=[]
                allrndrs=[]

                bats1=[]
                bowls1=[]
                wktkeepers1=[]
                allrndrs1=[]

            

            
            
            
        if txt=='SAVE Team':
            #p=self.label14.text()
            #q=#'"+self.label14.text()+"','"+selected[counter]+"','"+self.points(selected[counter])+"';"   
            self.saveteam()




        if txt=='OPEN Team':
            
            self.openteam()

        if txt=='EVALUATE Team':
            from EvaluateTeam import Ui_EvaluateTeam
            EvaluateTeam = QtWidgets.QDialog()
            ui = Ui_EvaluateTeam()
            ui.setupUi(EvaluateTeam)
            EvaluateTeam.show()
            EvaluateTeam.exec_()
            
    
    def initialize(self):
        self.label2.setText(str(self.bat))
        self.label4.setText(str(self.bowl))
        self.label6.setText(str(self.ar))
        self.label8.setText(str(self.wkt))
        self.label10.setText(str(self.pointsavl))
        self.label12.setText(str(self.pointsused))


    def rbtns(self):
        global txt
        
        if self.BAT.isChecked()==True:
            category='BAT'
            
        elif self.BOW.isChecked()==True:
            category='BWL'
            
        elif self.AR.isChecked()==True:
            category='AR'
            
        elif self.WK.isChecked()==True:
            category='WK'
            
        if txt=='NEW Team':
            print('IN new')
            self.filllists(category)
            self.fillQlist(category)

        if txt=='OPEN Team':
            self.fillQlist(category)

        if txt=='SAVE Team':
            self.fillQlist(category)
                
    def filllists(self,category):
        
        self.listWidget1.clear()
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        sql="SELECT Player from stats WHERE Ctg='"+category+"';"
        xc.execute(sql)
        global count1,count2,count3,count4
        if category=='BAT':
            while count1<2:
                while True:
                    record=xc.fetchone()
                    if record==None:
                        break
                    #print(record[0 self.listWidget1.addItem(record[0])
                    global bats
                    bats.append(record[0])
            #self.fillQlist(category)
            #print(bats)
                count1+=1
            print(bats)
        if category=='BWL':
            while count2<2:
                while True:
                    record=xc.fetchone()
                    if record==None:
                        break
                    #print(record[0])
                    #self.listWidget1.addItem(record[0])
                    global bowls
                    bowls.append(record[0])
                #self.fillQlist(category)
                count2+=1
            print(bowls)
        if category=='AR':
            while count3<2:
                while True:
                    record=xc.fetchone()
                    if record==None:
                        break
                    #print(record[0])
                    #self.listWidget1.addItem(record[0])
                    global allrndrs
                    allrndrs.append(record[0])
                #self.fillQlist(category)
                count3+=1
            print(allrndrs)      
        if category=='WK':
            while count4<2:
                while True:
                    record=xc.fetchone()
                    if record==None:
                        break
                    #print(record[0])
                    #self.listWidget1.addItem(record[0])
                    global wktkeepers
                    wktkeepers.append(record[0])
                count4+=1
        #self.fillQlist(category)
            print(wktkeepers)



                
    def fillQlist(self,category):
        self.listWidget1.clear()
        
        if category=='BAT':
            global bats
            for a in bats:
                self.listWidget1.addItem(a)
                #print(bats)

        if category=='BWL':
            global bowls
            for a in bowls:
                self.listWidget1.addItem(a)

        if category=='AR':
            global allrndrs
            for a in allrndrs:
                self.listWidget1.addItem(a)

        if category=='WK':
            global wktkeepers
            for a in wktkeepers:
                self.listWidget1.addItem(a)
                
    def fillQlist2(self):
        self.listWidget2.clear()
        
        global selected
        for a in selected:
            self.listWidget2.addItem(a)
        #self.points(a)
        self.bat=len(bats1)
        self.bowl=len(bowls1)
        self.wkt=len(wktkeepers1)
        self.ar=len(allrndrs1)
        self.initialize()
        
    def removelist1(self,item):
        try:
            global bats1,bowls1,allrndrs1,wktkeepers1

            if len(bats1)+len(bowls1)+len(allrndrs1)+len(wktkeepers1)>10:
                msg1='Not more than 11 players'
                raise exception
            
            
            y=self.points(item.text())
            
            self.pointsused=self.pointsused+int(y)
            self.pointsavl=self.pointsavl-int(y)

            
            if self.pointsused>1000 and self.pointsavl<0:
                msg1='Insufficient Points'
                self.pointsused=self.pointsused-int(y)
                self.pointsavl=self.pointsavl+int(y)
    
                raise execption
        

    
            
            
            if self.BAT.isChecked()==True:
                if len(bats1)>4:
                    msg1='Batsmen cannot be more than 5'
                    self.pointsused=self.pointsused-int(y)
                    self.pointsavl=self.pointsavl+int(y)
                    raise execption
            
                #global bats,bats1
                z=self.listWidget1.takeItem(self.listWidget1.row(item))
                #print(item.text())
                bats.remove(item.text())
                bats1.append(item.text())
                #self.listWidget2.addItem(item.text())
            if self.BOW.isChecked()==True:
                if len(bowls1)>4:
                    msg1='Bowlers cannot be more than 5'
                    self.pointsused=self.pointsused-int(y)
                    self.pointsavl=self.pointsavl+int(y)
                    raise exception
            
                
                #global bowls,bowls1
                z=self.listWidget1.takeItem(self.listWidget1.row(item))
                #print(item.text())
                bowls.remove(item.text())
                bowls1.append(item.text())
                #self.listWidget2.addItem(item.text())
            if self.AR.isChecked()==True:
                if len(allrndrs1)>2:
                    msg1='Allrounders cannot be more than 3'
                    self.pointsused=self.pointsused-int(y)
                    self.pointsavl=self.pointsavl+int(y)
                    raise exception

                #global allrndrs,allrndrs1
                z=self.listWidget1.takeItem(self.listWidget1.row(item))
                #print(item.text())
                allrndrs.remove(item.text())
                allrndrs1.append(item.text())
                #self.listWidget2.addItem(item.text())
            if self.WK.isChecked()==True:
                if len(wktkeepers1)>0:
                    msg1='Wicketkeeper cannot be more than 1'
                    self.pointsused=self.pointsused-int(y)
                    self.pointsavl=self.pointsavl+int(y)
                    raise exception
            
                #global wktkeepers,wktkeepers1
                z=self.listWidget1.takeItem(self.listWidget1.row(item))
                #print(item.text())
                wktkeepers.remove(item.text())
                wktkeepers1.append(item.text())
                #self.listWidget2.addItem(item.text())
            #print(bats)
            #print(bats1)


            
                
                    
            #self.initialize()
            self.selected()

        except:
            
            msg=QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText(msg1)
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

            
        
    def removelist2(self,item):
        global bats1,bowls1,allrndrs1,wktkeepers1,bats,bowls,allrndrs,wktkeepers

        
        #self.listWidget2.takeItem(self.listWidget2.row(item))
        if self.BAT.isChecked()==True:
            category='BAT'
        if self.BOW.isChecked()==True:
            category='BWL'
        if self.AR.isChecked()==True:
            category='AR'
        if self.WK.isChecked()==True:
            category='WK'
        
            #global bats,bats1
        self.listWidget2.takeItem(self.listWidget2.row(item))
        if item.text() in bats1:
            #print(item.text())
            bats1.remove(item.text())
            bats.append(item.text())
            #self.listWidget1.addItem(item.text())
        if item.text() in bowls1:
            #global bowls,bowls1
            #self.listWidget2.takeItem(self.listWidget2.row(item))
            #print(item.text())
            bowls1.remove(item.text())
            bowls.append(item.text())
            #self.listWidget1.addItem(item.text())
        if item.text() in allrndrs1:
            #global allrndrs,allrndrs1
            #self.listWidget2.takeItem(self.listWidget2.row(item))
            #print(item.text())
            allrndrs1.remove(item.text())
            allrndrs.append(item.text())
            #self.listWidget1.addItem1(item.text())
        if item.text() in wktkeepers1:
            #global wktkeepers,wktkeepers1
            #self.listWidget2.takeItem(self.listWidget2.row(item))
            #print(item.text())
            wktkeepers1.remove(item.text())
            wktkeepers.append(item.text())
            #self.listWidget1.addItem(item.text())
        
        #self.listWidget1.addItem(item.text())
        if self.BAT.isChecked()==False and self.BOW.isChecked()==False and self.AR.isChecked()==False and self.WK.isChecked()==False:
            category=None
            
        y=self.points(item.text())
        self.pointsused=self.pointsused-int(y)
        self.pointsavl=self.pointsavl+int(y)
        self.selected()
        self.fillQlist(category)

        
    def selected(self):
        global bats1,bowls1,allrndrs1,wktkeepers1,selected
        selected=[]
        selected=bats1+bowls1+allrndrs1+wktkeepers1
        print(selected)
        self.fillQlist2()


    def points(self,a):
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        sql="SELECT Value from stats WHERE Player='"+a+"';"
        xc.execute(sql)
        record=xc.fetchone()
        print(record[0])
        return record[0]


    def saveteam(self):
        global selected
        import sqlite3
        x=sqlite3.connect("game_database.db")
        xc=x.cursor()
        sql="SELECT Name from teams WHERE Name='"+self.label14.text()+"';"
        xc.execute(sql)
        record1=xc.fetchone()
        if record1==None:            

             
            if len(selected)<11:
                #self.dialog()
                return

            if len(selected)==11:
                
                counter=0
                
                while counter<len(selected):
                    
                    xc.execute("INSERT INTO teams (Name,Players,Value) VALUES ('"+self.label14.text()+"','"+selected[counter]+"','"+str(self.points(selected[counter]))+"');")
                    x.commit()                                            
                    counter+=1
                                                                                             


        
                        
        if record1!=None:
                       
            xc.execute("DELETE FROM teams WHERE Name='"+self.label14.text()+"'")
            x.commit()
            self.saveteam()
                
            
             
    
    def openteam(self):
        global bats1,bowls1,allrndrs1,wktkeepers1,bats,bowls,allrndrs,wktkeepers
        global count1,count2,count3,count4
        count1=1
        count2=1
        count3=1
        count4=1

        bats=[]
        bowls=[]
        wktkeepers=[]
        allrndrs=[]

        
        bats1=[]
        bowls1=[]
        wktkeepers1=[]
        allrndrs1=[]

        #selected=[]




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
        #print(teams)

        team,ok=QInputDialog.getItem(MainWindow,"OPEN Team","Choose A Team",teams,0,False)
        if ok :
            self.label14.setText(str(team))

            selected1=[]
            sql1="SELECT Players from teams WHERE Name='"+team+"' "
            xc.execute(sql1)
            while True:
                record=xc.fetchone()
                if record==None:
                    break
                selected1.append(str(record[0]))
                #QtCore.QCoreApplication.processEvents()
            #print(selected1)




            
            
            xc.execute("SELECT Player from stats WHERE Ctg='BAT'")
            while True:
                count=0
                
                record=xc.fetchone()
                if record==None:
                    break
                while count<11:
                    if selected1[count]==record[0]:
                        bats1.append(str(record[0]))
                        break
                    count+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()
            #print(bats1)


            xc.execute("SELECT Player from stats WHERE Ctg='BWL'")
            while True:
                count=0
                
                record=xc.fetchone()
                if record==None:
                    break
                while count<11:
                    if selected1[count]==record[0]:
                        bowls1.append(str(record[0]))
                        break
                    count+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()
            #print(bowls1)


            
            xc.execute("SELECT Player from stats WHERE Ctg='AR'")
            while True:
                count=0
                
                record=xc.fetchone()
                if record==None:
                    break
                while count<11:
                    if selected1[count]==record[0]:
                        allrndrs1.append(str(record[0]))
                        break
                    count+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()
            #print(allrndrs1)



            
            xc.execute("SELECT Player from stats WHERE Ctg='WK'")
            while True:
                count=0
                
                record=xc.fetchone()
                if record==None:
                    break
                while count<11:
                    if selected1[count]==record[0]:
                        wktkeepers1.append(str(record[0]))
                        break
                    count+=1
                    QtCore.QCoreApplication.processEvents()
                QtCore.QCoreApplication.processEvents()
            #print(wktkeepers1)



            self.filllists('BAT')
            self.filllists('BWL')
            self.filllists('AR')
            self.filllists('WK')


            for a in bats1:
                if a in bats:
                    bats.remove(a)
            for a in bowls1:
                if a in bowls:
                    bowls.remove(a)
            for a in allrndrs1:
                if a in allrndrs:
                    allrndrs.remove(a)
            for a in wktkeepers1:
                if a in wktkeepers:
                    wktkeepers.remove(a)

            print(bats)
            print(bowls)
            print(wktkeepers)
            print(allrndrs)
            
            self.pointsused=0
            self.selected()
            for a in selected1:
                x=self.points(a)
                self.pointsused+=x
            self.pointsavl=1000-self.pointsused
            self.initialize()


    def open_rbtns(self):
        print('IN open')
        
        if self.BAT.isChecked()==True:
            category='BAT'
            
        elif self.BOW.isChecked()==True:
            category='BWL'
            
        elif self.AR.isChecked()==True:
            category='AR'
            
        elif self.WK.isChecked()==True:
            category='WK'

        
        self.fillQlist(category)
        




        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
