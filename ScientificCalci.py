from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import math
import numpy
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Ui_MainWindow(object):
    eqpress = False


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 540)
        MainWindow.setAutoFillBackground(False)
        self.value=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(6, 16, 941, 111))
        self.label.setStyleSheet("background-color : white")
        self.label.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label.setLineWidth(5)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.ansButton = QtWidgets.QPushButton(self.centralwidget)
        self.ansButton.setGeometry(QtCore.QRect(10, 150, 270, 61))
        self.ansButton.setStyleSheet("background-color : cyan")
        font = QtGui.QFont()
        font.setPointSize(29)
        self.ansButton.setFont(font)
        self.ansButton.setAutoDefault(True)
        self.ansButton.setDefault(False)
        self.ansButton.setFlat(False)
        self.ansButton.setObjectName("ansButton")
        self.InvButton = QtWidgets.QPushButton(self.centralwidget)
        self.InvButton.setGeometry(QtCore.QRect(10, 220, 121, 61))
        self.InvButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.InvButton.setFont(font)
        self.InvButton.setObjectName("InvButton")
        self.piButton = QtWidgets.QPushButton(self.centralwidget)
        self.piButton.setGeometry(QtCore.QRect(10, 290, 121, 61))
        self.piButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(32)
        self.piButton.setFont(font)
        self.piButton.setIconSize(QtCore.QSize(16, 16))
        self.piButton.setObjectName("piButton")
        self.eButton = QtWidgets.QPushButton(self.centralwidget)
        self.eButton.setGeometry(QtCore.QRect(10, 360, 121, 61))
        self.eButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.eButton.setFont(font)
        self.eButton.setObjectName("eButton")
        self.squareButton = QtWidgets.QPushButton(self.centralwidget)
        self.squareButton.setGeometry(QtCore.QRect(10, 430, 121, 61))
        self.squareButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.squareButton.setFont(font)
        self.squareButton.setObjectName("squareButton")
        self.sinButton = QtWidgets.QPushButton(self.centralwidget)
        self.sinButton.setGeometry(QtCore.QRect(160, 220, 121, 61))
        self.sinButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(23)
        self.sinButton.setFont(font)
        self.sinButton.setObjectName("sinButton")
        self.cosButton = QtWidgets.QPushButton(self.centralwidget)
        self.cosButton.setGeometry(QtCore.QRect(160, 290, 121, 61))
        self.cosButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.cosButton.setFont(font)
        self.cosButton.setObjectName("cosButton")
        self.tanButton = QtWidgets.QPushButton(self.centralwidget)
        self.tanButton.setGeometry(QtCore.QRect(160, 360, 121, 61))
        self.tanButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.tanButton.setFont(font)
        self.tanButton.setObjectName("tanButton")
        self.expButton = QtWidgets.QPushButton(self.centralwidget)
        self.expButton.setGeometry(QtCore.QRect(160, 430, 121, 61))
        self.expButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.expButton.setFont(font)
        self.expButton.setObjectName("expButton")
        self.factButton = QtWidgets.QPushButton(self.centralwidget)
        self.factButton.setGeometry(QtCore.QRect(290, 150, 131, 61))
        self.factButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(25)
        self.factButton.setFont(font)
        self.factButton.setObjectName("factButton")
        self.lnButton = QtWidgets.QPushButton(self.centralwidget)
        self.lnButton.setGeometry(QtCore.QRect(290, 220, 131, 61))
        self.lnButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lnButton.setFont(font)
        self.lnButton.setObjectName("lnButton")
        self.logButton = QtWidgets.QPushButton(self.centralwidget)
        self.logButton.setGeometry(QtCore.QRect(290, 290, 131, 61))
        self.logButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.logButton.setFont(font)
        self.logButton.setObjectName("logButton")
        self.rootButton = QtWidgets.QPushButton(self.centralwidget)
        self.rootButton.setGeometry(QtCore.QRect(290, 360, 131, 61))
        self.rootButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(27)
        self.rootButton.setFont(font)
        self.rootButton.setObjectName("rootButton")
        self.raiseButton = QtWidgets.QPushButton(self.centralwidget)
        self.raiseButton.setGeometry(QtCore.QRect(290, 430, 131, 61))
        self.raiseButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(19)
        self.raiseButton.setFont(font)
        self.raiseButton.setObjectName("raiseButton")
        self.openbracButton = QtWidgets.QPushButton(self.centralwidget)
        self.openbracButton.setGeometry(QtCore.QRect(430, 150, 131, 61))
        self.openbracButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(21)
        self.openbracButton.setFont(font)
        self.openbracButton.setObjectName("openbracButton")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(430, 220, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Button7.setFont(font)
        self.Button7.setObjectName("Button7")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(430, 290, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button4.setFont(font)
        self.Button4.setObjectName("Button4")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(430, 360, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button1.setFont(font)
        self.Button1.setObjectName("Button1")
        self.Button0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button0.setGeometry(QtCore.QRect(430, 430, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button0.setFont(font)
        self.Button0.setObjectName("Button0")
        self.closebracButton = QtWidgets.QPushButton(self.centralwidget)
        self.closebracButton.setGeometry(QtCore.QRect(568, 150, 121, 61))
        self.closebracButton.setStyleSheet("background-color : gray")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.closebracButton.setFont(font)
        self.closebracButton.setObjectName("closebracButton")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(570, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Button8.setFont(font)
        self.Button8.setObjectName("Button8")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(570, 290, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button5.setFont(font)
        self.Button5.setObjectName("Button5")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(570, 360, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Button2.setFont(font)
        self.Button2.setObjectName("Button2")
        self.decButton = QtWidgets.QPushButton(self.centralwidget)
        self.decButton.setGeometry(QtCore.QRect(570, 430, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.decButton.setFont(font)
        self.decButton.setObjectName("decButton")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(700, 150, 121, 61))
        self.delButton.setStyleSheet("background-color : red")
        font = QtGui.QFont()
        font.setPointSize(19)
        self.delButton.setFont(font)
        self.delButton.setObjectName("delButton")
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(700, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.Button9.setFont(font)
        self.Button9.setObjectName("Button9")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(700, 290, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button6.setFont(font)
        self.Button6.setObjectName("Button6")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(700, 360, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.Button3.setFont(font)
        self.Button3.setObjectName("Button3")
        self.equButton = QtWidgets.QPushButton(self.centralwidget)
        self.equButton.setGeometry(QtCore.QRect(700, 430, 121, 61))
        self.equButton.setStyleSheet("background-color : blue")
        font = QtGui.QFont()
        font.setPointSize(23)
        self.equButton.setFont(font)
        self.equButton.setObjectName("equButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(830, 150, 121, 61))
        self.clearButton.setStyleSheet("background-color :green")
        font = QtGui.QFont()
        font.setPointSize(21)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.divButton = QtWidgets.QPushButton(self.centralwidget)
        self.divButton.setGeometry(QtCore.QRect(828, 220, 121, 61))
        self.divButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(31)
        self.divButton.setFont(font)
        self.divButton.setObjectName("divButton")
        self.mulButton = QtWidgets.QPushButton(self.centralwidget)
        self.mulButton.setGeometry(QtCore.QRect(830, 290, 121, 61))
        self.mulButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(19)
        self.mulButton.setFont(font)
        self.mulButton.setObjectName("mulButton")
        self.subButton = QtWidgets.QPushButton(self.centralwidget)
        self.subButton.setGeometry(QtCore.QRect(830, 360, 121, 61))
        self.subButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(23)
        self.subButton.setFont(font)
        self.subButton.setObjectName("subButton")
        self.plusButton = QtWidgets.QPushButton(self.centralwidget)
        self.plusButton.setGeometry(QtCore.QRect(830, 430, 121, 61))
        self.plusButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(23)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        """ self.degButton = QtWidgets.QPushButton(self.centralwidget)
        self.degButton.setGeometry(QtCore.QRect(150, 150, 131, 61))
        self.degButton.setStyleSheet("background-color :gray")
        font = QtGui.QFont()
        font.setPointSize(30)
        self.degButton.setFont(font)
        self.degButton.setObjectName("degButton") """
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        #self.menubar.setEnabled(False)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 958, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Calculator = QtWidgets.QMenu(self.menubar)
        self.menu_Calculator.setObjectName("menu_Calculator")
        MainWindow.setMenuBar(self.menubar)

        """self.menu_Calculator.addSeparator()
        self.menu_Calculator.addSeparator()
        self.menu_Calculator.addSeparator()
        self.menu_Calculator.addSeparator()
        self.menu_Calculator.addSeparator()
        self.menu_Calculator.addSeparator()
        self.menubar.addAction(self.menu_Calculator.menuAction())"""
        self.arr = []
        self.ans=""
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scientific Calculator"))
        self.label.setText(_translate("MainWindow", ""))
        self.ansButton.setText(_translate("MainWindow", "ANS"))
        self.InvButton.setText(_translate("MainWindow", "Inv"))
        self.piButton.setText(_translate("MainWindow", "𝝅"))
        self.eButton.setText(_translate("MainWindow", "e"))
        self.squareButton.setText(_translate("MainWindow", "x^2"))
        self.sinButton.setText(_translate("MainWindow", "sin"))
        self.cosButton.setText(_translate("MainWindow", "cos"))
        self.tanButton.setText(_translate("MainWindow", "tan"))
        self.expButton.setText(_translate("MainWindow", "%"))
        self.factButton.setText(_translate("MainWindow", "x!"))
        self.lnButton.setText(_translate("MainWindow", "ln"))
        self.logButton.setText(_translate("MainWindow", "log"))
        self.rootButton.setText(_translate("MainWindow", "√"))
        self.raiseButton.setText(_translate("MainWindow", "x^y"))
        self.openbracButton.setText(_translate("MainWindow", "("))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.closebracButton.setText(_translate("MainWindow", ")"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.decButton.setText(_translate("MainWindow", "."))
        self.delButton.setText(_translate("MainWindow", "DEL"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.equButton.setText(_translate("MainWindow", "="))
        self.clearButton.setText(_translate("MainWindow", "AC"))
        self.divButton.setText(_translate("MainWindow", "÷"))
        self.mulButton.setText(_translate("MainWindow", "X"))
        self.subButton.setText(_translate("MainWindow", "-"))
        self.plusButton.setText(_translate("MainWindow", "+"))
        #self.degButton.setText(_translate("MainWindow", "DEG"))
        self.menu_Calculator.setTitle(_translate("MainWindow", " History"))

        self.Button0.clicked.connect(self.action0)
        self.Button1.clicked.connect(self.action1)
        self.Button2.clicked.connect(self.action2)
        self.Button3.clicked.connect(self.action3)
        self.Button4.clicked.connect(self.action4)
        self.Button5.clicked.connect(self.action5)
        self.Button6.clicked.connect(self.action6)
        self.Button7.clicked.connect(self.action7)
        self.Button8.clicked.connect(self.action8)
        self.Button9.clicked.connect(self.action9)
        self.decButton.clicked.connect(self.action_point)
        self.plusButton.clicked.connect(self.action_plus)
        self.subButton.clicked.connect(self.action_minus)
        self.divButton.clicked.connect(self.action_div)
        self.mulButton.clicked.connect(self.action_mul)
        self.equButton.clicked.connect(self.action_equal)
        self.clearButton.clicked.connect(self.action_clear)
        self.openbracButton.clicked.connect(self.action_openbrac)
        self.closebracButton.clicked.connect(self.action_closebrac)
        self.delButton.clicked.connect(self.action_del)
        self.raiseButton.clicked.connect(self.action_raise)
        self.InvButton.clicked.connect(self.action_inverse)
        self.logButton.clicked.connect(self.action_log)
        self.sinButton.clicked.connect(self.action_sin)
        self.cosButton.clicked.connect(self.action_cos)
        self.tanButton.clicked.connect(self.action_tan)
        self.rootButton.clicked.connect(self.action_root)
        self.lnButton.clicked.connect(self.action_ln)
        self.eButton.clicked.connect(self.action_e)
        self.piButton.clicked.connect(self.action_pi)
        self.factButton.clicked.connect(self.action_fact)
        self.ansButton.clicked.connect(self.action_ans)
        self.expButton.clicked.connect(self.action_mod)
        self.squareButton.clicked.connect(self.action_square)
        

        
    
    def action_equal(self):
  
        # get the label text
        equation = self.label.text()
        eq = self.value
        if equation!="":
            try:
                # getting the ans
                ans = eval(eq)
                self.ans = ans
                self.value = str(ans)
                self.label.setText(str(ans))
                self.actionOper = QtWidgets.QAction(MainWindow)
                self.menu_Calculator.addAction(self.actionOper)
                self.menu_Calculator.addSeparator()
                self.menubar.addAction(self.menu_Calculator.menuAction())
                eq1 = equation+" = "+str(ans)
                self.menubar.triggered.connect(self.menu_action)
                self.actionOper.setText(eq1)
                self.eqpress = True
            except:
                # setting text to the label
                msg = QMessageBox()
                msg.setWindowTitle("Scientific Calculator")
                msg.setText("Wrong Input")
                msg.exec_()
                self.label.setText("")

    def menu_action(self,action):
        self.label.setText(action.text().split(" = ")[0])
        self.value = action.text().split(" = ")[0].replace("x", "*")
        self.value = self.value.replace("÷", "/")
        self.value = self.value.replace("^ ", "**")
        self.value = self.value.replace("sin(", "math.sin(")
        self.value = self.value.replace("cos(", "math.cos(")
        self.value = self.value.replace("tan(", "math.tan(")
        self.value = self.value.replace("log(", "math.log(")
        self.value = self.value.replace("√(", "math.sqrt(")
        self.value = self.value.replace("e", "2.718281828459045")
        self.value = self.value.replace("𝜋", "3.14159265359")
  
    def action_plus(self):
        # appending label text
        text = self.label.text()
        if text[-3:] == " - " or text[-3:] == " ÷ " or text[-3:] == " x ":
            text = text[:-3]
            self.value = self.value[:-3]# for replacing the operator
        elif text[-1] == ".":
            text = text[:-1]
            self.value = self.value[:-1]
        self.value = self.value + " + "
        self.label.setText(text + " + ")
        self.eqpress = False
  
    def action_minus(self):
        # appending label text
        text = self.label.text()
        if text[-3:] == " + ":
            text = text[:-3]
            self.value = self.value[:-3]  # for replacing the operator
        elif text[-1] == ".":
            text = text[:-1]
            self.value = self.value[:-1]
        self.value = self.value + " - "
        self.label.setText(text + " - ")
        self.eqpress = False
  
    def action_div(self):
        # appending label text
        text = self.label.text()
        if text[-3:] == " - " or text[-3:] == " + " or text[-3:] == " x ":
            text = text[:-3]
            self.value = self.value[:-3]  # for replacing the operator
        elif text[-1] == ".":
            text = text[:-1]
            self.value = self.value[:-1]
        self.value = self.value + " / "
        self.label.setText(text + " ÷ ")
        self.eqpress = False
  
    def action_mul(self):
        # appending label text
        text = self.label.text()
        if text[-3:] == " - " or text[-3:] == " + " or text[-3:] == " ÷ ":
            text = text[:-3]
            self.value = self.value[:-3]  # for replacing the operator
        elif text[-1] == ".":
            text = text[:-1]
            self.value = self.value[:-1]
        self.value = self.value + " * "
        self.label.setText(text + " x ")
        self.eqpress = False
        
  
    def action_point(self):
        # appending label text
        self.value = self.value + "."
        text = self.label.text()
        self.label.setText(text + ".")
  
    def action0(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "0"
        self.label.setText(text + "0")
        self.eqpress = False
  
    def action1(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "1"
        self.label.setText(text + "1")
        self.eqpress = False
  
    def action2(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "2"
        self.label.setText(text + "2")
        self.eqpress = False
  
    def action3(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "3"
        self.label.setText(text + "3")
        self.eqpress = False
  
    def action4(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "4"
        self.label.setText(text + "4")
        self.eqpress = False
  
    def action5(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "5"
        self.label.setText(text + "5")
        self.eqpress = False
  
    def action6(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "6"
        self.label.setText(text + "6")
        self.eqpress = False
  
    def action7(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "7"
        self.label.setText(text + "7")
        self.eqpress = False
  
    def action8(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "8"
        self.label.setText(text + "8")
        self.eqpress = False
  
    def action9(self):
        # appending label text
        text = self.label.text()
        if text == "" or self.eqpress:
            text = ""
            self.value = ""
        elif text[-3:] == "+ 0" or text[-3:] == "- 0" or text[-3:] == "x 0" or text[-3:] == "÷ 0":
            text = text[:-1]
        self.value = self.value + "9"
        self.label.setText(text + "9")
        self.eqpress = False
  
    def action_clear(self):
        # clearing the label text
        self.label.setText("")
        self.value = ""
        self.eqpress = False

    def action_openbrac(self):
        # appending label text
        self.value = self.value + "("
        text = self.label.text()
        self.label.setText(text + "(")
    
    def action_closebrac(self):
        # appending label text
        self.value = self.value + ")"
        text = self.label.text()
        self.label.setText(text + ")")

    def action_raise(self):
        # appending label text
        text = self.label.text()
        self.value = self.value + "**"
        self.label.setText(text + "^ ")

    def action_inverse(self):
        # appending label text
        self.value = self.value + "**-1"
        text = self.label.text()
        self.label.setText(text + "^ -1")

    def action_square(self):
        # appending label text
        self.value = self.value + "**2"
        text = self.label.text()
        self.label.setText(text + "^2 ")

    def action_log(self):
        # appending label text
        self.value = self.value + "math.log("
        text = self.label.text()
        self.label.setText(text + "log(")

    def action_ln(self):
        # appending label text
        self.value = self.value + "numpy.log("
        text = self.label.text()
        self.label.setText(text + "ln(")

    def action_sin(self):
        # appending label text
        self.value = self.value + "math.sin("
        text = self.label.text()
        self.label.setText(text + "sin(")
    
    def action_cos(self):
        # appending label text
        self.value = self.value + "math.cos("
        text = self.label.text()
        self.label.setText(text + "cos(")

    def action_tan(self):
        # appending label text
        self.value = self.value + "math.tan("
        text = self.label.text()
        self.label.setText(text + "tan(")

    def action_root(self):
        # appending label text
        self.value = self.value + "math.sqrt("
        text = self.label.text()
        self.label.setText(text + "√(")

    def action_mod(self):
        # appending label text
        self.value = self.value + " % "
        text = self.label.text()
        self.label.setText(text + " % ")

    def action_e(self):
        # appending label text
        self.value = self.value + "2.718281828459045"
        text = self.label.text()
        self.label.setText(text + "e")

    def action_pi(self):
        # appending label text
        self.value = self.value + "3.14159265359"
        text = self.label.text()
        self.label.setText(text + "𝜋")

    def action_ans(self):
        # appending label text
        self.value = self.value + str(self.ans)
        text = self.label.text()
        self.label.setText(text + str(self.ans))

    def action_fact(self):
        # appending label text
        text = self.label.text()
        arr = text.split()
        arr[-1] = math.factorial(int(arr[-1]))
        print(arr[-1])
        fact = str(arr[-1])
        self.value = str(self.value[:-1] + fact)
        print(self.value)
        print(eval(self.value))
        self.label.setText(text + "!")

    def action_del(self):
        # clearing a single digit
        equ = self.value
        text = self.label.text()
        if text[-4:]=="sin(" or text[-4:]=="cos(" or text[-4:]=="tan(" or text[-4:]=="log(":
            self.label.setText(text[:-4])
            self.value = equ[:-9]
        elif text[-3:]=="ln(":
            self.label.setText(text[:-3])
            self.value = equ[:-10]
        elif equ[-2:]=="**":
            self.label.setText(text[:-2])
            self.value = equ[:-2]
        elif equ[-3:]=="**2":
            self.label.setText(text[:-3])
            self.value = equ[:-3]
        elif equ[-4:]=="**-1":
            self.label.setText(text[:-4])
            self.value = equ[:-4]
        elif text[-2:]=="√(":
            self.label.setText(text[:-2])
            self.value = equ[:-10]
        elif text[-1:]=="𝜋":
            self.label.setText(text[:-1])
            self.value = equ[:-13]
        elif text[-1:]=="e":
            self.label.setText(text[:-1])
            self.value = equ[:-17]
        else:
            self.value = (self.value[:len(self.value)-1])
            self.label.setText(text[:len(text)-1])
        #print(text[:len(text) - 1])


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_0:
            self.action0()

        elif e.key() == Qt.Key_1:
            self.action1()

        elif e.key() == Qt.Key_2:
            self.action2()

        elif e.key() == Qt.Key_3:
            self.action3()

        elif e.key() == Qt.Key_4:
            self.action4()

        elif e.key() == Qt.Key_5:
            self.action5()

        elif e.key() == Qt.Key_6:
            self.action6()

        elif e.key() == Qt.Key_7:
            self.action7()

        elif e.key() == Qt.Key_8:
            self.action8()

        elif e.key() == Qt.Key_9:
            self.action9()

        elif e.key() == Qt.Key_Enter or e.key() == Qt.Key_Equal or e.key() == Qt.Key_Return:
            self.action_equal()

        elif e.key() == Qt.Key_Plus:
            self.action_plus()

        elif e.key() == Qt.Key_Minus:
            self.action_minus()

        elif e.key() == Qt.Key_Asterisk:
            self.action_mul()

        elif e.key() == Qt.Key_Slash:
            self.action_div()

        elif e.key() == Qt.Key_Backspace:
            self.action_del()

        elif e.key() == Qt.Key_Delete:
            self.action_clear()

        elif e.key() == Qt.Key_Period:
            self.action_point()

        elif e.key() == Qt.Key_ParenLeft:
            self.action_openbrac()

        elif e.key() == Qt.Key_ParenRight:
            self.action_closebrac()

        elif e.key() == Qt.Key_Percent:
            self.action_mod()

        elif e.key() == Qt.Key_AsciiCircum:
            self.action_raise()

        elif e.key() == Qt.Key_Exclam:
            self.action_fact()
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    """MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)"""
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())

