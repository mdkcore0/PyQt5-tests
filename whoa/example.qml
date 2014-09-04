import QtQuick 2.0

Item {
    id: root

    width: 300
    height: 100

    Rectangle {
        anchors.fill: parent

        color: "gray"

        Text {
            anchors.horizontalCenter: parent.horizontalCenter

            text: "WHOAAA"
            color: "blue"
            font.pointSize: 32
        }
    }
}
