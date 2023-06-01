import os
import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QSurfaceFormat
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtQuick3D import QQuick3D

from triangle import TriangleGeometry

if __name__ == '__main__':
    os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Basic'
    app = QGuiApplication(sys.argv)

    QSurfaceFormat.setDefaultFormat(QQuick3D.idealSurfaceFormat())

    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile('main.qml'))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
