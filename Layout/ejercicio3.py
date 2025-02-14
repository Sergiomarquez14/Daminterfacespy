import sys
from PyQt6.QtWidgets import (
    QHBoxLayout, QMainWindow, QWidget, QApplication, QVBoxLayout
)
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")

        layout1 = QVBoxLayout() 
        layout2 = QHBoxLayout() 
        layout3 = QHBoxLayout()

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)
        layout2.setSpacing(20)
        layout3.setSpacing(20)

        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('yellow'))

        layout3.addWidget(Color('purple'))
        layout3.addWidget(Color('red'))

        layout1.addLayout(layout2)
        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
