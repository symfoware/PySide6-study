import struct
from PySide6.QtGui import QVector3D
from PySide6.QtQml import QmlElement
from PySide6.QtQuick3D import QQuick3DGeometry
from PySide6.QtCore import QByteArray

QML_IMPORT_NAME = 'TriangleGeometry'
QML_IMPORT_MAJOR_VERSION = 1


@QmlElement
class TriangleGeometry(QQuick3DGeometry):

    def __init__(self, parent=None):
        QQuick3DGeometry.__init__(self, parent)
        self.updateData()


    def updateData(self):
        self.clear()

        stride = 3

        # We use numpy arrays to handle the vertex data,
        # but still we need to consider the 'sizeof(float)'
        # from C to set the Stride, and Attributes for the
        # underlying Qt methods
        FLOAT_SIZE = 4
        vertexData = QByteArray()

        # a triangle, front face = counter-clockwise
        vertexData.append(struct.pack('<f', -1.0))
        vertexData.append(struct.pack('<f', -1.0))
        vertexData.append(struct.pack('<f', 0.0))

        vertexData.append(struct.pack('<f', 1.0))
        vertexData.append(struct.pack('<f', -1.0))
        vertexData.append(struct.pack('<f', 0.0))
        
        vertexData.append(struct.pack('<f', 0.0))
        vertexData.append(struct.pack('<f', 1.0))
        vertexData.append(struct.pack('<f', 0.0))
        
        self.setVertexData(vertexData)
        self.setStride(stride * FLOAT_SIZE)
        self.setBounds(QVector3D(-1.0, -1.0, 0.0), QVector3D(+1.0, +1.0, 0.0))
        self.setPrimitiveType(QQuick3DGeometry.PrimitiveType.Triangles)
        self.addAttribute(
            QQuick3DGeometry.Attribute.PositionSemantic, 0, QQuick3DGeometry.Attribute.F32Type
        )


"""
https://doc.qt.io/qt-6/qquick3dgeometry.html#setPrimitiveType
Points	The primitives are points.
LineStrip	The primitives are lines in a strip.
Lines	The primitives are lines in a list.
TriangleStrip	The primitives are triangles in a strip.
TriangleFan	The primitives are triangles in a fan. Be aware that triangle fans may not be supported at run time, depending on the underlying graphics API.
Triangles	The primitives are triangles in a list.
"""
