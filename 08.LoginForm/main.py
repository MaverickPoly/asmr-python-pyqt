import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()

        # Window
        self.setWindowTitle("Login Form")
        self.setGeometry(600, 200, 600, 800)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        box = QWidget()
        box.setStyleSheet("""
            border-radius: 12px;
            border: 1px solid #ddd;
            padding: 0px 100px;
        """)
        box_layout = QVBoxLayout()
        box.setLayout(box_layout)

        # Top Title
        title = QLabel("Login Form")
        title.setStyleSheet("""
            font-size: 36px;
            border: none;
        """)
        title.setFixedHeight(50)
        title.setAlignment(Qt.AlignCenter)
        box_layout.addWidget(title)

        # Login Input
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Login...")
        self.login_input.setStyleSheet("""
            padding: 12px;
            border-radius: 10px;
            font-size: 20px;
        """)
        box_layout.addWidget(self.login_input)

        # Password Input
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password...")
        self.password_input.setStyleSheet("""
            padding: 12px;
            border-radius: 10px;
            font-size: 20px;
        """)
        box_layout.addWidget(self.password_input)

        # Submit Button
        btn = QPushButton("Login")
        btn.setStyleSheet("""
            QPushButton {
                font-size: 20px;
                border-radius: 12px;
                padding: 12px;
                background: rgb(0, 0, 150);
                color: white;
            }
            QPushButton:hover {
                background: rgb(0, 0, 190);
            }
        """)
        btn.clicked.connect(self.handle_submit)
        box_layout.addWidget(btn)

        layout.addWidget(box)
        self.setLayout(layout)


    def handle_submit(self):
        login = self.login_input.text()
        password = self.password_input.text()

        if login == "admin" and password == "123":
            QMessageBox.information(None, "Success", "Logged in successfully!")
        else:
            QMessageBox.information(None, "Failure", "Invalid login or password!")


def main():
    application = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    application.exec()


if __name__ == '__main__':
    main()
