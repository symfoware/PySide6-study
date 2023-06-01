import QtQuick
import QtQuick3D
import QtQuick3D.Helpers
import TriangleGeometry

Window {
    id: window
    width: 500
    height: 500
    visible: true
    //color: "#848895"

    View3D {
        id: v3d
        anchors.fill: parent
        camera: camera

        PerspectiveCamera {
            id: camera
            position: Qt.vector3d(0, 0, 10)
        }

        DirectionalLight {
            position: Qt.vector3d(-10, 10, -10)
            color: Qt.rgba(1.0, 1.0, 1.0, 1.0)
            //ambientColor: Qt.rgba(0.1, 0.1, 0.1, 1.0)
        }

        //! [model triangle]
        Model {
            visible: true
            scale: Qt.vector3d(4, 4, 4)
            geometry: TriangleGeometry {
            }
            materials: [
                DefaultMaterial {
                    diffuseColor: "#90ee90"
                }
            ]
        }
        //! [model triangle]


    }

    WasdController {
        controlledObject: camera
    }

}
