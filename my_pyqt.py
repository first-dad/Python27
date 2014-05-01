# -*- coding: utf-8 -*-

import sys
import os
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, uic


application = QApplication(sys.argv)

class W(QDialog):
    def __init__(self):
        super(W, self).__init__()
        self.WPATH = "w.txt"
        uic.loadUi("w.ui", self)
        self.okButton.clicked.connect(self.onOkClicked)
        self.cancelButton.clicked.connect(self.onCancelClicked)
        self.textEdit.textChanged.connect(self.calcPythons)
        self.listWidget.currentRowChanged.connect(self.listRowChanged)
        self.loadFile()

    def listRowChanged(self, index):
        if index == 0:
            self.textEdit.setText(
                self.textEdit.toPlainText().toUpper()
            )
        else:
            self.textEdit.setText(
                self.textEdit.toPlainText().toLower()
            )

    def calcPythons(self):
        self.countLabel.setText(str(self.textEdit.toPlainText().count("python")))

    def loadFile(self):
        if os.path.exists(self.WPATH):
            self.textEdit.setText(open(self.WPATH).read())

    def saveFile(self):
        open(self.WPATH, "w").write(self.textEdit.toPlainText())


    def onOkClicked(self):
        print "onOkClicked"
        self.saveFile()

    def onCancelClicked(self):
        self.close()


if __name__ == '__main__':
    widget = W()

    widget.resize(390, 540)
    widget.setWindowTitle("Hello World!!")
    widget.show()

    sys.exit(application.exec_())