import sys
from PySide6.QtGui import (QGuiApplication, QVector3D)
from PySide6.Qt3DCore import (Qt3DCore)
from PySide6.Qt3DExtras import (Qt3DExtras)

class Window(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()

        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(20, 20, 20))
        self.camera().setViewCenter(QVector3D(0, 0, 0))
        
        # For camera controls
        self.rootEntity = self.createScene()

        self.setRootEntity(self.rootEntity)

        self.resize(500, 500)

    def createScene(self):
        # Root entity
        rootEntity = Qt3DCore.QEntity()

        # Material
        material = Qt3DExtras.QDiffuseSpecularMaterial(rootEntity)
        
        entity = Qt3DCore.QEntity(rootEntity)
        # 直方体
        mesh = Qt3DExtras.QCuboidMesh(entity)
        mesh.setXExtent(5) # X軸サイズ
        mesh.setYExtent(5) # Y軸サイズ
        mesh.setZExtent(5) # Z軸サイズ

        entity.addComponent(mesh)
        entity.addComponent(material)

        return rootEntity


if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    view = Window()
    view.show()
    sys.exit(app.exec())
