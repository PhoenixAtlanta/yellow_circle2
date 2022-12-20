import sys
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.btn_add.clicked.connect(self.check_draw)

        self.value_draw = False

        self.btn_add.clicked.connect(self.check_draw)

    def check_draw(self):
        self.value_draw = True  # разрешаем рисовать
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if self.value_draw:
            qp = QPainter()
            # Начинаем процесс рисования
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()  # Завершаем рисование
            self.value_draw = False

    def draw_circle(self, qp):
        # Задаем кисть
        qp.setBrush(QColor("yellow"))
        radius = randint(10, 200)  # создаем радиус
        qp.drawEllipse(self.size().width() // 2 - (radius // 2), self.size().height() // 2 - (radius // 2),
                       radius, radius)  # рисуем круг по центру экрана
        qp.setBrush(QColor(0, 255, 0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ye = YellowCircle()
    ye.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
