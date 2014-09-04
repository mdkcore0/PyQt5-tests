#!/usr/bin/env python

from PyQt5.QtQuick import QQuickPaintedItem
from PyQt5.QtCore import pyqtProperty
from PyQt5.QtCore import QRectF
from PyQt5.QtCore import QPointF
from PyQt5.QtCore import QSizeF
from PyQt5.QtGui import QPainter
from PyQt5.QtGui import QPen
from PyQt5.QtGui import QColor

class SimpleEllipse(QQuickPaintedItem):
    def __init__(self, parent=None):
        super(SimpleEllipse, self).__init__(parent)

        self._color = QColor()
        self._penWidth = 1
        self._antiAliasing = False
        self._fill = False

    # color related properties
    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    # penWidth related properties
    @pyqtProperty(int)
    def penWidth(self):
        return self._penWidth

    @penWidth.setter
    def penWidth(self, penWidth):
        self._penWidth = penWidth

    # aliasing related properties
    @pyqtProperty(bool)
    def antiAliasing(self):
        return self._antiAliasing

    @antiAliasing.setter
    def antiAliasing(self, antiAliasing):
        self._antiAliasing = antiAliasing

    # fill related properties
    @pyqtProperty(bool)

    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, fill):
        self._fill = fill

    # drawn an ellipse with given properties
    def paint(self, painter):
        penWidth = self._penWidth

        painter.setPen(QPen(self._color, penWidth))
        painter.setRenderHints(QPainter.Antialiasing, self._antiAliasing)

        if self._fill:
            painter.setBrush(self._color)

        start = QPointF(penWidth, penWidth)
        finish = QSizeF(self.width() - penWidth * 2,
                self.height() - penWidth * 2)

        rect = QRectF(start, finish)
        painter.drawEllipse(rect)
