#!/usr/bin/env python

import sys
import os
from PyQt5.QtCore import QFile
from PyQt5.QtCore import QFileInfo
from PyQt5.QtCore import QTextCodec

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QFileDialog

class Notepad(QMainWindow):
    def __init__(self):
        super(Notepad, self).__init__()
        self.initUI()

    def initUI(self):
        openAction = QAction('Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open a file')
        openAction.triggered.connect(self.openFile)

        closeAction = QAction('Close', self)
        closeAction.setShortcut('Ctrl+Q')
        closeAction.setStatusTip('Close Nopepad')
        closeAction.triggered.connect(self.close)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(openAction)
        fileMenu.addAction(closeAction)

        self.textEdit = QTextEdit(self)
        self.textEdit.setFocus()
        self.textEdit.setReadOnly(True)

        self.resize(700, 800)
        self.setWindowTitle('Nopepad')
        self.setCentralWidget(self.textEdit)
        self.show()

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File',
                os.getenv('HOME'))

        if not filename:
            return

        fh = ''

        if QFile.exists(filename):
            fh = QFile(filename)

        if not fh.open(QFile.ReadOnly):
            QtGui.qApp.quit()

        data = fh.readAll()
        codec = QTextCodec.codecForUtfText(data)
        unistr = codec.toUnicode(data)

        tmp = ('Nopepad: %s' % filename)
        self.setWindowTitle(tmp)

        basename = QFileInfo(fh).baseName()
        self.statusBar().showMessage('File \'%s\' loaded' % basename)

        self.textEdit.setText(unistr)

def main():
    app = QApplication(sys.argv)
    notepad = Notepad()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
