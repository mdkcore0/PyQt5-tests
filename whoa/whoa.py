#!/usr/bin/env python

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView

if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = QQuickView()
    view.setSource(QUrl("example.qml"))
    view.show()

    sys.exit(app.exec_())
