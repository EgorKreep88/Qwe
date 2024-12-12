import sys
import random
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        try:
            uic.loadUi('ui.ui', self)
        except Exception as e:
            print(f"Ошибка загрузки ui.ui: {e}")
            sys.exit(1)


        self.circles = []


        self.btnAddCircle.clicked.connect(self.add_circle)
        self.btnEditCoffee.clicked.connect(self.open_add_edit_form)

    def add_circle(self):

        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        diameter = random.randint(20, 100)
        self.circles.append((color, diameter))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for color, diameter in self.circles:
            painter.setBrush(color)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            painter.drawEllipse(x, y, diameter, diameter)

    def open_add_edit_form(self):
        try:

            self.add_edit_form = AddEditCoffeeForm(self)
            self.add_edit_form.show()
        except Exception as e:
            print(f"Ошибка открытия формы добавления/редактирования кофе: {e}")


class AddEditCoffeeForm(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AddEditCoffeeForm, self).__init__(parent)
        try:
            uic.loadUi('addEditCoffeeForm.ui', self)
        except Exception as e:
            print(f"Ошибка загрузки addEditCoffeeForm.ui: {e}")
            sys.exit(1)


        self.btnSave.clicked.connect(self.save_coffee)
        self.btnCancel.clicked.connect(self.close)

    def save_coffee(self):

        coffee_name = self.lineEditCoffeeName.text()
        coffee_type = self.lineEditCoffeeType.text()
        print(f"Сохранено: {coffee_name}, Тип: {coffee_type}")
        self.close()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
