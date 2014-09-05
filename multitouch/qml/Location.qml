import QtQuick 2.0

Item {
    property color color: "black"
    property int xPos: 0
    property int yPos: 0
    property int id: -1

    anchors.fill: parent

    Rectangle {
        color: parent.color
        x: 0
        y: parent.yPos

        width: parent.width
        height: 4
    }

    Rectangle {
        color: parent.color
        x: parent.xPos
        y: 0

        width: 4
        height: parent.height
    }

    Text {
        x: parent.xPos + 8
        y: parent.yPos + 8

        text: "%1: (%2, %3)".arg(parent.id).arg(parent.xPos).arg(parent.yPos)
        color: parent.color
    }
}
