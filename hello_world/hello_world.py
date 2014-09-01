#!/usr/bin/env python

import sys
from PyQt5.QtWidgets import QApplication, QWidget

a = QApplication([])
w = QWidget()

w.resize(320, 240)
w.setWindowTitle("FIRST BLOOD!")
w.show()

sys.exit(a.exec_())
