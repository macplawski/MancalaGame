from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog
import sys

class Ui_MainWindow(object):
    whoMove = 2
    buttonList = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1017, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuGra = QtWidgets.QMenu(self.menubar)
        self.menuGra.setObjectName("menuGra")
        self.menuPomoc = QtWidgets.QMenu(self.menubar)
        self.menuPomoc.setObjectName("menuPomoc")
        MainWindow.setMenuBar(self.menubar)
        self.actionInfo = QtWidgets.QAction(MainWindow)
        self.actionInfo.setObjectName("actionInfo")
        self.actionNowa_gra = QtWidgets.QAction(MainWindow)
        self.actionNowa_gra.setObjectName("actionNowa_gra")
        self.actionWczytaj_gr = QtWidgets.QAction(MainWindow)
        self.actionWczytaj_gr.setObjectName("actionWczytaj_gr")
        self.actionZapisz_gr = QtWidgets.QAction(MainWindow)
        self.actionZapisz_gr.setObjectName("actionZapisz_gr")
        self.menuGra.addAction(self.actionNowa_gra)
        self.menuGra.addAction(self.actionWczytaj_gr)
        self.menuGra.addAction(self.actionZapisz_gr)
        self.menuPomoc.addAction(self.actionInfo)
        self.menubar.addAction(self.menuGra.menuAction())
        self.menubar.addAction(self.menuPomoc.menuAction())

        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(60, 120, 61, 341))
        self.label2.setStyleSheet("border-radius : 30; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label1")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(880, 120, 61, 351))
        self.label1.setStyleSheet("border-radius : 30; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label1.setFont(font)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label2")


        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(270, 230, 471, 131))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label3.setFont(font)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")

        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(40, 70, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label4.setFont(font)
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setObjectName("label4")
        self.label5 = QtWidgets.QLabel(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(880, 490, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label5.setFont(font)
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setObjectName("label5")

        self.button12 = QtWidgets.QPushButton(self.centralwidget)
        self.button12.setGeometry(QtCore.QRect(150, 110, 101, 101))
        self.button12.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button12.setFont(font)
        self.button12.setObjectName("button12")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(630, 380, 101, 101)
        self.button5.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(510, 380, 101, 101))
        self.button4.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(390, 380, 101, 101))
        self.button3.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(270, 380, 101, 101))
        self.button2.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(150, 380, 101, 101))
        self.button1.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(750, 110, 101, 101))
        self.button7.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button7.setFont(font)
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(630, 110, 101, 101))
        self.button8.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button8.setFont(font)
        self.button8.setObjectName("button8")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(510, 110, 101, 101))
        self.button9.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button9.setFont(font)
        self.button9.setObjectName("button9")
        self.button10 = QtWidgets.QPushButton(self.centralwidget)
        self.button10.setGeometry(QtCore.QRect(390, 110, 101, 101))
        self.button10.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button10.setFont(font)
        self.button10.setObjectName("button10")
        self.button11 = QtWidgets.QPushButton(self.centralwidget)
        self.button11.setGeometry(QtCore.QRect(270, 110, 101, 101))
        self.button11.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button11.setFont(font)
        self.button11.setObjectName("button11")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(750, 380, 101, 101))
        self.button6.setStyleSheet("border-radius : 50; border : 2px solid black")
        font = QtGui.QFont()
        font.setPointSize(20)
        self.button6.setFont(font)
        self.button6.setObjectName("button6")

        self.buttonList.append(self.button1)
        self.buttonList.append(self.button2)
        self.buttonList.append(self.button3)
        self.buttonList.append(self.button4)
        self.buttonList.append(self.button5)
        self.buttonList.append(self.button6)
        self.buttonList.append(self.label1)
        self.buttonList.append(self.button7)
        self.buttonList.append(self.button8)
        self.buttonList.append(self.button9)
        self.buttonList.append(self.button10)
        self.buttonList.append(self.button11)
        self.buttonList.append(self.button12)
        self.buttonList.append(self.label2)

        self.actionInfo.triggered.connect(self.infoMessage)
        self.actionNowa_gra.triggered.connect(self.newGame)
        self.actionWczytaj_gr.triggered.connect(self.loadGame)
        self.actionZapisz_gr.triggered.connect(self.saveGame)

        self.button1.clicked.connect(lambda : self.move(0))
        self.button2.clicked.connect(lambda : self.move(1))
        self.button3.clicked.connect(lambda : self.move(2))
        self.button4.clicked.connect(lambda : self.move(3))
        self.button5.clicked.connect(lambda : self.move(4))
        self.button6.clicked.connect(lambda : self.move(5))
        self.button7.clicked.connect(lambda : self.move(7))
        self.button8.clicked.connect(lambda : self.move(8))
        self.button9.clicked.connect(lambda : self.move(9))
        self.button10.clicked.connect(lambda : self.move(10))
        self.button11.clicked.connect(lambda : self.move(11))
        self.button12.clicked.connect(lambda : self.move(12))

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mankala"))

        self.menuGra.setTitle(_translate("MainWindow", "Gra"))
        self.menuPomoc.setTitle(_translate("MainWindow", "Pomoc"))
        self.actionInfo.setText(_translate("MainWindow", "Info"))
        self.actionNowa_gra.setText(_translate("MainWindow", "Nowa gra"))
        self.actionWczytaj_gr.setText(_translate("MainWindow", "Wczytaj grę"))
        self.actionZapisz_gr.setText(_translate("MainWindow", "Zapisz grę"))

        self.label1.setText(_translate("MainWindow", "0"))
        self.label2.setText(_translate("MainWindow", "0"))
        self.label4.setText(_translate("MainWindow", "Gracz 1"))
        self.label5.setText(_translate("MainWindow", "Gracz 2"))
        self.button1.setText(_translate("MainWindow", "4"))
        self.button2.setText(_translate("MainWindow", "4"))
        self.button3.setText(_translate("MainWindow", "4"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button5.setText(_translate("MainWindow", "4"))
        self.button6.setText(_translate("MainWindow", "4"))
        self.button7.setText(_translate("MainWindow", "4"))
        self.button8.setText(_translate("MainWindow", "4"))
        self.button9.setText(_translate("MainWindow", "4"))
        self.button10.setText(_translate("MainWindow", "4"))
        self.button11.setText(_translate("MainWindow", "4"))
        self.button12.setText(_translate("MainWindow", "4"))

    def newGame(self):
        a = self.checkMessage("Czy na pewno chcesz otworzyć nową grę?")
        if not a:
            return
        if not self.isGameEnd():
            b = self.checkMessage("Czy chcesz zapisać istniejącą grę?")
            if b:
                self.saveGame()

        self.label1.setText("0")
        self.label2.setText("0")
        self.label3.setText("")
        self.button1.setText("4")
        self.button2.setText("4")
        self.button3.setText("4")
        self.button4.setText("4")
        self.button5.setText("4")
        self.button6.setText("4")
        self.button7.setText("4")
        self.button8.setText("4")
        self.button9.setText("4")
        self.button10.setText("4")
        self.button11.setText("4")
        self.button12.setText("4")

        for x in range(0, 13):
            self.buttonList[x].setEnabled(True)
        self.label2.setStyleSheet("border-radius : 30; border : 2px solid black")
        self.label1.setStyleSheet("border-radius : 30; border : 2px solid black")

        self.label4.setStyleSheet("")
        self.label5.setStyleSheet("")

    def checkWhoMove(self):
        if self.whoMove % 2:
            for x in range(0, 6):
                self.buttonList[x].setEnabled(True)
                self.label4.setStyleSheet("")
            for x in range(7, 13):
                self.buttonList[x].setEnabled(False)
                self.label5.setStyleSheet("background-color: cyan;")
        else:
            for x in range(0, 6):
                self.buttonList[x].setEnabled(False)
                self.label5.setStyleSheet("")
            for x in range(7, 13):
                self.buttonList[x].setEnabled(True)
                self.label4.setStyleSheet("background-color: cyan;")

    def checkMessage(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Potwierdzenie")
        msg.setText(text)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY = msg.button(QMessageBox.Yes)
        buttonY.setText('Tak')
        buttonN = msg.button(QMessageBox.No)
        buttonN.setText('Nie')
        ret = msg.exec_()
        if ret == QMessageBox.Yes:
            return 1
        else:
            return 0

    def move(self, nr):
        numberOfStones = int(self.buttonList[nr].text())
        if self.checkMessage("Czy chcesz wykonać ruch?") == False:
            return

        if self.buttonList[nr].text() == "0":
            return
        if nr < 6:
            self.whoMove = 0
        else:
            self.whoMove = 1

        self.buttonList[nr].setText("0")

        x = 0
        while x < numberOfStones:
            x += 1
            if self.whoMove == 1 and ((nr+x) % 14) == 6:
                numberOfStones += 1
                continue
            elif self.whoMove == 0 and ((nr+x) % 14) == 13:
                numberOfStones += 1
                continue
            self.buttonList[(nr+x) % 14].setText(str(int(self.buttonList[(nr+x) % 14].text())+1))

        if self.buttonList[(nr+x) % 14].text() == "1" and ((nr+x) % 14) != 6 and ((nr+x) % 14) != 13 and self.buttonList[12 - (nr + x)].text() != "0":
            if nr < 6 and ((nr + x) % 13) < 6:
                self.buttonList[6].setText(str(int(self.buttonList[(nr+x) % 14].text()) + int(self.buttonList[6].text())+int(self.buttonList[12 - (nr + x)].text())))
                self.buttonList[12 - (nr + x)].setText("0")
                self.buttonList[(nr + x) % 14].setText("0")
            elif nr > 6 and nr < 13 and ((nr + x) % 13) < 13 and ((nr + x) % 13) > 6:
                self.buttonList[13].setText(str(int(self.buttonList[(nr+x) % 14].text()) + int(self.buttonList[13].text())+int(self.buttonList[12 - (nr + x)].text())))
                self.buttonList[12 - (nr + x)].setText("0")
                self.buttonList[(nr + x) % 14].setText("0")

        if self.whoMove == 0 and ((nr+x) % 14) == 6:
            self.whoMove = 1
        elif self.whoMove == 1 and ((nr+x) % 14) == 13:
            self.whoMove = 0

        self.checkWhoMove()

        if self.isGameEnd():
            a = self.whoWin()
            if a == 1:
                self.label3.setText("Wygrał gracz nr 2")
                self.label1.setStyleSheet("background-color: green; border-radius : 30; border : 2px solid black")
                self.label2.setStyleSheet("background-color: red; border-radius : 30; border : 2px solid black")
            elif a == 2:
                self.label3.setText("Wygrał gracz nr 1")
                self.label2.setStyleSheet("background-color: green; border-radius : 30; border : 2px solid black")
                self.label1.setStyleSheet("background-color: red; border-radius : 30; border : 2px solid black")
            else:
                self.label3.setText("Remis")
                self.label2.setStyleSheet("background-color: yellow; border-radius : 30; border : 2px solid black")
                self.label1.setStyleSheet("background-color: yellow; border-radius : 30; border : 2px solid black")
            self.actionZapisz_gr.setEnabled(False)

    def isGameEnd(self):
        firstPlayer = 1
        secondPlayer = 1
        for x in range(0, 6):
            if self.buttonList[x].text() != "0":
                firstPlayer = 0
                break
        for x in range(7, 13):
            if self.buttonList[x].text() != "0":
                secondPlayer = 0
                break
        if firstPlayer or secondPlayer:
            return True
        else:
            return False

    def whoWin(self):
        if int(self.buttonList[6].text()) > int(self.buttonList[13].text()):
            return 1
        elif int(self.buttonList[6].text()) < int(self.buttonList[13].text()):
            return 2
        else:
            return 0

    def infoMessage(self):
        print("INFO")
        msg = QMessageBox()
        msg.setWindowTitle("INFO")
        msg.setText("Mankala jest to gra logiczna składająca się z 12 pól tzw. domków i dwóch większych tzw. domów. Do każdego z graczy należy sześć pól leżących przed nim i dom po jego prawej stronie. Na początku gry w każdym z pól znajdują się 4 kamienie.\n\nRUCH KAMIENI \nRuch polega na wyjęciu wszystkich kamieni z któregokolwiek z 6 własnych pól i „rozsianiu” po jednym do kolejnych pól (nie omijając własnego domu i pól należących do drugiego gracza) w kierunku odwrotnym do wskazówek zegara. Przy pełnym okrążeniu planszy kamienie omijają pole startowe. Jeżeli ostatni kamień wyląduje we własnym domku gracz wykonuje następny ruch. Jeśli nie – kolejkę przejmuje drugi gracz.\n\nPRZEJMOWANIE KAMIENI (BICIE)\nJeśli ostatni kamień wyląduje na własnym pustym polu – gracz zabiera wszystkie kamienie z przyległego pola po drugiej stronie planszy i wraz z ostatnim rozsiewanym kamieniem umieszcza w swoim domu (zbicie). Jeżeli w przyległym polu nie ma kamieni nic nie jest przejmowane (bite). Tak samo, ruch nie kończy się biciem, jeżeli ostatni kamień wyląduje na pustym polu przeciwnika.\n\nCEL GRY\nCelem gry jest zebranie we własnym domu jak największej ilości kamieni.\n\nKONIEC GRY \nGra kończy się kiedy wszystkie pola jednego z graczy są puste. W takiej sytuacji pozostałe kamienie lądują w domu drugiego gracza. Wygrywa ten, kto zdobędzie większą ilość kamieni.")
        x = msg.exec_()

    def saveGame(self):
        fileName, _ = QFileDialog.getSaveFileName(None, "Zapisz grę", "", "Mancala Files (*.mancala)")
        if fileName == "":
            return
        f = open(fileName, "w")
        for i in self.buttonList:
            f.write(i.text()+"\n")
        f.write(str(self.whoMove))
        f.close()

    def loadGame(self):
        a = self.checkMessage("Czy na pewno wczytać grę?")
        if not a:
            return
        b = self.checkMessage("Czy chcesz zapisać istniejącą grę?")
        if b:
            self.saveGame()

            if not self.isGameEnd():
                b = self.checkMessage("Czy chcesz zapisać istniejącą grę?")
                if b:
                    self.saveGame()


        self.readFile()
        self.checkWhoMove()

    def readFile(self):
        fileName, _ = QFileDialog.getOpenFileName(None, "Wczytaj grę", "", "Mancala Files (*.mancala)")
        if fileName == "":
            return
        f = open(fileName, "r")
        count = 0
        while True:
            line = f.readline()
            if not line:
                break
            if count < 14:
                self.buttonList[count].setText(line[0])
            else:
                self.whoMove = int(line[0])
            count += 1
        f.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator = QTranslator()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
