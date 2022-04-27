import sys
from PyQt5 import QtCore, QtWidgets
from ExpresstoNFA import ExpressToNFA
from NFAtoDFA import NFATODFA
from DFAtoMinDFA import DFAtoMinDFA
import pickle


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(864, 634)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 10, 81, 21))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 111, 31))
        self.label_3.setObjectName("label_3")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setGeometry(QtCore.QRect(140, 40, 491, 31))
        self.input.setObjectName("input")


        self.check = QtWidgets.QPushButton(self.centralwidget)
        self.check.setGeometry(QtCore.QRect(650, 40, 93, 28))
        self.check.setObjectName("check")
        self.check.clicked.connect(self.checkFun)


        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(760, 40, 93, 28))
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(self.resetFun)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 80, 161, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 120, 111, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 120, 111, 21))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 140, 261, 361))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(300, 140, 261, 361))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(590, 140, 261, 361))
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 520, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 540, 81, 16))
        self.label_8.setObjectName("label_8")


        self.nfa_read = QtWidgets.QPushButton(self.centralwidget)
        self.nfa_read.setGeometry(QtCore.QRect(10, 570, 93, 28))
        self.nfa_read.setObjectName("nfa_read")
        self.nfa_read.clicked.connect(self.readNFAFun)

        self.nfa_generate = QtWidgets.QPushButton(self.centralwidget)
        self.nfa_generate.setGeometry(QtCore.QRect(110, 570, 93, 28))
        self.nfa_generate.setObjectName("nfa_generate")
        self.nfa_generate.clicked.connect(self.generationNFAFun)


        self.nfa_save = QtWidgets.QPushButton(self.centralwidget)
        self.nfa_save.setGeometry(QtCore.QRect(210, 570, 61, 28))
        self.nfa_save.setObjectName("nfa_save")
        self.nfa_save.clicked.connect(self.NFASaveFun)


        self.dfa_save = QtWidgets.QPushButton(self.centralwidget)
        self.dfa_save.setGeometry(QtCore.QRect(500, 570, 61, 28))
        self.dfa_save.setObjectName("dfa_save")
        self.dfa_save.clicked.connect(self.SaveDFAFun)


        self.dfa_read = QtWidgets.QPushButton(self.centralwidget)
        self.dfa_read.setGeometry(QtCore.QRect(300, 570, 93, 28))
        self.dfa_read.setObjectName("dfa_read")
        self.dfa_read.clicked.connect(self.readDFAFun)


        self.dfa_generate = QtWidgets.QPushButton(self.centralwidget)
        self.dfa_generate.setGeometry(QtCore.QRect(400, 570, 93, 28))
        self.dfa_generate.setObjectName("dfa_generate")
        self.dfa_generate.clicked.connect(self.generationDFAFun)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(310, 520, 91, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 540, 81, 16))
        self.label_10.setObjectName("label_10")
        self.mfa_init = QtWidgets.QLabel(self.centralwidget)
        self.mfa_init.setGeometry(QtCore.QRect(600, 520, 91, 16))
        self.mfa_init.setObjectName("mfa_init")
        self.mfa_eventual = QtWidgets.QLabel(self.centralwidget)
        self.mfa_eventual.setGeometry(QtCore.QRect(600, 540, 81, 16))
        self.mfa_eventual.setObjectName("mfa_eventual")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(650, 570, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.generationMGAFun)


        self.nfa_init = QtWidgets.QLabel(self.centralwidget)
        self.nfa_init.setGeometry(QtCore.QRect(110, 520, 72, 15))
        self.nfa_init.setObjectName("nfa_init")
        self.nfa_eventual = QtWidgets.QLabel(self.centralwidget)
        self.nfa_eventual.setGeometry(QtCore.QRect(110, 540, 72, 15))
        self.nfa_eventual.setObjectName("nfa_eventual")
        self.dfa_init = QtWidgets.QLabel(self.centralwidget)
        self.dfa_init.setGeometry(QtCore.QRect(400, 520, 72, 15))
        self.dfa_init.setObjectName("dfa_init")
        self.dfa_eventual = QtWidgets.QLabel(self.centralwidget)
        self.dfa_eventual.setGeometry(QtCore.QRect(400, 540, 72, 15))
        self.dfa_eventual.setObjectName("dfa_eventual")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(690, 520, 72, 15))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(690, 540, 72, 15))
        self.label_17.setObjectName("label_17")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NFA_DFA_MFA"))
        self.label_1.setText(_translate("MainWindow", "表达式"))
        self.label_2.setText(_translate("MainWindow", "正规式->NFA"))
        self.label_3.setText(_translate("MainWindow", "输入一个正规式"))
        self.check.setText(_translate("MainWindow", "验证"))
        self.reset.setText(_translate("MainWindow", "重置"))
        self.label_4.setText(_translate("MainWindow", "例如: (a* | b)*"))
        self.label_5.setText(_translate("MainWindow", "NFA->DFA"))
        self.label_6.setText(_translate("MainWindow", "DFA->MFA"))
        self.label_7.setText(_translate("MainWindow", "初始状态集:"))
        self.label_8.setText(_translate("MainWindow", "终止状态集:"))
        self.nfa_read.setText(_translate("MainWindow", "从文件读NFA"))
        self.nfa_generate.setText(_translate("MainWindow", "生成NFA文件"))
        self.nfa_save.setText(_translate("MainWindow", "保存"))
        self.dfa_save.setText(_translate("MainWindow", "保存"))
        self.dfa_read.setText(_translate("MainWindow", "从文件读DFA"))
        self.dfa_generate.setText(_translate("MainWindow", "生成DFA文件"))
        self.label_9.setText(_translate("MainWindow", "初始状态集:"))
        self.label_10.setText(_translate("MainWindow", "终止状态集:"))
        self.mfa_init.setText(_translate("MainWindow", "初始状态集:"))
        self.mfa_eventual.setText(_translate("MainWindow", "终止状态集:"))
        self.pushButton_9.setText(_translate("MainWindow", "生成MFA文件"))

        self.nfa_init.setText(_translate("MainWindow", "-"))
        self.nfa_eventual.setText(_translate("MainWindow", "-"))
        self.dfa_init.setText(_translate("MainWindow", "-"))
        self.dfa_eventual.setText(_translate("MainWindow", "-"))
        self.label_16.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "-"))

    def checkFun(self):
        try:
            self.resetFun()
            Express = self.input.text()
            if Express == None or Express.__len__()==0:
                raise TypeError("输入异常")
            self.EtoN = ExpressToNFA(Express)
            self.ENresult = self.EtoN.run()
            self.NtoD = NFATODFA(self.ENresult['HeadGraph'],self.ENresult['Head'],self.ENresult['Tail'])
            self.NDresult = self.NtoD.run()
            self.DtoM = DFAtoMinDFA(self.NDresult['DFAGraph'],self.NDresult['StartState'],self.NDresult['EndStates'])
            self.MDFA = self.DtoM.run()
            QtWidgets.QMessageBox.about(self.centralwidget,"正规式检查","输入的正规式正确")
        except Exception as T:
            QtWidgets.QMessageBox.about(self.centralwidget,"正规式检查","输入的正规式错误\n详情:"+str(T))
            print(T.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
            print(T.__traceback__.tb_lineno)            # 发生异常所在的行数
            self.resetFun()


    def resetFun(self):
        self.EtoN = None
        self.ENresult = None
        self.NtoD = None
        self.NDresult = None
        self.DtoM =     None
        self.MDFA =     None
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setText(_translate("MainWindow", ""))
        self.textEdit_2.setText(_translate("MainWindow", ""))
        self.textEdit_3.setText(_translate("MainWindow", ""))
        self.nfa_init.setText(_translate("MainWindow", "-"))
        self.nfa_eventual.setText(_translate("MainWindow", "-"))
        self.dfa_init.setText(_translate("MainWindow", "-"))
        self.dfa_eventual.setText(_translate("MainWindow", "-"))
        self.label_16.setText(_translate("MainWindow", "-"))
        self.label_17.setText(_translate("MainWindow", "-"))

    def readNFAFun(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open File", "./", "Txt (*.txt)")
        try:
            f = open(fname[0], 'rb')
            Restore = pickle.load(f)
            self.EtoN = Restore
            self.ENresult = self.EtoN.run()
            self.NtoD = NFATODFA(self.ENresult['HeadGraph'],self.ENresult['Head'],self.ENresult['Tail'])
            self.NDresult = self.NtoD.run()
            self.DtoM = DFAtoMinDFA(self.NDresult['DFAGraph'],self.NDresult['StartState'],self.NDresult['EndStates'])
            self.MDFA = self.DtoM.run()
            self.generationNFAFun()
            self.generationDFAFun()
            self.generationMGAFun()
        except:
            QtWidgets.QMessageBox.about(self.centralwidget,"生成错误","请确保操作正确")
            return

    def generationNFAFun(self):
        if self.ENresult == None:
            QtWidgets.QMessageBox.about(self.centralwidget,"生成错误","请确保操作正确")
            return
        _translate = QtCore.QCoreApplication.translate
        self.textEdit.setText(_translate("MainWindow", self.ENresult['GraphInfo']))
        self.nfa_init.setText(_translate("MainWindow", str(self.ENresult['Head'])))
        self.nfa_eventual.setText(_translate("MainWindow", str(self.ENresult['Tail'])))

    def NFASaveFun(self):
        try:
            data = self.EtoN
            f = open('NFASave.txt', 'wb')
            pickle.dump(data, f)
            QtWidgets.QMessageBox.about(self.centralwidget,"文件写入","文件写入完成")
        except Exception as F:
            QtWidgets.QMessageBox.about(self.centralwidget,"保存错误","请确保操作正确\n详情"+str(F))
            return


    def readDFAFun(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget, "Open File", "./", "Txt (*.txt)")
        try: 
            f = open(fname[0], 'rb')
            Restore = pickle.load(f)
            self.NtoD =Restore
            self.NDresult = self.NtoD.run()
            self.DtoM = DFAtoMinDFA(self.NDresult['DFAGraph'],self.NDresult['StartState'],self.NDresult['EndStates'])
            self.MDFA = self.DtoM.run()
            self.generationDFAFun()
            self.generationMGAFun()
        except:
            QtWidgets.QMessageBox.about(self.centralwidget,"生成错误","请确保操作正确")
            return


    def generationDFAFun(self):
        if self.NDresult == None:
            QtWidgets.QMessageBox.about(self.centralwidget,"生成错误","请确保操作正确")
            return
        _translate = QtCore.QCoreApplication.translate
        self.textEdit_2.setText(_translate("MainWindow", self.NDresult['GraphInfo']))
        self.dfa_init.setText(_translate("MainWindow", str(self.NDresult['StartState'])))
        self.dfa_eventual.setText(_translate("MainWindow",  " ".join(str(i) for i in self.NDresult['EndStates'])  ))

    def SaveDFAFun(self):
        try:
            data = self.NtoD
            f = open('DFASave.txt', 'wb')
            pickle.dump(data, f)
            QtWidgets.QMessageBox.about(self.centralwidget,"文件写入","文件写入完成")
        except Exception as F:
            QtWidgets.QMessageBox.about(self.centralwidget,"保存错误","请确保操作正确\n详情"+str(F))
            return


        if self.NtoD == None:
            QtWidgets.QMessageBox.about(self.centralwidget,"保存错误","请确保操作正确")
            return
        



    def generationMGAFun(self):
        if self.MDFA == None:
            QtWidgets.QMessageBox.about(self.centralwidget,"生成错误","请确保操作正确")
            return
        _translate = QtCore.QCoreApplication.translate
        self.textEdit_3.setText(_translate("MainWindow", self.MDFA['GraphInfo']))
        self.label_16.setText(_translate("MainWindow", str(self.MDFA['StartState'])))
        self.label_17.setText(_translate("MainWindow",  " ".join(str(i) for i in self.MDFA['EndStates'])  ))


def runwindow():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow) 
    MainWindow.show()
    sys.exit(app.exec_()) 

if __name__ == "__main__":
    runwindow()