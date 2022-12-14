# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    """
    A class that builds the GUI window with PyQt5.
    """
    def setupUi(self, MainWindow):
        """
        A method that creates objects, sets object names, and sets their properties.
        :param MainWindow: The space created in PyQtDesigner where all widgets are added.
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1132, 853)
        MainWindow.setMinimumSize(QtCore.QSize(1132, 853))
        MainWindow.setMaximumSize(QtCore.QSize(1132, 853))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(340, 20, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.explanation = QtWidgets.QLabel(self.centralwidget)
        self.explanation.setGeometry(QtCore.QRect(80, 120, 2471, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.explanation.setFont(font)
        self.explanation.setFocusPolicy(QtCore.Qt.NoFocus)
        self.explanation.setTextFormat(QtCore.Qt.PlainText)
        self.explanation.setObjectName("explanation")
        self.s1scorelabel = QtWidgets.QLabel(self.centralwidget)
        self.s1scorelabel.setGeometry(QtCore.QRect(120, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s1scorelabel.setFont(font)
        self.s1scorelabel.setObjectName("s1scorelabel")
        self.s2scorelabel = QtWidgets.QLabel(self.centralwidget)
        self.s2scorelabel.setGeometry(QtCore.QRect(120, 340, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s2scorelabel.setFont(font)
        self.s2scorelabel.setObjectName("s2scorelabel")
        self.s3scorelabel = QtWidgets.QLabel(self.centralwidget)
        self.s3scorelabel.setGeometry(QtCore.QRect(120, 400, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s3scorelabel.setFont(font)
        self.s3scorelabel.setObjectName("s3scorelabel")
        self.s1sdlabel = QtWidgets.QLabel(self.centralwidget)
        self.s1sdlabel.setGeometry(QtCore.QRect(610, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s1sdlabel.setFont(font)
        self.s1sdlabel.setObjectName("s1sdlabel")
        self.s2sdlabel = QtWidgets.QLabel(self.centralwidget)
        self.s2sdlabel.setGeometry(QtCore.QRect(610, 340, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s2sdlabel.setFont(font)
        self.s2sdlabel.setObjectName("s2sdlabel")
        self.s3sdlabel = QtWidgets.QLabel(self.centralwidget)
        self.s3sdlabel.setGeometry(QtCore.QRect(610, 400, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.s3sdlabel.setFont(font)
        self.s3sdlabel.setObjectName("s3sdlabel")
        self.r12label = QtWidgets.QLabel(self.centralwidget)
        self.r12label.setGeometry(QtCore.QRect(120, 460, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r12label.setFont(font)
        self.r12label.setObjectName("r12label")
        self.r13label = QtWidgets.QLabel(self.centralwidget)
        self.r13label.setGeometry(QtCore.QRect(120, 520, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r13label.setFont(font)
        self.r13label.setObjectName("r13label")
        self.r23label = QtWidgets.QLabel(self.centralwidget)
        self.r23label.setGeometry(QtCore.QRect(120, 580, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.r23label.setFont(font)
        self.r23label.setObjectName("r23label")
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(510, 660, 93, 28))
        self.calculateButton.setObjectName("calculateButton")
        self.outputComposite = QtWidgets.QLabel(self.centralwidget)
        self.outputComposite.setGeometry(QtCore.QRect(120, 710, 911, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outputComposite.setFont(font)
        self.outputComposite.setText("")
        self.outputComposite.setObjectName("outputComposite")
        self.s1scoreinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s1scoreinput.setGeometry(QtCore.QRect(360, 280, 121, 31))
        self.s1scoreinput.setObjectName("s1scoreinput")
        self.s3scoreinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s3scoreinput.setGeometry(QtCore.QRect(360, 400, 121, 31))
        self.s3scoreinput.setObjectName("s3scoreinput")
        self.s2scoreinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s2scoreinput.setGeometry(QtCore.QRect(360, 340, 121, 31))
        self.s2scoreinput.setObjectName("s2scoreinput")
        self.r12input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.r12input.setGeometry(QtCore.QRect(360, 460, 121, 31))
        self.r12input.setObjectName("r12input")
        self.r13input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.r13input.setGeometry(QtCore.QRect(360, 520, 121, 31))
        self.r13input.setObjectName("r13input")
        self.r23input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.r23input.setGeometry(QtCore.QRect(360, 580, 121, 31))
        self.r23input.setObjectName("r23input")
        self.s1sdinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s1sdinput.setGeometry(QtCore.QRect(870, 280, 121, 31))
        self.s1sdinput.setObjectName("s1sdinput")
        self.s2sdinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s2sdinput.setGeometry(QtCore.QRect(870, 340, 121, 31))
        self.s2sdinput.setObjectName("s2sdinput")
        self.s3sdinput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.s3sdinput.setGeometry(QtCore.QRect(870, 400, 121, 31))
        self.s3sdinput.setObjectName("s3sdinput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1132, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow) -> None:
        """
        Sets the window title and adds all text to the main window, including text from buttons and labels.
        :param MainWindow: The space created in PyQtDesigner where all widgets are added.
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Composite IQ Score Calculator"))
        self.title.setText(_translate("MainWindow", "Composite IQ Score Calculator"))
        self.explanation.setText(_translate("MainWindow", "This application calculates a composite IQ score from "
                                                          "three subtests. The calculated composite has a mean of "
                                                          "100 and a standard\n"
                                                          "deviation of 15.\n"
                                                          "\n"
                                                          "In order to calculate a composite IQ score from three "
                                                          "subtests, you must enter your scores on each subtest, "
                                                          "the standard deviations\n"
                                                          "of each subtest, and the correlations between scores on "
                                                          "each subtest (ie: correlations between subtests 1 and 2, "
                                                          "subtests 1 and 3,\n"
                                                          "and subtests 2 and 3). A mean score of 100 is assumed for "
                                                          "each subtest.\n"
                                                          "\n"
                                                          ""))
        self.s1scorelabel.setText(_translate("MainWindow", "Subtest 1 Score: "))
        self.s2scorelabel.setText(_translate("MainWindow", "Subtest 2 Score: "))
        self.s3scorelabel.setText(_translate("MainWindow", "Subtest 3 Score: "))
        self.s1sdlabel.setText(_translate("MainWindow", "Subtest 1 Standard Deviation: "))
        self.s2sdlabel.setText(_translate("MainWindow", "Subtest 2 Standard Deviation: "))
        self.s3sdlabel.setText(_translate("MainWindow", "Subtest 3 Standard Deviation: "))
        self.r12label.setText(_translate("MainWindow", "Subtests 1 & 2 Correlation: "))
        self.r13label.setText(_translate("MainWindow", "Subtests 1 & 3 Correlation: "))
        self.r23label.setText(_translate("MainWindow", "Subtests 2 & 3 Correlation: "))
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
