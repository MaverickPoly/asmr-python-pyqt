import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ColorPicker(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Color Picker")
        self.setGeometry(200, 200, 500, 500)

        self.color = (255, 255, 255, 255)

        layout = QVBoxLayout()
        button = QPushButton("Choose Color")
        button.clicked.connect(self.choose_color)
        layout.addWidget(button)

        self.label = QLabel(str(self.color))
        self.label.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.update_bg()

    def choose_color(self):
        color = QColorDialog.getColor()
        if not color.isValid():
            return
        self.color = color.red(), color.green(), color.blue(), color.alpha()
        self.update_bg()


    def update_bg(self):
        self.setStyleSheet(f"""
            background-color: rgba{self.color}; 
        """)
        self.label.setText(str(self.color))


def main():
    app = QApplication(sys.argv)
    window = ColorPicker()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
