import QtQuick 2.0
import Shapes 1.0
import QtGraphicalEffects 1.0

Rectangle {
    id: root

    color: "black"

    SimpleEllipse {
        anchors {
            fill: parent
            margins: 10
        }

        color: "green"
        penWidth: 2
        antiAliasing: true
        fill: true
    }

    SimpleEllipse {
        id: colorfulEllipse

        width: root.width * .4
        height: root.height * .4

        anchors.centerIn: parent

        fill: true
        visible: false
    }

    RadialGradient {
        anchors.fill: colorfulEllipse

        source: colorfulEllipse
        horizontalRadius: width
        verticalRadius: height
        smooth: true

        gradient: Gradient {
            GradientStop { position: .0; color: "cyan" }
            GradientStop { position: .5; color: "transparent" }
        }
    }

    SimpleEllipse {
        id: colorfulEllipse2

        width: root.width * .25
        height: root.height * .25

        anchors {
            top: colorfulEllipse.bottom
            horizontalCenter: parent.horizontalCenter
        }

        fill: true
        antiAliasing: true
    }

    RadialGradient {
        anchors.fill: colorfulEllipse2

        source: colorfulEllipse2
        horizontalRadius: width
        verticalRadius: height
        smooth: true

        gradient: Gradient {
            GradientStop { position: 0.000; color: Qt.rgba(1, 0, 0, 1) }
            GradientStop { position: 0.167; color: Qt.rgba(1, 1, 0, 1) }
            GradientStop { position: 0.333; color: Qt.rgba(0, 0, 1, 1) }
            GradientStop { position: 0.500; color: Qt.rgba(0, 1, 1, 1) }
            GradientStop { position: 0.667; color: Qt.rgba(0, 0, 1, 1) }
            GradientStop { position: 0.833; color: Qt.rgba(1, 0, 1, 1) }
            GradientStop { position: 1.000; color: Qt.rgba(1, 0, 0, 1) }
        }
    }
}
