import QtQuick 2.0

Rectangle {
    id: root

    color: "black"

    MultiPointTouchArea {
        anchors.fill: parent

        onPressed: {
            console.log("Touch")

            for (var i = 0; i < touchPoints.length; ++i)
                console.log(i, touchPoints[i].x, touchPoints[i].y)
        }
    }
}
