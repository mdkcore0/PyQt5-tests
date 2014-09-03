#!/usr/bin/env python

import sys

from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QObject
from PyQt5.QtCore import QUrl

from PyQt5.QtQml import qmlRegisterType
from PyQt5.QtQml import QQmlComponent
from PyQt5.QtQml import QQmlEngine

class Person(QObject):
    def __init__(self, parent=None):
        super(Person, self).__init__(parent)

        self._name = ''
        self._shoeSize = 0

    @pyqtProperty('QString')
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @pyqtProperty(int)
    def shoeSize(self):
        return self._shoeSize

    @shoeSize.setter
    def shoeSize(self, shoeSize):
        self._shoeSize = shoeSize

app = QCoreApplication(sys.argv)

qmlRegisterType(Person, 'People', 1, 0, 'Person')
engine = QQmlEngine()

component = QQmlComponent(engine)
component.loadUrl(QUrl('example.qml'))

person = component.create()

if person is not None:
    print "The person's name is %s." % person.name
    print "They wear a size %d shoe." % person.shoeSize
else:
    for error in component.errors():
        print error.toString()
