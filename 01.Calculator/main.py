import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Btn:
    def __init__(self, text: str, row: int, col: int, bg: str, col_span: int):
        self.text = text
        self.row = row
        self.col = col
        self.bg = bg
        self.col_span = col_span


# Settings
CELL_SIZE = 150
WIDTH, HEIGHT = CELL_SIZE * 4, CELL_SIZE * 6

BUTTONS = [
    Btn("C", 0, 0, "red", 1),
    Btn("D", 0, 1, "red", 1),
    Btn("%", 0, 2, "orange", 1),
    Btn("+", 0, 3, "orange", 1),

    Btn("7", 1, 0, "white", 1),
    Btn("8", 1, 1, "white", 1),
    Btn("9", 1, 2, "white", 1),
    Btn("-", 1, 3, "orange", 1),

    Btn("4", 2, 0, "white", 1),
    Btn("5", 2, 1, "white", 1),
    Btn("6", 2, 2, "white", 1),
    Btn("*", 2, 3, "orange", 1),

    Btn("1", 3, 0, "white", 1),
    Btn("2", 3, 1, "white", 1),
    Btn("3", 3, 2, "white", 1),
    Btn("/", 3, 3, "orange", 1),

    Btn("0", 4, 0, "white", 2),
    Btn(".", 4, 2, "white", 1),
    Btn("=", 4, 3, "green", 1),
]


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(0, 0, WIDTH, HEIGHT)
        self.center_on_screen()


        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 24))
        self.input_field.setAlignment(Qt.AlignRight)
        self.input_field.setStyleSheet(f"""
            QLineEdit {{
                border-radius: 8px;
                border: 1px solid #ccc;
                height: {CELL_SIZE - 50};
            }}
            QLineEdit:focus {{
                border: 1px solid #999;
            }}
        """)
        self.main_layout.addWidget(self.input_field)

        self.grid = QGridLayout()
        self.main_layout.addLayout(self.grid)

        self.generate_buttons()

    def generate_buttons(self):
        for btn in BUTTONS:
            button = QPushButton()
            button.setText(btn.text)
            button.setStyleSheet(f"""
                QPushButton {{
                    background: {btn.bg};
                    width: {CELL_SIZE}px;
                    height: {CELL_SIZE}px;
                    color: #222;
                    font-weight: 400;
                    font-size: 35px;
                    cursor: pointer;
                    border-radius: 12px;
                    border: 1px solid #eee;
                }}
                QPushButton:hover {{
                    border: 1px solid #888;
                }}
            """)

            match btn.text:
                case 'C':
                    button.clicked.connect(self.clear_input_field)
                case 'D':
                    button.clicked.connect(self.delete_char)
                case '%':
                    button.clicked.connect(self.calculate_percent)
                case '=':
                    button.clicked.connect(self.calculate)
                case _:
                        button.clicked.connect(lambda _, b=btn: self.add_char(b.text))

            self.grid.addWidget(button, btn.row, btn.col, 1, btn.col_span)

    def add_char(self, char: str):
        self.input_field.setText(self.input_field.text() + char)

    def clear_input_field(self):
        self.input_field.setText("")

    def delete_char(self):
        self.input_field.setText(self.input_field.text()[:-1])

    def calculate_percent(self):
        try:
            res = str(eval(self.input_field.text()) / 100)
            self.input_field.setText(res)
        except:
            self.input_field.setText("Error!")

    def calculate(self):
        try:
            res = str(eval(self.input_field.text()))
            if res.isdigit():
                res = str(int(res))
            else:
                res = str(round(float(res), 2))
            self.input_field.setText(res)
        except:
            self.input_field.setText("Error!")

    def center_on_screen(self):
        resolution = QDesktopWidget().screenGeometry()
        self.move(resolution.width() // 2 - self.frameSize().width() // 2,
                  resolution.height() // 2 - self.frameSize().height() // 2)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
