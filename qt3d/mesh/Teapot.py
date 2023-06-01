import sys
from PySide6.QtGui import (QGuiApplication, QVector3D, QColor)
from PySide6.Qt3DCore import (Qt3DCore, )
from PySide6.Qt3DExtras import (Qt3DExtras)
from PySide6.Qt3DRender import (Qt3DRender)
from PySide6.QtCore import (QUrl)

class Window(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()
        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(0, 10, 10))
        self.camera().setViewCenter(QVector3D(0, 1, 0))
        self.camera().setUpVector(QVector3D(0, 1, 0))

        self.rootEntity = self.createScene()
        self.setRootEntity(self.rootEntity)

        # For camera controls
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(100)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())
        
        self.resize(500, 500)


    def createScene(self):
        # Root entity
        rootEntity = Qt3DCore.QEntity()
        entity = Qt3DCore.QEntity(rootEntity)

        # Material
        material = Qt3DExtras.QDiffuseSpecularMaterial(rootEntity)
        # Diffuse: ライトによる表面の凹凸を表現するための色(color)
        material.setDiffuse(QColor(144, 238, 144))
        # Ambient: 他の光源がない状態で物体が放つ色(color)
        material.setAmbient(QColor(0, 128, 0))
        
        # Mesh
        mesh = Qt3DRender.QMesh(entity)
        # ファイルを読み込み
        mesh.setSource(QUrl.fromLocalFile('teapot.obj'))

        entity.addComponent(mesh)
        entity.addComponent(material)
        return rootEntity

if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    view = Window()
    view.show()
    sys.exit(app.exec())

    