import struct
from PySide6.QtGui import QVector3D
from PySide6.QtQml import QmlElement
from PySide6.QtQuick3D import QQuick3DGeometry
from PySide6.QtCore import QByteArray

QML_IMPORT_NAME = 'CubeGeometry'
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class CubeGeometry(QQuick3DGeometry):

    def __init__(self, parent=None):
        QQuick3DGeometry.__init__(self, parent)
        self.updateData()


    def updateData(self):
        self.clear()

        points = [
            [1,  1,  1],
            [1,  1, -1],
            [-1,  1,  1],
            [-1,  1, -1],

            [1, -1,  1],
            [1, -1, -1],
            [-1, -1,  1],
            [-1, -1, -1],

            [1,  1,  1],
            [-1,  1,  1],
            [1,  1, -1],
            [-1,  1, -1],

            [1, -1,  1],
            [-1, -1,  1],
            [1, -1, -1],
            [-1, -1, -1],

            [1,  1,  1],
            [1, -1,  1],
            [1,  1, -1],
            [1, -1, -1],

            [-1,  1,  1],
            [-1, -1,  1],
            [-1,  1, -1],
            [-1, -1, -1]
        ]

        FLOAT_SIZE = 4
        STRIDE = 3 # x,y,z
        vertexData = QByteArray()
        for x, y, z in points:
            vertexData.append(struct.pack('<f', x))
            vertexData.append(struct.pack('<f', y))
            vertexData.append(struct.pack('<f', z))
        
        self.setVertexData(vertexData)
        self.setStride(STRIDE * FLOAT_SIZE)
        self.setBounds(QVector3D(-1.0, -1.0, 0.0), QVector3D(+1.0, +1.0, 0.0))
        self.setPrimitiveType(QQuick3DGeometry.PrimitiveType.Lines)
        self.addAttribute(
            QQuick3DGeometry.Attribute.PositionSemantic, 0, QQuick3DGeometry.Attribute.F32Type
        )


"""
QQuick3DGeometry.PrimitiveType
https://doc.qt.io/qt-6/qquick3dgeometry.html#setPrimitiveType
Points	The primitives are points.
LineStrip	The primitives are lines in a strip.
Lines	The primitives are lines in a list.
TriangleStrip	The primitives are triangles in a strip.
TriangleFan	The primitives are triangles in a fan. Be aware that triangle fans may not be supported at run time, depending on the underlying graphics API.
Triangles	The primitives are triangles in a list.
"""
