import sys
import random
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.pushButton.clicked.connect(self.add_circle)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Окружности')

    def paintEvent(self, event):
        self.update()

    def add_circle(self):
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for _ in range(10):  # Рисуем 10 окружностей
            color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            painter.setBrush(color)
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

