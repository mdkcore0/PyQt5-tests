import QtQuick 2.0

Rectangle {
    id: root

    color: "black"

    MultiPointTouchArea {
        anchors.fill: parent

        onPressed: {
            var colors = ["red", "yellow", "green", "orange", "cyan",
                "lime", "blue", "magenta", "pink", "white"];
            var component = Qt.createComponent("Location.qml");

            for (var i = 0; i < touchPoints.length; ++i) {
                var location = component.createObject(root);

                location.color = colors[i % colors.length];
                location.xPos = touchPoints[i].x;
                location.yPos = touchPoints[i].y;
                location.id = i;
            }
        }
    }
}
