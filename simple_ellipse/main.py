#!/usr/bin/env python

import sys
import os

from simple_ellipse import SimpleEllipse

from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import QUrl

if __name__ == '__main__':
    app = QApplication(sys.argv)

    qmlRegisterType(SimpleEllipse, "Shapes", 1, 0, "SimpleEllipse")

    view = QQuickView()
    view.resize(480, 480)

    view.setResizeMode(QQuickView.SizeRootObjectToView)
    view.setSource(QUrl.fromLocalFile(
        os.path.join(os.path.dirname(__file__), 'qml/main.qml')))

    view.show()

    sys.exit(app.exec_())
