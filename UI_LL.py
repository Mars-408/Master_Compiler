import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Main.sizePolicy().hasHeightForWidth())
        Main.setSizePolicy(sizePolicy)
        Main.setMinimumSize(QtCore.QSize(1200, 800))
        Main.setMaximumSize(QtCore.QSize(1200, 800))
        Main.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(70, 40, 91, 31))
        self.openfile.setObjectName("openfile")
        self.openfile.clicked.connect(self.openFile)



        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setGeometry(QtCore.QRect(200, 40, 91, 31))
        self.ok.setObjectName("ok")
        self.ok.clicked.connect(self.inputGrammar)


        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(330, 40, 91, 31))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saveFile)



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 72, 15))
        self.label.setObjectName("label")
        self.L1 = QtWidgets.QTextEdit(self.centralwidget)
        self.L1.setGeometry(QtCore.QRect(20, 190, 411, 171))
        self.L1.setObjectName("L1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 371, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 371, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 371, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 72, 15))
        self.label_5.setObjectName("label_5")
        self.generation_first = QtWidgets.QPushButton(self.centralwidget)
        self.generation_first.setGeometry(QtCore.QRect(30, 370, 93, 28))
        self.generation_first.setObjectName("generation_first")
        self.generation_first.clicked.connect(self.gernerationFirst)

        self.generation_fllow = QtWidgets.QPushButton(self.centralwidget)
        self.generation_fllow.setGeometry(QtCore.QRect(130, 370, 93, 28))
        self.generation_fllow.setObjectName("generation_fllow")
        self.generation_fllow.clicked.connect(self.gernerationFllow)

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 410, 72, 15))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 600, 72, 15))
        self.label_7.setObjectName("label_7")
        self.L3 = QtWidgets.QTableView(self.centralwidget)
        self.L3.setGeometry(QtCore.QRect(20, 620, 410, 160))
        self.L3.setObjectName("L3")
        self.L2 = QtWidgets.QTableView(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(20, 430, 410, 160))
        self.L2.setObjectName("L2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 10, 72, 15))
        self.label_8.setObjectName("label_8")
        self.construction = QtWidgets.QPushButton(self.centralwidget)
        self.construction.setGeometry(QtCore.QRect(470, 40, 141, 28))
        self.construction.setObjectName("construction")
        self.construction.clicked.connect(self.constructAnalysis)


        self.R1 = QtWidgets.QTableView(self.centralwidget)
        self.R1.setGeometry(QtCore.QRect(470, 80, 711, 281))
        self.R1.setObjectName("R1")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 380, 72, 15))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(480, 400, 111, 31))
        self.label_10.setObjectName("label_10")
        self.R2 = QtWidgets.QLineEdit(self.centralwidget)
        self.R2.setGeometry(QtCore.QRect(580, 400, 601, 31))
        self.R2.setObjectName("R2")
        self.analyse = QtWidgets.QPushButton(self.centralwidget)
        self.analyse.setGeometry(QtCore.QRect(470, 440, 93, 28))
        self.analyse.setObjectName("analyse")
        self.analyse.clicked.connect(self.analy)


        self.stepdisplay = QtWidgets.QPushButton(self.centralwidget)
        self.stepdisplay.setGeometry(QtCore.QRect(580, 440, 93, 28))
        self.stepdisplay.setObjectName("stepdisplay")
        self.stepdisplay.clicked.connect(self.stepDisplay)


        self.alldisplay = QtWidgets.QPushButton(self.centralwidget)
        self.alldisplay.setGeometry(QtCore.QRect(690, 440, 93, 28))
        self.alldisplay.setObjectName("alldisplay")
        self.alldisplay.clicked.connect(self.allDisplay)



        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(470, 480, 72, 15))
        self.label_11.setObjectName("label_11")
        self.R3 = QtWidgets.QTableWidget(self.centralwidget)
        self.R3.setGeometry(QtCore.QRect(470, 500, 711, 281))
        self.R3.setObjectName("R3")
        self.R3.setColumnCount(3)
        self.R3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.R3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.R3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.R3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.R3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.R3.setHorizontalHeaderItem(2, item)
        Main.setCentralWidget(self.centralwidget)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "LL_1_"))
        self.openfile.setText(_translate("Main", "打开文件"))
        self.ok.setText(_translate("Main", "确认文法"))
        self.save.setText(_translate("Main", "保存文件"))
        self.label.setText(_translate("Main", "文法输入"))
        self.label_2.setText(_translate("Main", "请输入满足LL(1)最简判别的2型文法。一行一个产生式"))
        self.label_3.setText(_translate("Main", "请输入形如S->A的产生式,空格用_表示,空用#表示"))
        self.label_4.setText(_translate("Main", "开始符为第一个产生式的左部,非终结符用大写字母表示"))
        self.label_5.setText(_translate("Main", "注意事项："))
        self.generation_first.setText(_translate("Main", "生成First集"))
        self.generation_fllow.setText(_translate("Main", "生成Fllow集"))
        self.label_6.setText(_translate("Main", "First集"))
        self.label_7.setText(_translate("Main", "Follow集"))
        self.label_8.setText(_translate("Main", "预测分析表"))
        self.construction.setText(_translate("Main", "构造预测分析"))
        self.label_9.setText(_translate("Main", "分析句子"))
        self.label_10.setText(_translate("Main", "待分析的句子"))
        self.analyse.setText(_translate("Main", "分析"))
        self.stepdisplay.setText(_translate("Main", "单步显示"))
        self.alldisplay.setText(_translate("Main", "一键显示"))
        self.label_11.setText(_translate("Main", "分析结果"))
        item = self.R3.verticalHeaderItem(0)
        item.setText(_translate("Main", "测试列1"))
        item = self.R3.verticalHeaderItem(1)
        item.setText(_translate("Main", "试列2"))
        item = self.R3.horizontalHeaderItem(0)
        item.setText(_translate("Main", "测试行1"))
        item = self.R3.horizontalHeaderItem(1)
        item.setText(_translate("Main", "新建行2"))
        item = self.R3.horizontalHeaderItem(2)
        item.setText(_translate("Main", "测试行3"))

    def openFile(self):
        print("openFile")

    def inputGrammar(self):
        print("inputGrammar")

    def saveFile(self):
        print("saveFile")

    def gernerationFirst(self):
        print("gernerationFirst")

    def gernerationFllow(self):
        print("gernerationFllow")

    def constructAnalysis(self):
        print("constructAnalysis")

    def analy(self):
        print("analy")

    def stepDisplay(self):
        print("stepDisplay")
    
    def allDisplay(self):
        print("allDisplay")



def runwindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 


if __name__ == '__main__':
    runwindow()