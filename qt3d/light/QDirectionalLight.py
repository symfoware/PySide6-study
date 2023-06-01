import sys
from PySide6.QtGui import (QGuiApplication, QVector3D, QColor)
from PySide6.Qt3DCore import (Qt3DCore)
from PySide6.Qt3DExtras import (Qt3DExtras)
from PySide6.Qt3DRender import (Qt3DRender)


class Window(Qt3DExtras.Qt3DWindow):
    def __init__(self):
        super().__init__()
        # Camera
        self.camera().lens().setPerspectiveProjection(45, 16 / 9, 0.1, 1000)
        self.camera().setPosition(QVector3D(10, 10, 10))
        self.camera().setViewCenter(QVector3D(0, 0, 0))

        self.rootEntity = self.createScene()
        self.setRootEntity(self.rootEntity)

        # For camera controls
        self.camController = Qt3DExtras.QOrbitCameraController(self.rootEntity)
        self.camController.setLinearSpeed(100)
        self.camController.setLookSpeed(180)
        self.camController.setCamera(self.camera())

        # 光源
        light = Qt3DRender.QDirectionalLight(self.rootEntity)
        # 色
        light.setColor(QColor(0, 255, 0))
        # 光の強さ
        light.setIntensity(1)
        # 光源の位置
        light.setWorldDirection(QVector3D(-1, -1, -1))
        
        self.rootEntity.addComponent(light)

        
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