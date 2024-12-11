import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui.ui', self)

        # Подключаем кнопку к обработчику
        self.pushButton.clicked.connect(self.add_circle)

        # Список для хранения окружностей
        self.circles = []

    def add_circle(self):
        # Генерация случайного диаметра и координат
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)

        # Сохраняем окружность как кортеж (x, y, diameter)
        self.circles.append((x, y, diameter))

        # Перерисовываем виджет
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QBrush(QColor(255, 255, 0)))  # Желтый цвет

        # Рисуем все окружности
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
