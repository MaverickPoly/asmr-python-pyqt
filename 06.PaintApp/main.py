import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QSize

# Colors
COLORS = [
    QColor(255, 0, 0), QColor(0, 255, 0), QColor(0, 0, 255), QColor(0, 0, 0),
    QColor(255, 155, 0), QColor(120, 120, 120), QColor(0, 150, 255),
    QColor(200, 255, 0), QColor(150, 0, 255), QColor(255, 0, 155),
]


class Canvas(QWidget):
    def __init__(self, color, thickness):
        super().__init__()
        self.setFixedSize(1300, 700)

        self.color = color
        self.thickness = thickness

        self.canvas = QPixmap(self.size())
        self.canvas.fill(Qt.white)

        self.last_point = QPoint()
        self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.canvas)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            painter = QPainter(self.canvas)
            pen = QPen(self.color, self.thickness, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def clear_canvas(self):
        self.canvas.fill(Qt.white)
        self.update()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Paint App")

        layout = QVBoxLayout()
        self.canvas = Canvas(COLORS[0], 4)
        layout.addWidget(self.canvas)

        # Buttons
        button_layout = QHBoxLayout()

        colors_layout = QHBoxLayout()
        for color in COLORS:
            btn = QPushButton()
            color_rgba = f"rgba({color.red()}, {color.green()}, {color.blue()}, {color.alpha()})"
            btn.setStyleSheet(f"""
                background: {color_rgba};
                width: 30px;
                height: 30px;
                border-radius: 6px;
            """)
            print(color_rgba)
            btn.clicked.connect(lambda _, c=color: self.set_pen_color(c))
            colors_layout.addWidget(btn)
            # btn.setFixedSize(QSize(10, 10))

        slider = QSlider(Qt.Horizontal)
        slider.setTickInterval(1)
        slider.setMinimum(1)
        slider.setMaximum(20)
        slider.setValue(4)
        slider.valueChanged.connect(self.slider_change)

        clear_btn = QPushButton("Clear")
        clear_btn.clicked.connect(self.canvas.clear_canvas)
        button_layout.setSpacing(20)
        button_layout.addLayout(colors_layout)
        button_layout.addWidget(slider)
        button_layout.addWidget(clear_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def set_pen_color(self, color):
        print("Changing color:", color)
        self.canvas.color = color

    def slider_change(self, value):
        self.canvas.thickness = value


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
